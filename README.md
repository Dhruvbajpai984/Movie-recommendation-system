# Movie Recommendation System (ML-Based)

A simple **content-based movie recommendation system** built using Python and machine learning techniques.  
It suggests similar movies based on their genres using **cosine similarity**.

---

## Features

- Recommend movies based on user input
- Uses **TF-IDF vectorization** for better text representation
- Computes similarity using **cosine similarity**
- Simple and interactive command-line interface
- Beginner-friendly machine learning project

---

## How It Works

1. A small dataset of movies and their categories (genres) is created.
2. Text data is converted into numerical form using **TF-IDF Vectorizer**.
3. Cosine similarity is calculated between all movies.
4. When a user enters a movie name:
   - The system finds similar movies
   - Displays the top 3 recommendations

---

## Tech Stack

- Python 
- Pandas
- Scikit-learn

---

## ScreenShot

<img width="711" height="861" alt="Screenshot 2026-03-24 at 2 17 14 PM" src="https://github.com/user-attachments/assets/38584416-5bf3-40c4-9413-d216f792a834" />
<img width="612" height="329" alt="Screenshot 2026-03-24 at 2 17 36 PM" src="https://github.com/user-attachments/assets/a0f484ce-747e-4732-b322-d7e6bfa33d9e" />

---

##  Limitations
- Uses a small dataset
- Recommendations based only on category
- No real-time data

##  Future Improvements
- Integrate larger datasets (IMDb/TMDB)
- Add movie ratings and descriptions
- Build a web interface using Streamlit

---

##  Installation

1. Clone the repository:
```bash
git clone https://github.com/Dhruvbajpai984/movie-recommender.git



