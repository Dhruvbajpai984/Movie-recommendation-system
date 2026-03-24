#  Movie Recommendation System (ML Based)

##  Project Description
This project is a simple Movie Recommendation System built using Python and basic Machine Learning concepts.  
It recommends movies based on similarity in their genres.

Unlike a basic system with fixed recommendations, this project uses a similarity measure to suggest movies dynamically.

---

##  How it Works
- A small dataset of movies and their genres is created.
- The genre text is converted into numerical form using CountVectorizer.
- Cosine Similarity is used to find similarity between movies.
- When the user enters a movie name, the system recommends similar movies.

---

##  Machine Learning Concepts Used
- Feature Extraction (CountVectorizer)
- Similarity Measurement (Cosine Similarity)
- Basic Recommendation System

---

##  Technologies Used
- Python
- Pandas
- Scikit-learn

---

##  How to Run
1. Install required libraries:
   ```bash
   pip install pandas scikit-learn
