import pytest

from base.id_scheme_type import IdSchemeType, detect_id_scheme_type


def test1():
    pass


@pytest.mark.parametrize(
    "id",
    [
        "valid-id-goes-here",
        "another-valid-id-goes-here",
    ],
)
def test2(id):
    pass


@pytest.mark.parametrize(
    "id",
    [
        "shortest-possible-id-goes-here",
        "another-valid-id-goes-here",
        "a-long-valid-id-goes-here",
    ],
)
def test3(id):
    pass


@pytest.mark.parametrize(
    "id",
    [
        "invalid-id-goes-here",  # explain why this value is invalid
        "another-invalid-id-goes-here",  # explain why this value is invalid
        "another-invalid-id-goes-here",  # explain why this value is invalid
    ],
)
def test4(id):
    pass


@pytest.mark.parametrize(
    "id",
    [
        "invalid-id-goes-here",  # explain why this value is invalid
        "another-invalid-id-goes-here",  # explain why this value is invalid
        "another-invalid-id-goes-here",  # explain why this value is invalid
        "another-invalid-id-goes-here",  # explain why this value is invalid
    ],
)
def test5(id):
    pass


@pytest.mark.parametrize(
    "id",
    [
        "invalid-id-goes-here-000-000-000-000",  # explain why this value is invalid
        "another-invalid-id-goes-here-000-000-000-000",  # explain why this value is invalid
        "another-invalid-id-goes-here-000-000-000-000",  # explain why this value is invalid
        "another-invalid-id-goes-here-000-000-000-000",  # explain why this value is invalid
    ],
)
def test6(id):
    pass
