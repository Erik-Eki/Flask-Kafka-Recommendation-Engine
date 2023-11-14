# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the movie dataset
games_df = pd.read_csv("./data/video_game_data.csv")

# Define a function to create a soup of features
def create_soup(x):
    return ' '.join(x['Genre']) + ' ' + x['Name']

# Apply the function to the games_df
games_df['soup'] = games_df.apply(create_soup, axis=1)

# Define a TF-IDF Vectorizer Object
tfidf = TfidfVectorizer(stop_words='english')

# Compute the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(games_df['soup'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create a reverse map of indices and movie titles
indices = pd.Series(games_df.index, index=games_df['Name']).drop_duplicates()

# Define a function to get recommendations based on a movie title
def get_recommendations(data, cosine_sim=cosine_sim):
    genre = data["genre"]
    rating = float(data["rating"])
    # Filter the games based on the genre and rating
    filtered_games = games_df[(games_df['Genre'].str.contains(genre)) & (games_df['User_Score'] >= rating)]

    # Sort the games by popularity
    sorted_games = filtered_games.sort_values(by='Global_Sales', ascending=False)

    # Get the top 10 games
    top_games = sorted_games.head(10)

    # Return the list of movie titles
    return top_games[['Name', 'Genre', 'User_Score', 'Critic_Score', 'Global_Sales']].to_dict(orient="records")
    
    # title = data["genre"]
    
    # # Get the index of the movie that matches the title
    # idx = indices[title]

    # # Get the pairwsie similarity scores of all games with that movie
    # sim_scores = list(enumerate(cosine_sim[idx]))

    # # Sort the games based on the similarity scores
    # sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # # Get the scores of the 10 most similar games
    # sim_scores = sim_scores[1:11]

    # # Get the movie indices
    # movie_indices = [i[0] for i in sim_scores]

    # # Return the top 10 most similar games
    # return games_df['Name'].iloc[movie_indices]

# Define a function to recommend games based on a user's preferences
def recommend_games(preferences):
    # Create an empty list to store the recommended games
    recommended_games = []

    # Loop through the user's preferences
    for preference in preferences:
        # Get the recommendations for the preference
        recommendations = get_recommendations(preference)

        # Append the recommendations to the list
        recommended_games.append(recommendations)

    # Return the list of recommended games
    return recommended_games