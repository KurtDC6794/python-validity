"""Signed init blobs for 06cb:0081 (Lenovo Yoga 730-13IKB).

The 0081 is a 06cb device but takes the 138a:0090 blob set: it accepts the 090
init_hardcoded (0x0000) and rejects the 9a one (0x04be).
"""

from .blobs_90 import (  # noqa: F401
    init_hardcoded,
    init_hardcoded_clean_slate,
    reset_blob,
    db_write_enable,
)
