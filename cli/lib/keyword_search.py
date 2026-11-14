import string
import pickle
import math
from collections import Counter
from nltk import PorterStemmer
from .search_utils import *


class InvertedIndex:
    index: dict[str, set] = {}
    docmap: dict[int, Movie] = {}
    term_frequency: dict[int, Counter] = {}

    def __add_document(self, doc_id: int, text: str):
        tokens = tokenize_text(text)
        for t in tokens:
            if t not in self.index:
                self.index[t] = set()
            if doc_id not in self.term_frequency:
                self.term_frequency[doc_id] = Counter()
            self.index[t].add(doc_id)
            self.term_frequency[doc_id][t] +=1

    def get_documents(self, term: str) -> list[int]:
        if term not in self.index:
            return []
        return sorted(list(self.index[term]))
    def get_document_movie(self, doc_id: int) -> Movie:
        return self.docmap[doc_id]
    def get_tf(self, doc_id: int, term: str) -> int:
        if doc_id not in self.term_frequency:
            return 0
        return self.term_frequency[doc_id][term]
    
    def build(self):
        movies = load_movies()
        for movie in movies:
            self.__add_document(movie["id"], f"{movie["title"]} {movie["description"]}")
            self.docmap[movie["id"]] =  movie
    def save(self):
        index_file = open(INDEX_CACHE_PATH, "wb")
        docmap_file = open(INDEX_DOCMAP_CACHE_PATH, "wb")
        term_frequency_file = open(INDEX_TERMFREQUENCY_CACHE_PATH, "wb")
        pickle.dump(self.index, index_file)
        pickle.dump(self.docmap, docmap_file)
        pickle.dump(self.term_frequency, term_frequency_file)

    def load(self):
        try:
            index_file = open(INDEX_CACHE_PATH, "rb")
            docmap_file = open(INDEX_DOCMAP_CACHE_PATH, "rb")
            term_frequency_file = open(INDEX_TERMFREQUENCY_CACHE_PATH, "rb")
            self.index = pickle.load(index_file)
            self.docmap = pickle.load(docmap_file)
            self.term_frequency = pickle.load(term_frequency_file)
        except(Exception):
            raise Exception("Trying to access inexistant file")
        
def build_command() -> InvertedIndex:
    index = InvertedIndex()
    index.build()
    index.save()
    return index

def idf_command(term: str):
    term = tokenize_single_term(term)
    index = InvertedIndex()
    index.load()
    total_doc_count = len(index.docmap)
    matching_doc_count = len(index.get_documents(term))
    result= math.log((total_doc_count +1)/(matching_doc_count+1))
    print(f"Inverse document frequency of '{term}': {result:.2f}")

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[Movie]:
    results = []
    index = InvertedIndex()
    try:
        index.load()
    except(Exception):
        raise Exception("Unable to load index")
    query_tokens = tokenize_text(query)
    for query_token in query_tokens:
        doc_indexes = index.get_documents(query_token)
        for i in doc_indexes:
            movie = index.get_document_movie(i)
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


def tokenize_single_term(term: str) -> str:
    tokens = tokenize_text(term)
    if len(tokens) != 1:
        raise Exception("invaild number of tokens in terms, expecting 1")
    else:
        return tokens[0]
