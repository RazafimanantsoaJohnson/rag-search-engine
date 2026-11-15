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
    tfidf_parser = subparsers.add_parser("tfidf", help="Get the tf-idf score of a term in a document")
    tfidf_parser.add_argument("doc_id", type=int, help="id of a document")
    tfidf_parser.add_argument("term", type=str, help="the term to get the score for")
    bm25_idf_parser = subparsers.add_parser("bm25idf", help="Get BM25 IDF score for a given term")
    bm25_idf_parser.add_argument("term", type=str, help="Term to get BM25 IDF score for")

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
            result = tf_command(args.doc_id, args.term)
            print(f"Inverse document frequency of '{args.term}': {result:.2f}")
            pass
        case "idf":
            idf_command(args.term)
            pass
        case "tfidf":
            result = tfidf_command(args.doc_id, args.term)
            print(f"Inverse document frequency of '{args.term}': {result:.2f}")
            pass
        case "bm25idf":
            result = bm25_idf_command(args.term)
            print(f"BM25 IDF score of '{args.term}': {result:.2f}")
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()