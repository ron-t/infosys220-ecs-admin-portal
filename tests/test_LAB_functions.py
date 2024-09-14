from base.LAB_grades import Grade, grade_string_to_grade, grade_string_to_point, grade_to_point


def test_grade_to_string_a_plus():
    """grade_string_to_point is correct for A+"""
    input_string = "A+"
    output = grade_string_to_point(input_string)
    expected = 9

    assert output == expected


def test_grade_to_string_a():
    """grade_string_to_point is correct for A"""
    input_string = "A"
    output = grade_string_to_point(input_string)
    expected = 8

    assert output == expected


def test_grade_to_string_a_minus():
    pass


def test_grade_to_string_b_plus():
    pass


def test_grade_to_string_b():
    pass


def test_grade_to_string_b_minus():
    pass


def test_grade_to_string_c_plus():
    pass


def test_grade_to_string_c():
    pass


def test_grade_to_string_c_minus():
    pass
