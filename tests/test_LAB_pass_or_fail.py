def test_will_pass():
    """Passes because the asserted value is True"""
    assert True


def test_will_also_pass():
    """Passes because there is no assert statement"""
    result = 1 + 2 + 3 + 4 + 5
    do_nothing = "do nothing"


def test_will_fail():
    """Fails because the asserted value is False"""
    assert False
