## ⚡️ Short Description

**IEEE 754 Floating-Point Binary Converter**

A Python utility that converts any floating-point number (decimal) into its **IEEE 754 Single-Precision (32-bit)** or **Double-Precision (64-bit)** binary representation. The tool clearly visualizes the three components: **Sign Bit**, **Biased Exponent**, and **Mantissa (Fraction)**, providing a direct educational tool for computer science students and anyone interested in floating-point arithmetic.

-----

# 💻 IEEE 754 Floating-Point Binary Converter

## ✨ Overview

The **IEEE 754 Floating-Point Binary Converter** is a command-line utility written in Python designed to demonstrate how a standard floating-point number is represented in memory according to the **IEEE 754 standard**.

It supports both **Single-Precision (32-bit)** and **Double-Precision (64-bit)** formats, taking a user-provided decimal number and breaking it down into its three key binary components: the **Sign Bit**, the **Biased Exponent**, and the **Mantissa (Fraction)**. This tool is ideal for educational purposes, helping to demystify how computers store and process non-integer numbers.

## 🚀 Features

  * **Dual Precision Support:** Choose between 32-bit (Single-Precision) or 64-bit (Double-Precision) conversion.
  * **Detailed Visualization:** Clearly displays the Sign Bit, Biased Exponent, and Mantissa with the correct bit lengths.
  * **Full Binary Representation:** Shows the complete 32-bit or 64-bit binary sequence, segmented for easy field identification.
  * **Core Conversion Logic:** Includes custom implementations for separating integer/fractional parts, converting to binary (integer and fractional), and performing the crucial normalization step.

## 🛠 Installation and Setup

This project uses only **standard Python libraries** and does not require any external packages.

1.  **Clone the repository (or save the code):**
    ```bash
    git clone https://github.com/Ade20boss/FloatViz
    cd FloatViz
    ```

2.  **Run the script:**
    ```bash
    python FloatViz.py
    ```

## 💡 Usage

When you run the script, you will be prompted to select the bit length and then enter a floating-point number:

```
WELCOME TO IEE FLOATING POINT CONVERTER
64 BITS
32 BITS
Enter bit length: 32
Enter a number: -10.75
```

The output will then provide a clear, step-by-step breakdown of the number's binary representation:

```
Sign bit:  1  (0=positive, 1=negative)
Exponent (biased) 8 bit:  10000010
    |---|---|---|---|
Mantissa (23 bits):  01011000000000000000000
    |---|---|---|---|---|---|
Full 32-bit binary:
[1] [10000010] [01011000000000000000000]
```

## ⚙️ Key Functions

| Function | Description |
| :--- | :--- |
| `visualize_float()` | **Main function** that handles user input, orchestrates the conversion process, and prints the final visualized output. |
| `get_numbers(number2)` | Separates a floating-point number into its **integer part (int)** and **fractional part (float)**. |
| `integer_to_binary(n)` | Converts a non-negative integer to its **unprefixed binary string** representation using repeated division by 2. |
| `fractional_to_binary(fractional_part, bit_length)` | Converts the fractional part to a binary string by repeated multiplication by 2, limited by the chosen precision (23 or 52 bits). |
| `full_conversion(number3, bit)` | Combines the integer and fractional binary parts into a single string (e.g., `"101.11"`). |
| `normalized_conversion(number4, bit)` | **Crucial function** that performs the **IEEE 754 normalization**. It shifts the decimal point to the `1.xxx` format, calculates the raw exponent, applies the appropriate **bias** (127 for 32-bit, 1023 for 64-bit), and extracts/pads the final **Mantissa** and **Biased Exponent**. |

## 📐 IEEE 754 Format Summary

| Field | 32-bit (Single) Length | 64-bit (Double) Length | Description |
| :--- | :--- | :--- | :--- |
| **Sign Bit** | 1 bit | 1 bit | `0` for Positive, `1` for Negative. |
| **Exponent** | 8 bits | 11 bits | Stores the magnitude of the number's power of 2, after adding a **bias** (127 or 1023). |
| **Mantissa** | 23 bits | 52 bits | Stores the fractional part of the normalized binary number (the hidden `1.` is implied). |

## 🤝 Contributing

Feel free to fork the repository and contribute. Any enhancements, bug fixes, or new features (like handling special cases like $\pm \infty$ or NaN) are welcome\!
