#   # -------------------------------------------------------------------------------------- #
#   |  ░█▀▀░█░█░█▀█░█▀▀░▀█▀░▀█▀░█▀█░█▀█░█▀▀░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀░░░▀█▀░█▀▀░█▀▀░▀█▀░█▀▀  |
#   |  ░█▀▀░█░█░█░█░█░░░░█░░░█░░█░█░█░█░▀▀█░░░█░█░█░█░█░█░█░█░█░░░█▀▀░░░░█░░█▀▀░▀▀█░░█░░▀▀█  |
#   |  ░▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀  |
#   #--------------------------------------------------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * test_functions.py file for zcscommonlib. Makes sure that all functions work.     *
#   # -------------------------------------------------------------------------------- #

# Imports
from zcscommonlib import functions


# Test for the functions.month() function
def test_month():
    # Check that months 1 and 12 return "January" and "December".
    assert functions.month(1) == "January"
    assert functions.month(12) == "December"


# Test for the functions.palindrome() function
def test_palindrome():
    assert functions.palindrome("Racecar", True) == (True, 'racecaR')
    assert functions.palindrome("never a foot too far even", False) is True
    assert functions.palindrome("potato", True) == (False, 'otatop')
