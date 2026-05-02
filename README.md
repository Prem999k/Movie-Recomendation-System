# 🎬 Movie Recommendation System (Machine Learning Project)

## 📌 Project Overview

This project is a **Movie Recommendation System** built using **Machine Learning techniques (TF-IDF + Cosine Similarity)**.

The system recommends similar movies based on content such as overview, genres, and tagline, providing users with personalized suggestions.


---

## 🌐 Live Demo

🔗 https://movie-recomendation-system-premkumark.streamlit.app/

---

## 🎯 Objectives

* Build a content-based movie recommendation system
* Use Natural Language Processing (NLP) techniques
* Convert text data into numerical vectors using TF-IDF
* Compute similarity between movies
* Provide top movie recommendations based on user input

---

## 🚀 Features

* 🔍 Search for any movie
* 🎯 Get Top 10 similar movie recommendations
* ⚡ Fast similarity computation using TF-IDF
* 🎨 Clean and interactive UI using Streamlit

---

## 📊 Dataset Information

* Dataset: Movie dataset (CSV)
* Features used:

  * Movie Title
  * Overview
  * Genres
  * Tagline

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:**

  * Pandas
  * Scikit-learn
  * Streamlit

---

## 🧠 Model / Algorithm Used

### 🔹 TF-IDF (Term Frequency - Inverse Document Frequency)

* Converts text data into numerical vectors
* Highlights important words in a document

### 🔹 Cosine Similarity

* Measures similarity between movie vectors
* Helps find movies with similar content

---

## 🔄 Workflow

* Data Loading
* Data Cleaning
* Feature Combination (overview + genres + tagline)
* Text Vectorization using TF-IDF
* Similarity Calculation using Cosine Similarity
* Recommendation Generation
* Web App Deployment using Streamlit

---

## 📊 How It Works

1. Combine movie features into a single text column
2. Convert text into TF-IDF vectors
3. Compute cosine similarity between movies
4. When user selects a movie:

   * Find similarity scores
   * Sort movies based on similarity
   * Recommend Top 10 similar movies

---

## 📈 Key Insights

* Content-based filtering works well without user data
* TF-IDF helps extract meaningful text features
* Cosine similarity efficiently finds similar items
* Simple models can produce powerful recommendations

---

## 🚀 Future Improvements

* Add collaborative filtering
* Use deep learning (NLP models like BERT)
* Improve UI/UX design
* Add movie posters and ratings
* Deploy on cloud with scalability

---

## 🙌 Conclusion

This project demonstrates how **Machine Learning and NLP techniques** can be used to build an effective recommendation system, providing personalized movie suggestions based on content similarity.

---
