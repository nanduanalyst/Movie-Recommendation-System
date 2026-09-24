# 🎬 Movie Recommendation System

A Machine Learning based **Content-Based Movie Recommendation System** built with Python and Streamlit.

The application allows a user to select a movie and receive **5 similar movie recommendations** through a simple web interface.

## 🌐 Live Demo

Add your deployed Streamlit URL here:

"movie-recommendation-system-g4zdyqhpydlrnhayt6w4mb.streamlit.app"

## 📌 Project Overview

This project uses the **TMDB 5000 Movies Dataset** and **TMDB 5000 Credits Dataset**.

The notebook processes movie information such as:

- Genres
- Keywords
- Overview
- Cast
- Director

These features are combined into a `tags` column and converted into numerical vectors using `CountVectorizer`.

Cosine similarity is then used to identify movies with similar content.

## 🤖 Machine Learning Workflow

```text
TMDB Movies Dataset
        ↓
TMDB Credits Dataset
        ↓
Merge on Movie Title
        ↓
Select useful movie features
        ↓
Clean genres, keywords, cast and director
        ↓
Create "tags"
        ↓
CountVectorizer
        ↓
Cosine Similarity
        ↓
Top 5 Similar Movies
        ↓
Streamlit Web App
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 📊 Dataset

### TMDB 5000 Movies

The movies dataset contains **4,803 movie records** and includes fields such as:

- `title`
- `genres`
- `keywords`
- `overview`
- `popularity`
- `release_date`
- `vote_average`
- `vote_count`
- `runtime`
- `budget`
- `revenue`

### TMDB 5000 Credits

The credits dataset contains movie-related:

- `cast`
- `crew`
- `movie_id`
- `title`

## 🧠 Recommendation Method

This is a **content-based recommendation system**.

The following information is combined to create movie tags:

```text
Overview + Genres + Keywords + Cast + Director
```

The tags are converted into numerical vectors using:

```python
CountVectorizer(
    max_features=5000,
    stop_words="english"
)
```

Cosine similarity is calculated between the movie vectors.

The system returns the 5 movies with the highest similarity.

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── app.py
│   └── Streamlit web application
│
├── movies.pkl
│   └── Processed movie dataframe
│
├── similarity.pkl
│   └── Compact recommendation mapping
│       Contains the top 5 recommendations for each movie
│
├── movie_pred.ipynb
│   └── Data preprocessing and ML workflow
│
├── tmdb_5000_movies.csv
│   └── TMDB movies dataset
│
├── tmdb_5000_credits.zip
│   └── Compressed TMDB credits dataset
│
├── requirements.txt
│   └── Required Python libraries
│
└── .gitignore
    └── Files ignored by Git
```

## 🔍 `movie_pred.ipynb` — Step-by-Step

### 1. Load the datasets

```python
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
```

### 2. Merge the datasets

```python
movies = movies.merge(credits, on="title")
```

### 3. Select important columns

```python
movie = movies[
    ["genres", "id", "keywords", "title",
     "overview", "cast", "crew"]
]
```

### 4. Remove missing values

```python
movie.dropna(inplace=True)
```

### 5. Convert JSON-like columns

Genres and keywords are converted into lists of names.

### 6. Select the first three cast members

The first three actors are extracted from the cast information.

### 7. Find the director

The director is extracted from the crew information.

### 8. Process the overview

The overview is split into individual words.

### 9. Remove spaces from names

For example:

```text
Tom Hanks
```

becomes:

```text
TomHanks
```

### 10. Create the tags column

```python
movie["tags"] = (
    movie["overview"]
    + movie["genres"]
    + movie["keywords"]
    + movie["cast"]
    + movie["crew"]
)
```

### 11. Create the final dataframe

```python
new_df = movie[["id", "title", "tags"]]
```

### 12. Convert tags into text

```python
new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
```

### 13. Convert text to lowercase

```python
new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())
```

### 14. Vectorization

```python
cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(
    new_df["tags"]
).toarray()
```

### 15. Calculate cosine similarity

```python
similarity = cosine_similarity(vectors)
```

### 16. Save the processed movie data

```python
joblib.dump(new_df, "movies.pkl")
```

### 17. Save recommendation data

The deployed project uses a compact `similarity.pkl` containing the top 5 recommendation indexes for each movie. This keeps the GitHub/Streamlit deployment lightweight while preserving the recommendation results.

## 🖥️ Streamlit Application

The Streamlit app:

1. Loads `movies.pkl`
2. Loads the compact `similarity.pkl`
3. Shows a movie dropdown
4. Takes the selected movie
5. Finds its movie index
6. Gets the stored top 5 similar movie indexes
7. Displays the recommended movies

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
```

Open the project:

```bash
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

## 🚀 Deployment

This application can be deployed using **Streamlit Community Cloud**.

After connecting the GitHub repository, use:

```text
Main file: app.py
```

The deployed application can then be shared through a public `.streamlit.app` URL.

## 📈 Future Improvements

- Add movie posters
- Add movie descriptions
- Add ratings
- Add release year
- Add movie search
- Add genre filters
- Add TMDB poster API
- Add movie trailers
- Improve the Streamlit UI

## 👨‍💻 Author

**Nandu Rastogi**

Aspiring Data Analyst | Machine Learning Engineer

GitHub: `https://github.com/nanduanalyst`
