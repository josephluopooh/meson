#!/usr/bin/env python3

from pathlib import Path
import sys


def main() -> None:
    private = Path(sys.argv[1])
    headers = (private / 'dataonly-headers.pc').read_text(encoding='utf-8')
    plain = (private / 'dataonly-plain.pc').read_text(encoding='utf-8')

    assert 'prefix=' in headers
    assert 'includedir=' in headers
    assert 'libdir=' not in headers
    assert 'Cflags: -I${includedir}/dataonly-headers -DDATAONLY_HEADERS=1' in headers

    assert 'prefix=' not in plain
    assert 'includedir=' not in plain
    assert 'Cflags:' not in plain


if __name__ == '__main__':
    main()
