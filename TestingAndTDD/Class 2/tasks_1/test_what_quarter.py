# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs
# as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part
# of the second quarter; and month 11 (November), is part of the fourth quarter.
#
# Constraint:
#
# 1 <= month <= 12
# Should Satisfy this test:

import what_quarter


def test_what_quarter():
    assert what_quarter.what_quarter(3) == 1
    assert what_quarter.what_quarter(8) == 3
    assert what_quarter.what_quarter(11) == 4
    
