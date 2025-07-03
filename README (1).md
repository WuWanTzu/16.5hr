# Book Recommendation System

This project is a simple **Content-Based Recommendation System** that suggests similar books based on their descriptions.

## Dataset

- Name: Book Descriptions Dataset
- Format: CSV
- Entries: 100 books
- Fields: title, description

## Method

We use TF-IDF vectorization to convert book descriptions into numerical vectors and then calculate cosine similarity to recommend similar books.