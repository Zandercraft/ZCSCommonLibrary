#   # ------------------------------------------------------------------ #
#   |  ░█▄█░█▀█░▀█▀░█░█░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀░░░▀█▀░█▀▀░█▀▀░▀█▀░█▀▀  |
#   |  ░█░█░█▀█░░█░░█▀█░░░█░█░█░█░█░█░█░█░█░░░█▀▀░░░░█░░█▀▀░▀▀█░░█░░▀▀█  |
#   |  ░▀░▀░▀░▀░░▀░░▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀  |
#   #------------------------------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * test_zcsmath.py file for zcscommonlib. Makes sure that all math functions work.  *
#   # -------------------------------------------------------------------------------- #

# Imports
from zcscommonlib import zcsmath


# Test for the functions.great_circle() function
def test_great_circle():
    # Check if the distance between the specific coordinates match the answer which is already known.
    assert zcsmath.great_circle(52.370216, 4.895168, 52.520008, 13.404954) == 947546.2822650459
