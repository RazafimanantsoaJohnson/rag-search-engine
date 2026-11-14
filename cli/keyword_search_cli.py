import argparse
import json
from lib.keyword_search import *
from lib.search_utils import *

def main() -> None:
    parser = argparse.ArgumentParser(description = "Keyword Search CLI")
    subparsers = parser.add_subparsers(dest= "command", help= "Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")
    subparsers.add_parser("build", help="Search movies using keywords")
    tf_parser = subparsers.add_parser("tf", help="Get the term frequency of a term in a document")
    tf_parser.add_argument("doc_id", type=int, help="id of a document")
    tf_parser.add_argument("term", type=str, help="the term to get the frequency for")
    idf_parser = subparsers.add_parser("idf", help="Get the inverted document frequency score of a term")
    idf_parser.add_argument("term", type=str, help="")

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
        case "build":
            build_command()
            pass
        case "tf":
            term = tokenize_single_term(args.term)
            index = InvertedIndex()
            index.load()
            result= index.get_tf(args.doc_id, term)
            print(result)
            pass
        case "idf":
            idf_command(args.term)
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()