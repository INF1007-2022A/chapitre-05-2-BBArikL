#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    sous_total = sum([val[2]*val[1] for val in data])
    recu = f"{name}\n" \
           f"SOUS TOTAL     {sous_total:.2f} $" \
           f"\nTAXES           {sous_total*.15:.2f} $" \
           f"\nTOTAL          {sous_total*1.15:.2f} $"

    return recu


def format_number(number, num_decimal_digits):
    abs_n = int(abs(number))
    dig_groups = []
    while abs_n != 0:
        dig_groups.append(abs_n % 1000)
        abs_n //= 1000

    dig_groups.reverse()
    dig_groups[-1] = f"{dig_groups[-1] + (abs(number) - int(abs(number))):.{num_decimal_digits}f}"

    return f"{'-' if number < 0 else  ''}{' '.join(f'{dig}' for dig in dig_groups)}"


def get_triangle(num_rows):
    border = "+"
    inner = "A"
    haut_bas = border * (2 * num_rows + 1)
    res = haut_bas

    for i in range(1, num_rows+1):
        res += f"\n{border}"
        espace = " " * (num_rows - i)
        res += espace + inner*(2*i-1) + espace
        res += border
    return res + "\n" + haut_bas


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
