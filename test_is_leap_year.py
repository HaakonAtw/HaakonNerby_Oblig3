from is_leap_year import is_leap_year
import pytest


@pytest.mark.parametrize("year, boolean",
                         [
                             (120, True),
                             (124, True),
                             (128, True),
                             (132, True),
                             (136, True),
                             (140, True),
                             (144, True)
                         ]
                         )
def test_year_divisible_by_four_but_not_hundred(year, boolean):
    assert is_leap_year(year) is boolean


@pytest.mark.parametrize("year, boolean",
                         [
                             (400, True),
                             (800, True),
                             (1200, True)
                         ]
                         )
def test_year_divisible_by_four_hundred(year, boolean):
    assert is_leap_year(year) is boolean


@pytest.mark.parametrize("year, boolean",
                         [
                             (5, False),
                             (6, False),
                             (7, False),
                             (9, False),
                             (15, False),
                             (34, False),
                             (338, False),
                             (1998, False)

                         ]
                         )
def test_year_not_divisible_by_four(year, boolean):
    assert is_leap_year(year) is boolean


@pytest.mark.parametrize("year, boolean",
                         [
                             (1700, False),
                             (1800, False),
                             (1900, False),
                             (2100, False)
                         ]
                         )
def test_year_divisible_by_hundred_but_not_four_hundred(year, boolean):
    assert is_leap_year(year) is boolean
