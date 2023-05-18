# Movie Dataset Analysis

This project involves the analysis of a movie dataset using Python and various libraries such as pandas, seaborn, numpy, matplotlib, and torch. The dataset used in this project is stored in a CSV file named "movie_metadata.csv". The goal of this project is to perform exploratory data analysis (EDA) on the dataset, handle missing values, and gain insights from the data.

## Table of Contents

- [Imports](#imports)
- [Data Loading](#data-loading)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Dealing with Missing Values](#dealing-with-missing-values)
- [Further Examination](#further-examination)

## Imports

The required libraries for this project are imported, including pandas, seaborn, numpy, matplotlib, torch, and scikit-learn.

## Data Loading

The dataset is loaded from the "movie_metadata.csv" file using the pandas library. The loaded dataset is stored in a pandas DataFrame named `df`.

## Exploratory Data Analysis (EDA)

The EDA section begins with examining the dataset by displaying the first few rows using `df.head()`. The column names are displayed using `df.columns`, and the shape of the dataset (number of rows and columns) is printed using `df.shape`. The `df.info()` method provides information about the data types and missing values in each column.

A summary of the numerical columns is generated using `df.describe().T`, which includes statistics such as count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values.

## Dealing with Missing Values

The code checks for missing values in each column using `df.isna().sum()`. Based on the number of missing values and the feasibility of filling or dropping the columns, certain columns are dropped or filled. For example, columns with a small number of missing values or categorical values are dropped using `df.dropna()`. The `budget` and `gross` columns are filled with the median values using `fillna()`.

After handling missing values, duplicate rows are removed using `df.drop_duplicates()`. The final shape of the dataset is printed to show the number of rows and columns remaining.

## Further Examination

Additional analysis is performed on the dataset. The count of movies per language is displayed using a bar plot created with seaborn. A countplot is used to visualize the number of movies made per year. Lastly, a line plot is used to explore the relationship between IMDb scores and the number of Facebook likes on movie pages.

## Conclusion

This project provides a detailed analysis of the movie dataset, including data loading, exploratory data analysis, handling missing values, and additional examination. The code can be used as a starting point for further analysis or as a reference for working with similar datasets.
