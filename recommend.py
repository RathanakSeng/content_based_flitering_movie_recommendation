import pickle
import pandas as pd
import argparse

# Set up command-line argument parser
parser = argparse.ArgumentParser(description="Recommend similar movies.")
parser.add_argument("movie", type=str, help="The title of the movie to base recommendations on.")
parser.add_argument("--top_n", type=int, default=5, help="Number of recommendations to return (default: 5)")

args = parser.parse_args()
movie_input = args.movie
top_n = args.top_n

# Load 'new_dataset' from its pickle file
with open('./output/movies.pkl', 'rb') as f:
    movies = pickle.load(f)
    new_dataset = pd.DataFrame(movies)

# Load 'similar' (e.g., similarity matrix or array) from its pickle file
with open('./output/similar.pkl', 'rb') as f:
    similar = pickle.load(f)

def recommend(movie, top_n=5):
    """
    Recommend top N movies similar to the given movie title.
    
    Parameters:
        movie (str): The title of the movie to base recommendations on.
        top_n (int): Number of recommendations to return.
    
    Returns:
        list: A list of recommended movie titles.
    """
    movie = movie.strip().lower()
    match = new_dataset[new_dataset["title"].str.lower().str.strip() == movie]
    
    if match.empty:
        return f"Movie '{movie}' not found in the dataset."
    
    movie_index = match.index[0]
    distances = similar[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:top_n+1]
    
    recommendations = [new_dataset.iloc[i[0]].title for i in movie_list]
    return recommendations


# ========== RUN ==========
print(f"Recommended for '{movie_input}':")
result = recommend(movie_input, top_n)
if isinstance(result, list):
    for title in result:
        print("-", title)
else:
    print(result)