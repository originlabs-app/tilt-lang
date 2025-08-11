import argparse

from .parser import parse_program


def main() -> None:
    parser = argparse.ArgumentParser(description="TILT CLI")
    parser.add_argument("file", help="TILT source file")
    args = parser.parse_args()
    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()
    program = parse_program(source)
    print(program)


if __name__ == "__main__":
    main()
