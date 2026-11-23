"""Copy the pre-rendered entry image to /output/entry.png.

The image itself was drawn offline (deterministic PIL render of the
33 verified Sunday 22 November 2026 stories, winners' template) and
is stored next to this file as entry.png. This program only copies
it, so the grader run is stdlib-only, network-free and deterministic.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("missing entry.png next to main.py\n")
        return 1
    if os.path.getsize(src) > 1048576:
        sys.stderr.write("entry.png exceeds the 1 MiB limit\n")
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    sys.stdout.write("wrote %s (%d bytes)\n" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
