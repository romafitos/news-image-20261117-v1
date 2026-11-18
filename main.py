#!/usr/bin/env python3
"""Publish the bundled front-page image for make.fun bounty news-image-20261117.

The entry is a single pre-rendered image (entry.png): a front page titled
THE WORLD IN ONE DAY that sums up the world news of Tuesday 17 November
2026 in 33 stories across six continents, led by the Kerch Bridge strike.

This program does one small, verifiable job: it copies the bundled image
into the output directory and proves the copy is byte-for-byte identical
by comparing SHA-256 hashes. Standard library only.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
MAX_IMAGE_BYTES = 1 * 1024 * 1024  # 1 MiB


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = Path(__file__).resolve().parent / IMAGE_NAME
    if not source.is_file():
        print(
            f"error: bundled image '{IMAGE_NAME}' is missing next to main.py "
            f"(looked for {source}) — cannot produce the entry",
            file=sys.stderr,
        )
        return 1

    size = source.stat().st_size
    if size > MAX_IMAGE_BYTES:
        print(
            f"error: bundled image is {size} bytes, over the "
            f"{MAX_IMAGE_BYTES} byte limit",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / IMAGE_NAME

    shutil.copyfile(source, destination)

    source_hash = sha256_of(source)
    destination_hash = sha256_of(destination)
    if source_hash != destination_hash:
        print(
            "error: hash mismatch after copy "
            f"(source {source_hash[:16]}..., output {destination_hash[:16]}...)",
            file=sys.stderr,
        )
        return 1

    print(f"output: {destination}")
    print(f"size: {destination.stat().st_size} bytes")
    print(f"sha256: {destination_hash[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
