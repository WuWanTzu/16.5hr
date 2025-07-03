# Movie Recommendation System

This project implements a **Content-Based Recommendation System** using movie plot summaries.

## Method

- Each movie's `plot` is treated as its semantic feature using TF-IDF vectorization.
- When a user likes a specific movie, we recommend others with similar semantic content.
- This approach does **not** require user ratings, only the content of the items themselves.

## Dataset

- `movies_dataset.csv` includes 100 movies with the following fields:
  - id
  - title
  - genre
  - plot