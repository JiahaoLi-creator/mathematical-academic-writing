#!/usr/bin/env python3
"""Verify the public-safe v0.4.1 runtime and its sixteen-file core binding."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = ROOT / "provenance/public-release.v1.json"
EXPECTED_CORE_PATHS = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/genre_profiles.md",
    "references/research_article_workflows.md",
    "references/mathematical_integrity.md",
    "references/statistical_source_map.md",
    "references/statistical_analysis_workflows.md",
    "references/statistical_writing.md",
    "references/source_and_derivation_audit.md",
    "references/anti_defensive_audit.md",
    "references/artifact_verification.md",
    "references/visual_companion.md",
    "references/corpus_manifest.md",
    "project_profiles/math3015.md",
    "project_profiles/advanced_mathematical_statistics.md",
    "project_profiles/quantitative_finance.md",
)
EXPECTED_CORE_SHA256 = "07a8468980749d06e2d3ece451910ff4a2de91505153fcb0f4d6403f9a5dfe7f"
EXPECTED_EXCLUDED_MATERIAL = [
    "source_pdfs",
    "extracted_or_normalized_corpus_text",
    "restricted_course_recordings_transcripts_and_frames",
    "private_evidence_registry",
    "blind_regression_oracles",
    "private_evaluation_outputs",
    "source_derived_notebook_fixtures",
    "signing_keys_and_trust_configuration",
    "signed_private_release_metadata",
]
EXPECTED_PRIVATE_LINEAGE = {
    "behavioral_harness_sha256": (
        "24832ab20f7ecc7201c39f4bf953a88b23b68782793a2864de441c4b71de0d01"
    ),
    "candidate_id": "candidate-36a8ddb896f73d2d",
    "candidate_identity_algorithm": "sha256-skill-behavioral-governance-nul-v2",
    "manifest_sha256": "67442c0d4752367ed7ca8e43cd3f5ec15b7b1515d94de2025cc568ad4be08314",
    "manifest_signature_sha256": (
        "23f121ca1032341a2fd88b356f18e485c710dccd2c2547010bbf566dd80d4b58"
    ),
    "note": (
        "Lineage anchors only; private evidence, signatures, and trust configuration are not "
        "reproduced in this public repository."
    ),
    "payload_sha256": "224f46d66d0070bad5b978eef2495ffd73d22e86f6510497445e46777f18e1ad",
    "release_governance_sha256": (
        "3133fca547b1935c57ce53ed844af24b891a8825e8905eb817b6dcd7eab7ea40"
    ),
    "runtime_skill_sha256": (
        "512fa76e8976f571129dd178400aa03af0d6426d7adf6331007dd206df212479"
    ),
    "status": "verified_signed_private_release",
}
EXPECTED_PUBLIC_SANITIZATION = {
    "changes": [
        {
            "operation": "remove_local_relative_links",
            "path": "references/statistical_source_map.md",
            "preserved": "bibliographic_text_and_routing_rules",
            "private_sha256": (
                "bf7df1c7d271ea0deb99cc253e26ef0fcd3e64e3211606ddc79229254a0afec4"
            ),
            "private_size": 6195,
            "public_sha256": (
                "77e9895c1d820b8632308bf78b6d5b20adeac8fa8c59c8431f57101e6849a8c7"
            ),
            "public_size": 6053,
            "removed_link_count": 2,
        }
    ],
    "policy": "narrow-public-path-sanitization-v1",
}
EXPECTED_PUBLIC_FILES = {
    ".gitattributes",
    ".github/workflows/verify-core.yml",
    ".gitignore",
    "CHANGELOG.md",
    "LICENSE",
    "MAINTENANCE.md",
    "README.md",
    "SKILL.md",
    "THIRD_PARTY_NOTICES.md",
    "agents/openai.yaml",
    "assets/usage-workflow.png",
    "examples/quick-start.md",
    "project_profiles/advanced_mathematical_statistics.md",
    "project_profiles/math3015.md",
    "project_profiles/quantitative_finance.md",
    "provenance/public-release.v1.json",
    "references/anti_defensive_audit.md",
    "references/artifact_verification.md",
    "references/corpus_manifest.md",
    "references/genre_profiles.md",
    "references/mathematical_integrity.md",
    "references/research_article_workflows.md",
    "references/source_and_derivation_audit.md",
    "references/statistical_analysis_workflows.md",
    "references/statistical_source_map.md",
    "references/statistical_writing.md",
    "references/visual_companion.md",
    "scripts/verify_public_core.py",
    "tests/draft_cases.json",
    "tests/notebook_samples.json",
    "tests/regression_cases.json",
    "tests/verification_cases.json",
}
TEXT_NAMES = {".gitattributes", ".gitignore", "LICENSE"}
TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
TOKEN_PATTERN = re.compile(
    r"\b(?:"
    r"gh[opusr]_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|"
    r"AKIA[0-9A-Z]{16}|"
    r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}"
    r")\b"
)
ABSOLUTE_USER_PATH_PATTERNS = (
    re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    re.compile(r"/home/[A-Za-z0-9._-]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\]+\\", re.IGNORECASE),
)
PRIVATE_KEY_MARKERS = tuple(
    "-----BEGIN " + key_type + " PRIVATE KEY-----"
    for key_type in ("OPENSSH", "RSA", "EC", "DSA")
)
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)")


class ValidationError(RuntimeError):
    """A public-distribution integrity failure."""


class DuplicateKey(ValueError):
    """A duplicate JSON object key."""


def duplicate_guard(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKey(key)
        result[key] = value
    return result


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_provenance() -> dict[str, Any]:
    raw = PROVENANCE.read_bytes()
    if len(raw) > 128 * 1024:
        raise ValidationError("provenance file exceeds 128 KiB")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=duplicate_guard)
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateKey) as exc:
        raise ValidationError(f"invalid provenance JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError("provenance root must be an object")
    if set(value) != {
        "core",
        "distribution",
        "excluded_material",
        "private_validation_lineage",
        "public_sanitization",
        "schema_version",
    }:
        raise ValidationError("provenance top-level fields are not closed")
    if value["schema_version"] != "1.1.0":
        raise ValidationError("unsupported provenance schema")
    distribution = value["distribution"]
    if distribution != {
        "name": "mathematical-academic-writing",
        "scope": "public_runtime",
        "version": "0.4.1",
    }:
        raise ValidationError("unexpected distribution identity")
    if value["excluded_material"] != EXPECTED_EXCLUDED_MATERIAL:
        raise ValidationError("unexpected excluded-material boundary")
    if value["private_validation_lineage"] != EXPECTED_PRIVATE_LINEAGE:
        raise ValidationError("unexpected private validation lineage")
    if value["public_sanitization"] != EXPECTED_PUBLIC_SANITIZATION:
        raise ValidationError("unexpected public sanitization boundary")
    return value


def snapshot_public_tree() -> dict[str, Path]:
    files: dict[str, Path] = {}
    for current, directories, filenames in os.walk(ROOT, followlinks=False):
        current_path = Path(current)
        if current_path == ROOT:
            directories[:] = [name for name in directories if name != ".git"]
        for name in list(directories):
            path = current_path / name
            if path.is_symlink():
                raise ValidationError(
                    f"symlink directory is not allowed: {path.relative_to(ROOT)}"
                )
        for name in filenames:
            path = current_path / name
            relative = path.relative_to(ROOT).as_posix()
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
                raise ValidationError(f"non-regular file is not allowed: {relative}")
            if info.st_nlink != 1:
                raise ValidationError(f"hard-linked file is not allowed: {relative}")
            files[relative] = path
    observed = set(files)
    if observed != EXPECTED_PUBLIC_FILES:
        missing = sorted(EXPECTED_PUBLIC_FILES - observed)
        extra = sorted(observed - EXPECTED_PUBLIC_FILES)
        raise ValidationError(f"public tree mismatch; missing={missing}, extra={extra}")
    return files


def verify_core(provenance: dict[str, Any], files: dict[str, Path]) -> str:
    core = provenance["core"]
    if not isinstance(core, dict) or set(core) != {
        "aggregate_algorithm",
        "aggregate_sha256",
        "files",
    }:
        raise ValidationError("provenance core fields are not closed")
    if core["aggregate_algorithm"] != "sha256-path-nul-bytes-nul-v1":
        raise ValidationError("unexpected core aggregate algorithm")
    if not isinstance(core["files"], list):
        raise ValidationError("provenance core files must be a list")
    manifest_paths = tuple(entry.get("path") for entry in core["files"])
    if manifest_paths != EXPECTED_CORE_PATHS:
        raise ValidationError("provenance core path order is invalid")

    aggregate = hashlib.sha256()
    for entry in core["files"]:
        if not isinstance(entry, dict) or set(entry) != {"path", "sha256", "size"}:
            raise ValidationError("a provenance core entry is not closed")
        relative = entry["path"]
        expected_hash = entry["sha256"]
        expected_size = entry["size"]
        if not isinstance(expected_hash, str) or HEX64.fullmatch(expected_hash) is None:
            raise ValidationError(f"invalid SHA-256 for {relative}")
        if isinstance(expected_size, bool) or not isinstance(expected_size, int):
            raise ValidationError(f"invalid size for {relative}")
        body = files[relative].read_bytes()
        if len(body) != expected_size:
            raise ValidationError(f"size mismatch: {relative}")
        if sha256_bytes(body) != expected_hash:
            raise ValidationError(f"hash mismatch: {relative}")
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(body)
        aggregate.update(b"\0")

    observed = aggregate.hexdigest()
    expected = core["aggregate_sha256"]
    if not isinstance(expected, str) or HEX64.fullmatch(expected) is None:
        raise ValidationError("invalid aggregate SHA-256")
    if expected != EXPECTED_CORE_SHA256:
        raise ValidationError("provenance does not bind the accepted public-safe v0.4.1 core")
    if observed != expected:
        raise ValidationError(f"core aggregate mismatch: {observed} != {expected}")
    return observed


def scan_text_files(files: dict[str, Path]) -> None:
    for relative, path in files.items():
        if path.name not in TEXT_NAMES and path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValidationError(f"non-UTF-8 public text file: {relative}") from exc
        if any(pattern.search(text) for pattern in ABSOLUTE_USER_PATH_PATTERNS):
            raise ValidationError(f"absolute user path found in {relative}")
        if any(marker in text for marker in PRIVATE_KEY_MARKERS):
            raise ValidationError(f"private key material found in {relative}")
        if TOKEN_PATTERN.search(text):
            raise ValidationError(f"credential-shaped value found in {relative}")


def verify_internal_markdown_links(files: dict[str, Path]) -> int:
    root = ROOT.resolve()
    checked = 0
    for relative, path in files.items():
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = match.group(1)
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if target.startswith(("#", "https://", "http://", "mailto:")):
                continue
            if "://" in target or target.startswith(("data:", "javascript:")):
                raise ValidationError(f"unsupported Markdown link in {relative}: {target}")
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError as exc:
                raise ValidationError(
                    f"Markdown link escapes the public tree in {relative}: {target}"
                ) from exc
            if not resolved.exists():
                raise ValidationError(f"broken internal Markdown link in {relative}: {target}")
            checked += 1
    return checked


def verify_sanitized_file(provenance: dict[str, Any], files: dict[str, Path]) -> None:
    change = provenance["public_sanitization"]["changes"][0]
    body = files[change["path"]].read_bytes()
    if len(body) != change["public_size"]:
        raise ValidationError("sanitized public file size mismatch")
    if sha256_bytes(body) != change["public_sha256"]:
        raise ValidationError("sanitized public file hash mismatch")


def main() -> int:
    try:
        files = snapshot_public_tree()
        provenance = load_provenance()
        aggregate = verify_core(provenance, files)
        scan_text_files(files)
        verify_sanitized_file(provenance, files)
        internal_link_count = verify_internal_markdown_links(files)
    except (OSError, ValidationError) as exc:
        print(json.dumps({"error": str(exc), "status": "failed"}, sort_keys=True))
        return 1
    print(
        json.dumps(
            {
                "core_file_count": len(EXPECTED_CORE_PATHS),
                "core_sha256": aggregate,
                "internal_markdown_links_checked": internal_link_count,
                "public_file_count": len(files),
                "sanitized_file_count": 1,
                "status": "passed",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
