from enum import Enum, auto
from typing import Optional


class Grade(Enum):
    A_PLUS = auto()
    A = auto()
    A_MINUS = auto()
    B_PLUS = auto()
    B = auto()
    B_MINUS = auto()
    C_PLUS = auto()
    C = auto()
    C_MINUS = auto()
    D_PLUS = auto()
    D = auto()
    D_MINUS = auto()
    F = auto()
    DNS = auto()
    DNC = auto()


def grade_to_point(grade: Grade, course_points: float = 1) -> float:
    point_mapping = {
        Grade.A_PLUS: 9,
        Grade.A: 8,
        Grade.A_MINUS: 7,
        Grade.B_PLUS: 6,
        Grade.B: 5,
        Grade.B_MINUS: 4,
        Grade.C_PLUS: 3,
        Grade.C: 2,
        Grade.C_MINUS: 1,
    }
    return point_mapping.get(grade, 0) * course_points


def grade_string_to_grade(input: str) -> Optional[Grade]:
    cleaned_input = input.strip().upper()
    mapping = {
        "A+": Grade.A_PLUS,
        "A": Grade.A,
        "A-": Grade.A_MINUS,
        "B+": Grade.B_PLUS,
        "B": Grade.B,
        "B-": Grade.B_MINUS,
        "C+": Grade.C_PLUS,
        "C": Grade.C,
        "C-": Grade.C_MINUS,
        "D+": Grade.D_PLUS,
        "D": Grade.D,
        "D-": Grade.D_MINUS,
        "F": Grade.F,
        "DNS": Grade.DNS,
    }

    return mapping.get(cleaned_input, None)


def grade_string_to_point(input: str) -> int:
    as_grade = grade_string_to_grade(input)

    if as_grade is None:
        return -1

    return grade_to_point(as_grade)
