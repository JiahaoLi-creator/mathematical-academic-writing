#!/usr/bin/env python3
"""Verify the public runtime distribution and accepted eight-file core binding."""

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
    "references/mathematical_integrity.md",
    "references/anti_defensive_audit.md",
    "references/visual_companion.md",
    "references/corpus_manifest.md",
    "project_profiles/math3015.md",
)
EXPECTED_EXCLUDED_MATERIAL = [
    "source_pdfs",
    "extracted_or_normalized_corpus_text",
    "private_evidence_registry",
    "blind_regression_oracles",
    "source_derived_notebook_fixtures",
    "signing_keys_and_trust_configuration",
    "signed_private_release_metadata",
]
EXPECTED_PRIVATE_LINEAGE = {
    "harness_sha256": "c24d7e652e51f05f086f3078d633b9cece8953c7a432430008cd99ffc2815609",
    "manifest_sha256": "ce105d8b50806d6188655982c383c13104d4a02889a43d5d505cfebd251121b1",
    "note": (
        "Lineage anchors only; the private harness is not reproducible from this public "
        "repository."
    ),
    "payload_sha256": "ba1ee737ba2b82f4848631f178fef4a1c64dc6c194763b87182183b51d57c22a",
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
    "provenance/public-release.v1.json",
    "references/anti_defensive_audit.md",
    "references/corpus_manifest.md",
    "references/genre_profiles.md",
    "references/mathematical_integrity.md",
    "references/visual_companion.md",
    "scripts/verify_public_core.py",
    "tests/notebook_samples.json",
    "tests/regression_cases.json",
}
TEXT_NAMES = {".gitattributes", ".gitignore", "LICENSE"}
TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
TOKEN_PATTERN = re.compile(r"\bgh[opusr]_[A-Za-z0-9]{20,}\b")
ABSOLUTE_USER_PATH_PATTERN = re.compile(r"/Users/[A-Za-z0-9._-]+/")
PRIVATE_KEY_MARKER = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"


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
        "version": "0.2.0",
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
        if ABSOLUTE_USER_PATH_PATTERN.search(text):
            raise ValidationError(f"absolute user path found in {relative}")
        if PRIVATE_KEY_MARKER in text:
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
