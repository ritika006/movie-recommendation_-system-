# 🎬 Movie Recommendation System

A **Movie Recommendation System** that suggests movies based on user preferences using **Content-Based Filtering** techniques.  
This project demonstrates how machine learning and similarity algorithms can be used to power real-world applications like Netflix or Amazon Prime recommendations.

---

## 🚀 Live Demo

🔗 **Live Application:**  
👉 [https://mrs-python.streamlit.app/](https://mrs-python.streamlit.app/)

---

## 📌 Project Overview

This **Movie Recommendation System** helps users discover new movies similar to their interests.  
By analyzing movie metadata such as **genres, tags, and descriptions**, the system recommends movies using **cosine similarity**.

---

## 🧠 Features

✔ Content-based movie recommendations  
✔ Similarity calculation using cosine similarity  
✔ Clean and interactive UI  
✔ Fast response time using preprocessed data  
✔ Easy to extend with collaborative filtering  

---

## 🧰 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Flask / Streamlit** (for web interface)
- **Pickle** (for saving models)
- **HTML / CSS** (frontend)

---

## 🧩 Dataset

The system uses a movie dataset containing:

- Movie title
- Genres
- Overview / tags
- Movie ID

📂 Common source: **MovieLens Dataset**

Example:
movieId | title | genres
1 | Toy Story (1995) | Animation|Comedy|Family


---

## 💻 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ritika006/movie-recommendation_-system-.git
```

### 2️⃣ Navigate to Project Directory
```
cd movie-recommendation_-system-
```

### 3️⃣ Create Virtual Environment (Optional)
```
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 4️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### ▶️ Usage
Run the Application
```
streamlit run app.py
```


## Open browser and visit:

http://localhost:5000

## 🎯 Example Recommendation Results
🔍 User Input:
Movie Selected: Avatar

### 🎬 Recommended Movies:
1. Guardians of the Galaxy
2. Interstellar
3. Star Wars: The Force Awakens
4. Avengers: Infinity War
5. Thor: Ragnarok

## 📈 How It Works
🧠 Content-Based Filtering

- Combines movie metadata (genres, tags, overview)

- Converts text into vectors using CountVectorizer

- Computes similarity using Cosine Similarity

- Recommends top-N most similar movies

## 🛠️ Project Structure
```
movie-recommendation_-system-/
│
├── app.py                     # Main application
├── movie_recommender.py       # Recommendation logic
├── movies.pkl                 # Movie data
├── similarity.pkl             # Similarity matrix
├── requirements.txt           # Dependencies
├── screenshots/               # Screenshots & GIFs
│   ├── home.png
│   ├── recommendations.png
│   └── demo.gif
└── README.md
```

## 🚀 Future Enhancements

🔄 Add collaborative filtering

⭐ Include user ratings

📱 Improve UI with React

☁ Deploy on cloud (AWS / GCP)

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

Commit your changes

Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

MovieLens Dataset

Scikit-learn Documentation

Flask / Streamlit Community

