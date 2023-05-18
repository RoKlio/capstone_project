# Movie Dataset Analysis

## This is a capstone project for Code Academy course programme

This project involves the analysis of a movie dataset using Python and various libraries. The dataset used in this project is stored in a CSV file named "movie_metadata.csv". The goal of this project is to perform exploratory data analysis (EDA) on the dataset, and train the model for IMDB score prediction.

## Table of Contents
- [Project structure](#project-structure)
- [Imports](#imports)
- [Data Loading](#data-loading)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Dealing with Missing Values](#dealing-with-missing-values)
- [Further Examination](#further-examination)

## Project structure

The project structure is organized as follows:

├── data/
│ └── movie_metadata.csv
├── flask_app/
│ ├── app.py
│ ├── index.html
└── notebooks/
│ └── modelling_and_EDA.ipynb

## Imports

The required libraries for this project are imported.

## Data Loading

The dataset is loaded from the "movie_metadata.csv" file using the pandas library. The loaded dataset is stored in a pandas DataFrame named `df`.

## Exploratory Data Analysis (EDA)

The EDA section begins with examining the dataset. Here we plot some graphs about our data set such as most popular language, actors and directors. We also check for some of the correlations between data.

## Feature engineering

We add some features to our dataset. I think important ones should be actor and director popularity and profit that the movie has made.

## Modelling

Here we make a tunable LSTM model and check its predictions. Then I compare it to some of machine learning models.

## Conclusion

This project provides a detailed analysis of the movie dataset, including data loading, exploratory data analysis, handling missing values, and additional examination. The code can be used as a starting point for further analysis or as a reference for working with similar datasets.


