# Twitter Sentiment Analysis

This project is part of **Oasis Infobyte - Data Science Internship (oibsip_task3)**. It focuses on classifying tweets based on sentiment using machine learning techniques.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Libraries Used](#libraries-used)
- [Preprocessing Steps](#preprocessing-steps)
- [Modeling](#modeling)
- [Results](#results)
- [How to Run](#how-to-run)

## Overview
The goal of this project is to build a sentiment analysis model that can classify tweets as **positive**, **negative**, or **neutral** using a Logistic Regression classifier.

## Dataset
- `Twitter_Data.csv`
- Contains tweet text and corresponding sentiment categories.
- Labels: `0` = Negative, `1` = Neutral, `2` = Positive

## Libraries Used
- pandas
- re
- nltk
- scikit-learn

## Preprocessing Steps
- Removed URLs, mentions, hashtags, punctuations, and non-alphabetic characters.
- Converted text to lowercase.
- Removed stopwords using NLTK.
- Tokenized and cleaned tweet text for feature extraction.

## Modeling
- Used `TfidfVectorizer` to convert text data into numerical form.
- Trained a `LogisticRegression` model with the processed data.
- Split data into 80% training and 20% testing.

## Results
- Evaluated using classification report and confusion matrix.
- Metrics include precision, recall, f1-score, and accuracy.

## How to Run
1. Clone this repo or download the files.
2. Upload the `Twitter_Data.csv` file if using Google Colab.
3. Run the Python script (`task3.py` or notebook).
4. Install dependencies:
   ```bash
   pip install pandas scikit-learn nltk
   