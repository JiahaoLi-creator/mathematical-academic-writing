#!/usr/bin/env python3
"""Verify the public runtime distribution and accepted twelve-file core binding."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = ROOT / "provenance/public-release.v1.json"
EXPECTED_CORE_PATHS = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/genre_profiles.md",
    "references/research_article_workflows.md",
    "references/mathematical_integrity.md",
    "references/source_and_derivation_audit.md",
    "references/anti_defensive_audit.md",
    "references/artifact_verification.md",
    "references/visual_companion.md",
    "references/corpus_manifest.md",
    "project_profiles/math3015.md",
    "project_profiles/quantitative_finance.md",
)
EXPECTED_CORE_SHA256 = "160b00a502b136e2827ea897722e5402c1fb51c5661a116d6701743797eb479c"
EXPECTED_EXCLUDED_MATERIAL = [
    "source_pdfs",
    "extracted_or_normalized_corpus_text",
    "private_evidence_registry",
    "blind_regression_oracles",
    "private_evaluation_outputs",
    "source_derived_notebook_fixtures",
    "signing_keys_and_trust_configuration",
    "signed_private_release_metadata",
]
EXPECTED_PRIVATE_LINEAGE = {
    "harness_sha256": "71f12d684bf852f9c535074cf0a1df70313fad99ac76cc088e81aea0f4efce80",
    "manifest_sha256": "d85b7d166fbc1f28177e947031b88318748a3ca90d94b2a0841dafd4185d09cc",
    "note": (
        "Lineage anchors only; the private harness is not reproducible from this public "
        "repository."
    ),
    "payload_sha256": "193e77e09c1d1a9db7ddaba11a26a0a2ccdd7f84fd76d00830920f81a46b913b",
    "status": "accepted_private_release",
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
        "schema_version",
    }:
        raise ValidationError("provenance top-level fields are not closed")
    if value["schema_version"] != "1.0.0":
        raise ValidationError("unsupported provenance schema")
    distribution = value["distribution"]
    if distribution != {
        "name": "mathematical-academic-writing",
        "scope": "public_runtime",
        "version": "0.3.0",
    }:
        raise ValidationError("unexpected distribution identity")
    if value["excluded_material"] != EXPECTED_EXCLUDED_MATERIAL:
        raise ValidationError("unexpected excluded-material boundary")
    if value["private_validation_lineage"] != EXPECTED_PRIVATE_LINEAGE:
        raise ValidationError("unexpected private validation lineage")
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
        raise ValidationError("provenance does not bind the accepted v0.3.0 core")
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
            raise ValidationError(f"GitHub token-shaped value found in {relative}")


def main() -> int:
    try:
        files = snapshot_public_tree()
        provenance = load_provenance()
        aggregate = verify_core(provenance, files)
        scan_text_files(files)
    except (OSError, ValidationError) as exc:
        print(json.dumps({"error": str(exc), "status": "failed"}, sort_keys=True))
        return 1
    print(
        json.dumps(
            {
                "core_file_count": len(EXPECTED_CORE_PATHS),
                "core_sha256": aggregate,
                "public_file_count": len(files),
                "status": "passed",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
