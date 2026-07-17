"""
ROT13 Converter
---------------

Generates ROT13 payloads for prompt injection research.
"""

import codecs


def convert(text: str) -> str:
    return codecs.encode(text, "rot_13")


def main():
    print("=" * 60)
    print(" ROT13 Converter")
    print("=" * 60)

    text = input("\nEnter text:\n> ")

    print("\nConverted payload:\n")
    print(convert(text))

    print("\nDone.")


if __name__ == "__main__":
    main()