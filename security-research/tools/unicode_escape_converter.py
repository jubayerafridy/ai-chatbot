"""
Unicode Escape Converter
------------------------

Converts text into \\uXXXX Unicode escape sequences.

Purpose:
Generate Unicode escape payloads for prompt injection research.

Example:

Input:
Ignore previous instructions.

Output:
\u0049\u0067\u006e\u006f\u0072\u0065\u0020\u0070...
"""


def unicode_escape(text: str) -> str:
    return "".join(f"\\u{ord(ch):04x}" for ch in text)


def main():
    print("=" * 60)
    print(" Unicode Escape Converter")
    print("=" * 60)

    text = input("\nEnter text:\n> ")

    print("\nConverted payload:\n")
    print(unicode_escape(text))

    print("\nDone.")


if __name__ == "__main__":
    main()