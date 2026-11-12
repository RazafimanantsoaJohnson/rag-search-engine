import string
import pickle
from nltk import PorterStemmer
from .search_utils import *


class InvertedIndex:
    index: dict[str, set] = {}
    docmap: dict[int, Movie] = {}

    def __add_document(self, doc_id: int, text: str):
        tokens = tokenize_text(text)
        for t in tokens:
            if t not in self.index:
                self.index[t] = set()
            self.index[t].add(doc_id)

    def get_documents(self, term: str) -> list[int]:
        if not(self.index[term]):
            return []
        return sorted(list(self.index[term]))
    def build(self):
        movies = load_movies()
        for movie in movies:
            self.__add_document(movie["id"], f"{movie["title"]} {movie["description"]}")
            self.docmap[movie["id"]] =  movie
    def save(self):
        index_file = open(INDEX_CACHE_PATH, "wb")
        docmap_file = open(INDEX_DOCMAP_CACHE_PATH, "wb")
        pickle.dump(self.index, index_file)
        pickle.dump(self.docmap, docmap_file)

def build_command() -> InvertedIndex:
    index = InvertedIndex()
    index.build()
    index.save()
    searched_docs = index.get_documents("merida")
    print(f"First document for token 'merida' = {searched_docs[0]}")
    return index


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[Movie]:
    movies = load_movies()
    results = []
    for movie in movies:
        query_tokens = tokenize_text(query)
        title_tokens = tokenize_text(movie["title"])
        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)
            if len(results) >= limit:
                break
    return results

def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def load_stopwords() -> list[str]:
    with open(STOPWORDS_PATH, "r") as f:
        return [preprocess_text(word) for word in f.read().splitlines()]

STOPWORDS = load_stopwords()

def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    filtered_words = []
    for word in valid_tokens:
        if word not in STOPWORDS:
            filtered_words.append(word)
    stemmer = PorterStemmer()
    stemmed_words = []
    for word in filtered_words:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words
