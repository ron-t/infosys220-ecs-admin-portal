from base.LAB_grades import grade_string_to_point
import pytest


@pytest.mark.xfail(reason="This test fails on purpose to show how the xfail mark works")
def test_xfail_example():
    """Demonstration of the pytest xfail mark feature"""
    assert False
