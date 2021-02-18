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
    metres = km * 1000
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
    # Function logic
    if 1 <= num <= 12:
        return str(months[num - 1])
    else:
        logging.error("Incorrect usage of months function in zcscommonlib. Please input a valid integer value between "
                      "1 and 12.")
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
            if typein == "str":
                userin = str(input(inputmsg))
            elif typein == "int":
                userin = int(input(inputmsg))
            elif typein == "float":
                userin = float(input(inputmsg))
            elif typein == "bool":
                userin = bool(input(inputmsg))
            else:
                logging.error("Incorrect usage of inputverify function in zcscommonlib. Please provide a valid input "
                              "type of 'int', 'float', 'str', or 'bool'.")
                exit(1)
        except ValueError:
            print(errormsg)
            continue
        break
    return userin
