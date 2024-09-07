from enum import StrEnum
import re

_LEGACY_SCHEME_RE = re.compile(r"id[1-9][0-9]{6,7}")
_INTERNAL_SCHEME_RE = re.compile(r"[0-9][0-9][0-9](-[0-9][0-9][0-9]){3}")
_EXTERNAL_SCHEME_RE = re.compile(r"([a-z](-(?!-))?)+(-[0-9][0-9][0-9]){4}")


class IdSchemeType(StrEnum):
    INTERNAL = "internal"
    INTERNAL_LEGACY = "legacy"
    EXTERNAL = "external"
    INVALID = "invalid"


def detect_id_scheme_type(id: str) -> IdSchemeType:
    if _LEGACY_SCHEME_RE.fullmatch(id):
        return IdSchemeType.INTERNAL_LEGACY

    if _INTERNAL_SCHEME_RE.fullmatch(id):
        return IdSchemeType.INTERNAL

    if _EXTERNAL_SCHEME_RE.fullmatch(id):
        return IdSchemeType.EXTERNAL

    return IdSchemeType.INVALID
