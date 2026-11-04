import string

def keyword_search(movies: list, search_query: str) -> str:
    result = ""
    i = 0
    result_count = 0
    while(i < len(movies) and result_count <5):
        movie = movies[i]
        if check_query(search_query.lower(), movie["title"]):
            result_count +=1
            if result =="":
                result = f"{i}. {movie["title"]}"
            else:
                result = f"{result}\n{i}. {movie["title"]}"
        i += 1
    return result

def check_query(search_query: str, movie_title: str) -> bool:
    table = str.maketrans("", "",string.punctuation)
    query = search_query.lower()
    title = movie_title.lower()
    query = str.translate(query, table)
    title = str.translate(title, table)
    return query in title