from base.LAB_grades import Grade, grade_string_to_grade, grade_string_to_point, grade_to_point
import pytest


@pytest.mark.parametrize(
    "input_string",
    [
        "D+",
        "D",
        "D-",
    ],
)
def test_grade_to_string_d_grades(input_string):
    """grade_string_to_point is correct for all D grades"""
    output = grade_string_to_point(input_string)
    expected = 0

    assert output == expected


@pytest.mark.parametrize(
    ("input_string", "expected_output"),
    [
        ("a+", 9),
        ("a", 8),
    ],
)
def test_grade_to_string_lower_case(input_string, expected_output):
    """update this test description"""
    output = grade_string_to_point(input_string)

    assert output == expected_output
