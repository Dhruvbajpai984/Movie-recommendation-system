import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Simple Movie Recommender System\n")

# Step 1: Define movie dataset
movies_data = {
    "title": [
        "avengers", "iron man", "thor", "captain america",
        "spiderman", "venom", "batman", "superman",
        "interstellar", "inception", "gravity", "martian"
    ],
    "category": [
        "action superhero", "action superhero", "action superhero", "action superhero",
        "action superhero", "action antihero", "dark action", "hero action",
        "science fiction space", "science fiction thriller", "space drama", "space survival"
    ]
}

movies_df = pd.DataFrame(movies_data)

# Step 2: Convert text data into numerical vectors
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(movies_df["category"])

# Step 3: Compute similarity scores
similarity_matrix = cosine_similarity(feature_matrix)

# Step 4: Recommendation function
def get_recommendations(user_movie):
    user_movie = user_movie.lower().strip()

    if user_movie not in movies_df["title"].values:
        print("Sorry, movie not found in database.")
        return

    movie_idx = movies_df[movies_df["title"] == user_movie].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))

    # Sort movies based on similarity (highest first)
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    print("\nYou may also like:")
    count = 0
    for idx, score in similarity_scores:
        if idx != movie_idx:
            print("-", movies_df.iloc[idx]["title"])
            count += 1
        if count == 3:
            break

# Step 5: User interaction loop
while True:
    user_input = input("\nEnter a movie name: ")
    get_recommendations(user_input)

    again = input("\nWould you like another recommendation? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        print("Goodbye!")
        break