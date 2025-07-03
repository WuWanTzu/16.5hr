
# Recommender System Project

This project implements a basic **Content-Based Filtering** recommender system using a dataset of Korean drama descriptions.

## ✅ Approach
- **Type**: Content-Based Filtering
- **Method**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Similarity Metric**: Cosine Similarity
- **Language**: Python

## 📁 Files
- `KoreanDramaDescriptions.csv`: A dataset with 100+ Korean drama descriptions (title + plot).
- `recommender_project.py`: Python code implementing the recommender system.
- `README.md`: This file, describing the approach.

## ▶️ How it Works
The system calculates similarity between drama plots using TF-IDF vectors, and recommends the top 5 dramas similar to the selected one.

## 💡 Example
```python
get_recommendations("KDrama 10")
```
Returns 5 similar Korean dramas based on their plot descriptions.
