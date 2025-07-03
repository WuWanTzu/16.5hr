
"""
This project implements a basic content-based recommender system.
It demonstrates how AI recommenders work using a text-based dataset (Korean drama plots).
Method: Content-Based Filtering using TF-IDF and cosine similarity.
Dataset: KoreanDramaDescriptions.csv (100+ entries)
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("KoreanDramaDescriptions.csv")

# Drop rows with missing descriptions and keep necessary columns
df = df.dropna(subset=["description"])
df = df[["title", "description"]]

# Create TF-IDF matrix based on drama descriptions
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Build a recommender function
def get_recommendations(title, cosine_sim=cosine_sim):
    # Find index of the given title
    indices = df.index[df['title'] == title].tolist()
    if not indices:
        return ["Title not found."]
    idx = indices[0]

    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5
    drama_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[drama_indices].tolist()

# Example usage
if __name__ == "__main__":
    print("Recommendations for 'KDrama 10':")
    recommendations = get_recommendations("KDrama 10")
    for i, title in enumerate(recommendations, 1):
        print(f"{i}. {title}")
