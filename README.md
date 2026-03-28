# Movie Recommendation System (ML-Based)

A content-based movie recommendation engine built using Python. This project utilizes Natural Language Processing (NLP) and Machine Learning techniques to suggest movies based on genre and category similarity.

---

##  Overview
This project demonstrates how text-based data can be converted into numerical vectors to find relationships between items. It is designed to solve the problem of manual discovery by providing automated suggestions based on a user's favorite title.

---

##  Tech Stack & Prerequisites
The project is built using Python and the following libraries:
- **Pandas:** For data manipulation and storage.
- **Scikit-learn:** For Machine Learning (TF-IDF Vectorizer and Cosine Similarity).

---

## Installation
To run this project locally, you must have Python installed. Install the required dependencies using pip:

```bash
pip install pandas scikit-learn
```

---

## How it works
This project is a Content-Based Recommender System. It suggests movies by calculating the mathematical similarity between the "features" (categories/genres) of different films.
1. Data Representation
The system starts with a dataset containing movie titles and their associated categories. Before analysis, the text is normalized (lowercase and stripped of spaces) to ensure consistent matching.

2. Feature Extraction (TF-IDF)
Since machines cannot understand raw text, we use the TF-IDF (Term Frequency-Inverse Document Frequency) method:

 Term Frequency (TF): Measures how often a word appears in a specific movie category.

 Inverse Document Frequency (IDF): Reduces the weight of common words (like "action") and highlights unique, descriptive keywords (like "interstellar").

3. Calculating Similarity
The system computes the Cosine Similarity between movie vectors. This measures the cosine of the angle between two points in a multi-dimensional space.
The Similarity Formula:

   similarity = cos(theta) = (A * B) / (||A|| ||B||)

Score of 1.0: Perfect match (identical categories).

Score of 0.0: No similarity.

The system identifies the top 3 movies with the highest scores and displays them to the user.

---

## Usage Instructions
1. Clone this repository or download the python movie_recommender.py file.

2. Run the script in your terminal:
python movie_recommender.py

3. When prompted, enter a movie name (e.g., inception or avengers).

4. The system will output the top 3 movies you might like based on the database.

---

## Screenshot

<img width="810" height="721" alt="Screenshot 2026-03-26 at 7 49 04 PM" src="https://github.com/user-attachments/assets/d0aa87bb-b24d-4f78-be8f-b574dee78b59" />
<img width="644" height="359" alt="Screenshot 2026-03-26 at 7 50 21 PM" src="https://github.com/user-attachments/assets/4b9c0cba-d174-468d-a65e-03f27095ee53" />

---

## Project Structure
1. movie_recommender.py - The main Python script containing the logic.

2. README.md - Documentation and setup guide.

3. requirements.txt - List of Python dependencies.

---

## Limitations & Future Scope
1. Exact Matches: The current version requires exact string input (handled by .lower().strip()).

2. Data Scaling: Future updates will transition from a manual dictionary to a larger CSV dataset (e.g., TMDb 5000 Movies).

3. Fuzzy Matching: Planning to implement the thefuzz library to handle user typos.
