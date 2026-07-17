# Netflix Data Analysis using Python

## Overview

This project explores Netflix's content catalog using Python and performs data cleaning, exploratory data analysis (EDA), and visualization to uncover insights about movies and TV shows available on Netflix.

The analysis focuses on content types, ratings, genres, countries, directors, release patterns, durations, and missing values using Pandas and Matplotlib.

---

## Dataset Information

The dataset contains information about Netflix titles, including:

* Show ID
* Type (Movie or TV Show)
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genres (Listed In)
* Description

---

## Technologies Used

* Python
* Pandas
* Matplotlib

---

## Data Cleaning Performed

The following preprocessing steps were applied:

* Removed rows containing missing values in:

  * `date_added`
  * `rating`
  * `duration`
* Standardized column names.
* Converted `Date_Added` into datetime format.
* Extracted numeric values from the `Duration` column for further analysis.
* Split multi-value columns such as:

  * Country
  * Cast
  * Genres (`Listed_In`)
* Handled month-wise ordering while analyzing content additions.

---

## Analysis Performed

The project answers several analytical questions, including:

### Content Analysis

* Total number of Movies and TV Shows.
* Distribution of content ratings.
* Top 10 countries producing Netflix content.
* Top 10 directors by number of titles.
* Most common Netflix genres.
* Number of titles added each year.
* Number of titles released each year.
* Month-wise content additions on Netflix.

### Duration Analysis

* Longest movie available in the dataset.
* Longest running TV show based on number of seasons.
* Distribution of movie durations.
* Distribution of TV show seasons.

### Historical Analysis

* Oldest movie present in the dataset.
* Most and least active months for content additions.

### Cast Analysis

* Top actors appearing most frequently in Netflix titles.

### Data Quality Analysis

* Visualization of missing values remaining in the dataset.

---

## Visualizations Generated

The project generates and saves the following charts:

| Visualization                 | File Name                |
| ----------------------------- | ------------------------ |
| Movies vs TV Shows            | `type_compare.png`       |
| Content Rating Distribution   | `ratings.png`            |
| Top 10 Countries              | `topcountry.png`         |
| Top 10 Directors              | `topdirector.png`        |
| Most Common Genres            | `genre.png`              |
| Content Added Each Year       | `content_year.png`       |
| Monthly Content Additions     | `movie_add.png`          |
| Movie Duration Distribution   | `movie_distribution.png` |
| TV Show Duration Distribution | `show_distribution.png`  |
| Missing Values Visualization  | `Missing.png`            |

---

## Project Structure

```
netflix-data-analysis/
│
├── netflix/
│   ├── Missing.png
│   ├── content_year.png
│   ├── genre.png
│   ├── movie_add.png
│   ├── movie_distribution.png
|   ├── netflix_data.csv
│   ├── ratings.png
│   ├── show_distribution.png
│   ├── topcountry.png
│   ├── topdirector.png
│   └── type_compare.png
│
├── Readme.md
└── netflix_analysis.py
```

---

## Key Python Concepts Used

* Data Cleaning
* GroupBy Operations
* Datetime Handling
* String Operations
* Regular Expressions (Regex)
* Data Aggregation
* Sorting and Filtering
* Missing Value Analysis
* Data Visualization
* Exploratory Data Analysis (EDA)

---

## How to Run the Project

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd Netflix-Data-Analysis
```

3. Install the required libraries.

```bash
pip install pandas matplotlib
```

4. Run the Python script.

```bash
python netflix_analysis.py
```

The generated visualizations will be saved inside the `netflix` folder.

---

## Conclusion

This project demonstrates practical data cleaning, exploratory data analysis, and visualization techniques using Pandas and Matplotlib. It provides insights into Netflix's content catalog, including trends in content additions, genre popularity, duration patterns, and distribution across countries, ratings, and directors.
