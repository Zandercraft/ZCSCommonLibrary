#   # ---------------------------------------------------------------- #
#   |  ░█▀▀░█░█░█▀█░█▀▀░▀█▀░▀█▀░█▀█░█▀█░█▀▀░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀  |
#   |  ░█▀▀░█░█░█░█░█░░░░█░░░█░░█░█░█░█░▀▀█░░░█░█░█░█░█░█░█░█░█░░░█▀▀  |
#   |  ░▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀  |
#   #----------------------------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/Functions-Module
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * General utils. Currently the only module, more may be added later.               *
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


def month(num: int) -> str:
    """
    Returns the name of a month (as a string type) from an integer input.
    :param num: the number (1-12) of the month wanted
    :return: the name of the month based on the number
    """
    # Imports
    import logging
    # Constants
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]
    # Check if number given is between 1 and 12
    if 1 <= num <= 12:
        # Return the name corresponding with that number (minus 1, as Python starts at 0)
        return str(months[num - 1])
    # The number is not between 1 and 12
    else:
        # Log error
        logging.error("Incorrect usage of months function in zcscommonlib. Please input a valid integer value between "
                      "1 and 12.")
        # Exit with non-zero error code
        exit(1)


def inputverify(typein: str, inputmsg: str, errormsg: str):
    """
    Gets the input from a user, persisting until the input of the right type is received with an optional input
    message and error message.
    :param typein: type of input to require of the user
    :param inputmsg: message to display to the user when getting input
    :param errormsg: message to display when an input of the wrong type is given
    :return: input provided from the user in the desired format
    """
    # Imports
    import logging
    # Function logic
    while True:
        try:
            # Grab user's input and try to convert it to the format provided.
            if typein == "str":
                userin = str(input(inputmsg))
            elif typein == "int":
                userin = int(input(inputmsg))
            elif typein == "float":
                userin = float(input(inputmsg))
            elif typein == "bool":
                userin = bool(input(inputmsg))
            # The developer used an improper format
            else:
                # Log error
                logging.error("Incorrect usage of inputverify function in zcscommonlib. Please provide a valid input "
                              "type of 'int', 'float', 'str', or 'bool'.")
                # Exit with non-zero exit code
                exit(1)
        except ValueError:
            # The user did not give an input in the requested format, log provided error message
            print(errormsg)
            # Get the user's input again
            continue
        # Proper input was obtained from the user, leave loop
        break
    # Return the input from the user in the requested format
    return userin
