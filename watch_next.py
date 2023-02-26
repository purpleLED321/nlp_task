import spacy

nlp = spacy.load('en_core_web_lg')

Planet_Hulk = nlp('''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')
token1 = nlp(
    ' '.join([str(t) for t in Planet_Hulk if not t.is_stop]))

movie_dict = {}


# Define a function to read a file containing movie titles and descriptions
def movie_file_reader():
    with open('movies.txt', 'r') as m:
        movies = m.readlines()
        for movie in movies:
            # Splits line then adds tile and description to dict
            title, description = movie.split(' :')
            movie_dict[title.strip()] = description.strip()


# Define a function to suggest the next movie to watch
def watch_next():
    # temp dict to hold the similarity value
    temp_dict = movie_dict
    # Iterate over each title in the movie_dict dictionary
    for token_ in movie_dict:
        # remove stop words and calculate similarity between the descriptions
        tokentest = nlp(
            (' '.join([str(t) for t in nlp(movie_dict[token_]) if not t.is_stop])))
        temp_dict[token_] = token1.similarity(tokentest)
    # Determine the title with the highest similarity score and print it as suggestion
    similar_key = max(temp_dict, key=temp_dict.get)
    print(f'Try watching {similar_key} next')


movie_file_reader()
watch_next()
