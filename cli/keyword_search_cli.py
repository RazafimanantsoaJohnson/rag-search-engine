import argparse
import json
from lib.keyword_search import *
from lib.search_utils import *

def main() -> None:
    parser = argparse.ArgumentParser(description = "Keyword Search CLI")
    subparsers = parser.add_subparsers(dest= "command", help= "Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = search_command(args.query)
            for i, res in enumerate(results, 1):
                print(f"{i}. {res['title']}")
            # movies_data = load_movies_data()
            # print(keyword_search(movies_data["movies"], args.query))
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()