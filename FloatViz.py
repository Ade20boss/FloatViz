def get_numbers(number2):
    # Function definition: starts the definition of the function 'get_numbers' which takes one argument 'number2'.
    """
    # Start of the docstring: provides a summary of the function's purpose.
    Calculate and return the integer and fractional parts of a floating-point number.

    This function takes a floating-point number as input, separates its integer part
    and fractional part, and returns them as a tuple.

    :param number2: The floating-point number to process.
    :type number2: float
    :return: A tuple containing the integer part and the fractional part of the input
             number. The first element is the integer part (int) and the second
             element is the fractional part (float).
    :rtype: tuple(int, float)
    """
    # Assigns the integer part of 'number2' to 'integer_part' by casting 'number2' to an integer (which truncates the fractional part).
    integer_part = int(number2)
    # Calculates the fractional part by subtracting the integer part from the original floating-point number.
    fractional_part = number2 - integer_part
    # Creates a tuple 'numbers' containing the separated integer and fractional parts.
    numbers = (integer_part, fractional_part)
    # Returns the tuple 'numbers' containing both parts.
    return numbers


def choice():
    print("64 BITS")
    print("32 BITS")

def choice2():
    bit_length = int(input("Enter bit length: "))
    return bit_length



def integer_to_binary(n):
    # Function definition: starts the definition of the function 'integer_to_binary' which takes one integer argument 'n'.
    """
    # Start of the docstring.
    Convert an integer to its binary representation as a string.

    This function accepts a non-negative integer and converts it to its
    corresponding binary representation without using built-in conversion
    methods. The binary result excludes any prefixes such as '0b'.

    :param n: The integer number to be converted into binary.
    :type n: int
    :return: The binary representation of the input integer as a string.
    :rtype: str
    """
    # Checks if the input integer 'n' is 0.
    if n == 0:
        # If 'n' is 0, its binary representation is simply "0".
        return "0"
    # Initializes an empty list 'bits' to store the binary digits (bits).
    bits = []
    # Starts a 'while' loop that continues as long as the number 'n' is greater than 0.
    while n > 0:
        # Calculates the remainder when 'n' is divided by 2 (n % 2), which is the next binary digit (0 or 1).
        # Converts the result to a string and appends it to the 'bits' list.
        bits.append(str(n % 2))
        # Updates 'n' by performing floor division by 2 (n //= 2), effectively shifting to the next bit.
        n //= 2
    # Joins the elements of the 'bits' list into a single string.
    # The list is reversed (bits[::-1]) because the bits were collected in reverse order (least significant bit first).
    return "".join(bits[::-1])


def fractional_to_binary(fractional_part, bit_length):
    """
    Converts a given fractional part of a number to its binary representation, up to a specified
    maximum number of binary digits determined by the bit length (either 32-bit or 64-bit).
    This method handles both terminating and non-terminating binary fractions by limiting the
    output length to correspond to the given bit length.

    :param fractional_part: The fractional part of the number to be converted to binary.
    :type fractional_part: float
    :param bit_length: The bit length of the representation (32 for single-precision, 64 for double-precision).
    :type bit_length: int
    :return: Binary representation of the fractional part as a string.
    :rtype: str
    """
    binary = []
    limit = 52 if bit_length == 64 else 23

    # Starts an infinite loop for the conversion process.
    while True:
        # Multiplies the current 'fractional_part' by 2.
        # Takes the integer part of the result (int(...)), which is the next binary digit (0 or 1).
        number = int(fractional_part * 2)
        # Calculates the new fractional part by taking the result of (fractional_part * 2) and subtracting the extracted integer (binary digit).
        new_fractional = (fractional_part * 2) - number
        # Appends the extracted binary digit ('number') to the 'binary' list.
        binary.append(number)
        # Updates 'fractional_part' to the 'new_fractional' for the next iteration.
        fractional_part = new_fractional
        # Checks if the new fractional part is exactly 0, meaning the conversion is complete.
        if new_fractional == 0:
            # If conversion is complete, exit the loop.
            break
        # Checks if the maximum number of bits ('limit') has been reached.
        elif len(binary) >= limit:
            # If the limit is reached (to prevent infinite loops for non-terminating binary fractions), exit the loop.
            break
    # Converts all the integer elements (binary digits) in the 'binary' list to strings.
    binary = list(map(str, binary))
    # Joins the string binary digits into a single string and returns it.
    return "".join(binary)


def full_conversion(number3, bit):
    """
    Converts a floating-point number to its binary representation including both
    integer and fractional parts. The conversion is precise up to a specified
    number of bits for the fractional part.

    :param number3: The floating-point number to be converted.
    :type number3: float
    :param bit: The number of bits to use for the fractional part in the binary
        representation.
    :type bit: int
    :return: A string representing the binary equivalent of the input floating-point
        number, including both the integer and fractional parts, separated by a
        decimal point.
    :rtype: str
    """
    # Calls 'get_numbers' to separate 'number3' into its integer and fractional parts using tuple unpacking.
    integer_part, fractional_part = get_numbers(number3)
    # Calls 'integer_to_binary' to convert the integer part to a binary string.
    binary_integer_part = integer_to_binary(integer_part)
    # Calls 'fractional_to_binary' to convert the fractional part to a binary string.
    binary_fractional_part = fractional_to_binary(fractional_part, bit)
    # Combines the two binary strings with a decimal point ('.') in between and returns the result.
    return binary_integer_part + "." + binary_fractional_part



def normalized_conversion(number4, bit):
    # Function definition: starts the definition of 'normalized_conversion' for IEEE 754 format preparation.
    """
    # Start of the docstring.
    Transforms a given number into its normalized binary representation compatible with the IEEE 754 standard.
    The function converts the number into binary, adjusts the format to ensure a valid normalized form,
    computes its exponent, and finally constructs the mantissa and exponent. The resulting values are formatted
    to maintain compliance with floating-point standards.

    :param number4: The number input provided for conversion into normalized binary format.
    :type number4: str
    :return: A list containing the mantissa as the first element and the exponent as the second element.
    :rtype: List[str]
    """
    # Calls 'full_conversion' to get the full binary representation of 'number4' (e.g., "101.11").
    number4 = full_conversion(number4, bit)
    # Converts the binary string into a list of individual characters (digits and the decimal point).
    number4 = [i for i in number4]
    # Initializes the raw exponent value to 0.
    exponent = 0
    # Checks if the first digit of the full binary representation is '1' (meaning the number is >= 1).
    if number4[0] == "1":
        # Calculates the raw exponent: position of the decimal point (number4.index(".")) minus 1.
        # This is the number of places the point must move to the right of the first '1'.
        exponent = number4.index(".") - 1
        # Removes the original decimal point.
        number4.remove(".")
        # Inserts the decimal point after the first digit ('1'), normalizing the number (e.g., 1.0111).
        number4.insert(1, ".")
    # Checks if the first digit is '0' (meaning the number is between 0 and 1, like 0.00101).
    elif number4[0] == "0":
        # Finds the index of the *first* '1' in the entire binary string (e.g., 0.00101 -> index of '1' is 3).
        first_1 = number4.index("1")
        # Calculates the raw exponent: The negation of the index of the first '1', plus 1.
        # This gives the number of places the point must move to the *right* to land after the first '1'.
        exponent = first_1 * -1 + 1
        # Slices the list to remove the leading '0.' and all leading zeros up to the first '1' (e.g., from '0.00101' to '101').
        number4 = number4[first_1:]
        # Finds the index of the first '1' in the *new*, shortened list (which will be 0).
        new_first_1 = number4.index("1")
        # Inserts the decimal point immediately after the first '1' (at index 1) to normalize it (e.g., '1.01').
        number4.insert(new_first_1 + 1, ".")
    # Checks if the last element is a decimal point (e.g., '1.' which happens if the number was a whole integer).
    if number4[-1] == ".":
        # Appends a '0' to make it '1.0' for proper formatting.
        number4.append("0")
    # Bias the exponent by adding 127/ (for IEEE 754 single-precision).
    if bit == 64:
        exponent = exponent + 1023
    else:
        exponent = exponent + 127

    # Converts the biased exponent (an integer) into its 8-bit binary string representation.
    exponent = integer_to_binary(exponent)
    # Pads the binary exponent string with leading zeros to ensure it is exactly 8/11 bits long.
    if bit == 32:
        exponent = exponent.rjust(8, "0")
    else:
        exponent = exponent.rjust(11, "0")
    # Joins the list of characters back into the normalized binary string (e.g., "1.0111").
    binary = "".join(number4)
    # Extracts the mantissa: the part of the binary string *after* the '1.' (starts at index 2).
    mantissa = binary[2:]
    print(mantissa)
    # Pads the mantissa with trailing zeros to ensure it is exactly 23 bits long (IEEE 754 requirement).
    if bit == 32:
        mantissa = mantissa.ljust(23, "0")
    else:
        mantissa = mantissa.ljust(52, "0")
    # Creates a list containing the final mantissa and the biased exponent binary string.
    details = [mantissa, exponent]
    # Returns the list of mantissa and exponent strings.
    return details


def visualize_float():
    # Function definition: starts the definition of 'visualize_float', the main function for user interaction and visualization.
    """
    # Start of the docstring.
    Convert and visualize a floating-point number as a binary representation.

    This function prompts the user to input a floating-point number, converts it to
    its binary representation using IEEE 754 single-precision floating-point format,
    and visualizes its three main components: sign bit, exponent (biased), and mantissa
    (fractional part). Additionally, the function displays the complete 32-bit floating-
    point binary representation in segments.

    :raises ValueError: If the entered input cannot be converted into a float.
    :return: None
    """
    # Comment indicating the expected variables (though they are calculated below).
    # Assume you already have:
    # sign_bit, exponent_bin (8-bit), mantissa_bin (23-bit)
    # Prompts the user for input and stores it as a string.
    print("WELCOME TO IEE FLOATING POINT CONVERTER")
    choice()
    bit_ = choice2()
    number5 = input("Enter a number: ")
    # Converts the user input string to a floating-point number. This line may raise a ValueError.
    number5 = float(number5)
    # Determines the sign bit: 1 if 'number5' is negative, 0 if it's positive or zero (Ternary operator).
    sign_bit = 1 if number5 < 0 else 0
    # Takes the absolute value of the number, as the sign is already captured by 'sign_bit'.
    number5 = abs(number5)
    # Calls 'normalized_conversion' on the absolute value to get the mantissa and exponent strings.
    number_mantissa, number_exponent = normalized_conversion(number5, bit_)
    # Prints the collected components (sign, exponent, mantissa) in their final order for verification.
    print(str(sign_bit), number_exponent, number_mantissa)
    # Prints a descriptive heading for the sign bit.
    # Step 1: Show sign
    # Prints the sign bit value and its interpretation.
    print("Sign bit: ", sign_bit, " (0=positive, 1=negative)")

    # Prints a descriptive heading for the exponent.
    # Step 2: Show exponent
    # Prints the 8-bit biased exponent.
    # Prints a visual separator for the exponent field, using '|' every 4 characters.
    if bit_ == 32:
        print("Exponent (biased) 8 bit: ", number_exponent)
        print("  ", "".join(['|' if i % 4 == 0 else '-' for i in range(8)]))
    else:
        print("Exponent (biased) 11 bit: ", number_exponent)
        print("  ", "".join(['|' if i % 4 == 0 else '-' for i in range(11)]))

    # Prints a descriptive heading for the mantissa.
    # Step 3: Show mantissa
    # Prints the 23-bit mantissa.
    # Prints a visual separator for the mantissa field, using '|' every 4 characters.
    if bit_ == 32:
        print("Mantissa (23 bits): ", number_mantissa)
        print("  ", "".join(['|' if i % 4 == 0 else '-' for i in range(23)]))
    else:
        print("Mantissa (52 bits): ", number_mantissa)
        print("  ", "".join(['|' if i % 4 == 0 else '-' for i in range(52)]))

    # Prints a descriptive heading for the full 32-bit representation.
    # Step 4: Full 32-bit
    # Constructs the full 32-bit binary string by concatenating the components.
    full_binary = f"{sign_bit}{number_exponent}{number_mantissa}"
    # Prints the full binary string label.
    if bit_ == 32:
        print("Full 32-bit binary:")
        # Prints a label to clarify the segmented display format.
        # Split into fields for clarity
        # Prints the full binary string, segmented by its fields: [Sign] [Exponent] [Mantissa].
        print(f"[{full_binary[0]}] [{full_binary[1:9]}] [{full_binary[9:]}]")
    else:
        print("Full 64-bit binary:")
        # Prints a label to clarify the segmented display format.
        # Split into fields for clarity
        # Prints the full binary string, segmented by its fields: [Sign] [Exponent] [Mantissa].
        print(f"[{full_binary[0]}] [{full_binary[1:12]}] [{full_binary[12:]}]")


# Executes the main visualization function when the script is run.
visualize_float()