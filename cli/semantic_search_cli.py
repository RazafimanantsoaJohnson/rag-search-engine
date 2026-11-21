import argparse
from lib.semantic_search import *


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    subparsers = parser.add_subparsers(dest= "command", help= "Available commands")

    subparsers.add_parser("verify", help="verify the model used in our semantic search")
    embed_subparser = subparsers.add_parser("embed-text", help="generate the embedding of a specific word")
    embed_subparser.add_argument("text", help="the text to embed")
    args = parser.parse_args()
    

    match args.command:
        case "verify":
            verify_model()
            pass
        case "embed-text":
            embed_text(args.text)
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
