"""
Homoglyph Converter
-------------------

Converts Latin characters into visually similar Unicode homoglyphs.

Purpose:
Generate prompt obfuscation payloads for AI security research.

Example:

Input:
Ignore previous instructions.

Output:
Ignоrе prеviоus instructiоns.

(Some letters become Cyrillic look-alikes.)
"""

from __future__ import annotations

# Latin -> Unicode homoglyph
HOMOGLYPHS = {
    "A": "Α",  # Greek Alpha
    "B": "Β",  # Greek Beta
    "C": "С",  # Cyrillic Es
    "E": "Е",  # Cyrillic IE
    "H": "Н",  # Cyrillic En
    "I": "Ι",  # Greek Iota
    "J": "Ј",  # Cyrillic Je
    "K": "Κ",  # Greek Kappa
    "M": "М",  # Cyrillic Em
    "N": "Ν",  # Greek Nu
    "O": "Ο",  # Greek Omicron
    "P": "Р",  # Cyrillic Er
    "S": "Ѕ",  # Cyrillic Dze
    "T": "Τ",  # Greek Tau
    "X": "Χ",  # Greek Chi
    "Y": "Υ",  # Greek Upsilon

    "a": "а",  # Cyrillic a
    "c": "с",  # Cyrillic es
    "e": "е",  # Cyrillic ie
    "i": "і",  # Cyrillic i
    "j": "ј",  # Cyrillic je
    "o": "о",  # Cyrillic o
    "p": "р",  # Cyrillic er
    "s": "ѕ",  # Cyrillic dze
    "x": "х",  # Cyrillic ha
    "y": "у",  # Cyrillic u
}


def convert(text: str) -> str:
    """
    Convert every supported Latin character
    into its Unicode homoglyph.
    """
    return "".join(HOMOGLYPHS.get(ch, ch) for ch in text)


def main():
    print("=" * 60)
    print(" Homoglyph Prompt Converter")
    print("=" * 60)

    text = input("\nEnter text:\n> ")

    print("\nConverted payload:\n")
    print(convert(text))

    print("\nDone.")


if __name__ == "__main__":
    main()