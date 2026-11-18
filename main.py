"""Entry program for make.fun news-image-20261118 (Python 3.13, stdlib only).

The finished front page, entry.png, sits beside this file. The program
copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set) and
checks the copy byte-for-byte against the source. The image is a static
asset: no network access, and every run writes identical bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
MAX_BYTES = 1_048_576
MAGIC = (b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n")  # JPEG, PNG


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def check_image(path):
    """Gate checks the entry must pass: a whole JPEG or PNG, at most 1 MiB."""
    data = path.read_bytes()[:16]
    if not data.startswith(MAGIC):
        raise SystemExit(f"{path} is neither a JPEG nor a PNG")
    if path.stat().st_size > MAX_BYTES:
        raise SystemExit(f"{path} is over the 1 MiB limit")


def main():
    if not SOURCE.is_file():
        print(f"entry.png not found beside main.py: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    check_image(SOURCE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if sha256_of(SOURCE) != sha256_of(target):
        print("copied entry.png does not match the source", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"sha256 {sha256_of(target)})")


if __name__ == "__main__":
    main()
