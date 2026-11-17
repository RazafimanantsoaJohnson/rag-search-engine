import argparse
from .lib.semantic_search import *


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    args = parser.parse_args()

    match args.command:
        case "verify":
            verify_model()
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
