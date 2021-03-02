#   # ---------------------------------------------------------------- #
#   |  ░█▀▀░█░█░█▀█░█▀▀░▀█▀░▀█▀░█▀█░█▀█░█▀▀░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀  |
#   |  ░█▀▀░█░█░█░█░█░░░░█░░░█░░█░█░█░█░▀▀█░░░█░█░█░█░█░█░█░█░█░░░█▀▀  |
#   |  ░▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀  |
#   #----------------------------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/Functions-Module
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * General utilities.                                                               *
#   # -------------------------------------------------------------------------------- #

def month(num: int) -> str:
    """
    Returns the name of a month (as a string type) from an integer input.

    :param num: the number (1-12) of the month wanted
    :return: the name of the month as a string based on the number provided
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


def typedinput(typein: str, inputmsg: str, errormsg: str):
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
            # Grab user's input and try to convert it to the format provided
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


def palindrome(inputstr: str, isword: bool) -> [bool, str]:
    """
    Takes an input, in the form of a string, and checks if it is a palindrome.

    :param inputstr: an input to check in the form of a string
    :param isword: is the value a single word
    :return: (bool - is palindrome, str - reversed word if single word)
    """
    # Remove all spaces from the input string
    formattedstr = inputstr.replace(" ", "")
    # Check if the string in reverse is the same as the normal string
    if formattedstr[::-1].lower() == formattedstr.lower():
        if isword:
            return True, formattedstr[::-1]  # TODO: Make compatible with sentences in future release.
        else:
            return True
    # Return false if the string is not a palindrome.
    else:
        if isword:
            return False, formattedstr[::-1]  # TODO: Make compatible with sentences in future release.
        else:
            return False


def palindromes(inputstr: str) -> (int, [str]):
    """
    Takes an input, in the form of a string, and checks how many palindromes are in it. Also returns an array of those
    palindromes.

    :param inputstr: an input to check in the form of a string
    :return: (int - number of palindromes, [str, str2...] - palindromes)
    """
    words = str.split(inputstr)  # Split the input into an array of the words in it
    palindrome_array = []
    # Cycle through all words provided
    for i in words:
        if i[::-1].lower() == i.lower():
            palindrome_array.append(i)  # Add palindromes to the array
    return len(palindrome_array), palindrome_array
