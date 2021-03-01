#   # -------------------------------------------- #
#   |  ░█▄█░█▀█░▀█▀░█░█░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀  |
#   |  ░█░█░█▀█░░█░░█▀█░░░█░█░█░█░█░█░█░█░█░░░█▀▀  |
#   |  ░▀░▀░▀░▀░░▀░░▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀  |
#   #--------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/Functions-Module
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * This module contains utilities related to mathematic calculations.               *
#   # -------------------------------------------------------------------------------- #

def great_circle(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the
    earth (decimal degrees), returns the distance in
    meters.
    All arguments must be of equal length.
    :param lon1: longitude of first point
    :param lat1: latitude of first point
    :param lon2: longitude of second point
    :param lat2: latitude of second point
    :return: distance in meters between the two sets of co-ords
    """
    # Imports
    import math
    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    km = 6378.8 * (math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 -
                                                                                                          lon1)))
    # Convert kilometres to metres
    metres = km * 1000
    # Return the distance in metres
    return metres
