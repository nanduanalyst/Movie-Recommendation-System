# 🎬 Movie Recommendation System

A Machine Learning based **Movie Recommendation System** that recommends movies based on the movie selected by the user.

The project uses the **TMDB 5000 Movies Dataset** and is designed with a simple and interactive **Streamlit user interface**.

## 🚀 Live Demo

🔗 **Streamlit App:** Add your deployed Streamlit URL here

## 📌 Project Overview

Finding a good movie to watch can be difficult when there are thousands of movies available.

This project uses Machine Learning to recommend movies that are similar to a movie selected by the user.

The user selects a movie from the Streamlit interface, and the system returns a list of recommended movies.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* TMDB Dataset

## 🤖 Machine Learning Approach

This project uses a **content-based recommendation approach**.

Movie information is processed and converted into features. The similarity between movies is then calculated to find movies that are similar to the selected movie.

The trained movie data and similarity matrix are stored in:

```text
movies.pkl
similarity.pkl
```

## 📊 Dataset

The project uses the **TMDB 5000 Movies Dataset**, containing movie information such as:

* Movie Title
* Genres
* Keywords
* Overview
* Popularity
* Release Date
* Runtime
* Vote Average
* Vote Count

## 💻 Streamlit User Interface

The Streamlit application provides a simple interface where users can:

1. Select a movie
2. Click the recommendation button
3. Get similar movie recommendations

Example:

```text
🎬 Movie Recommendation System

Select a movie:
[ Avatar                         ]

        [ Recommend Movies ]

Recommended Movies:

1. Guardians of the Galaxy
2. Star Trek
3. Interstellar
4. The Avengers
5. Iron Man
```

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
```

Move into the project folder:

```bash
cd movie-recommendation-system
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 requirements.txt

```text
streamlit
pandas
numpy
scikit-learn
```

## 🎯 Project Features

* 🎬 Movie selection
* 🤖 Machine Learning based recommendations
* 🔎 Similar movie search
* 🖥️ Interactive Streamlit interface
* ⚡ Fast recommendations using pre-trained files
* 🌐 Can be deployed as a live web application

## 🔮 Future Improvements

* Add movie posters
* Add movie trailers
* Add movie ratings
* Add genre filtering
* Add search functionality
* Improve recommendation accuracy
* Deploy the application online

## 👨‍💻 Author

**Nandu Rastogi**

Aspiring **Data Analyst | Machine Learning Engineer**

GitHub: https://github.com/nanduanalyst

LinkedIn: linkedin.com/in/nandu-rastogi-2a104b319



