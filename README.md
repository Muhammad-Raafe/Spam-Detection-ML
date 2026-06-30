# 📩 Spam Message Classifier

An interactive machine learning web app that classifies SMS/text messages as **Spam** or **Ham (Not Spam)** using a Naive Bayes classifier, built with Scikit-learn and deployed with Streamlit.

🔗 **Live Demo:** [Add your Streamlit Cloud link here]

---

## 🧠 Overview

This project applies **Natural Language Processing (NLP)** and **Multinomial Naive Bayes** to detect spam messages from raw text. The model is trained on the classic SMS Spam Collection dataset and wrapped in a clean, interactive dashboard where users can test any custom message in real time.

---

## ✨ Features

- 🔍 **Real-time message classification** — type any message and instantly get a Spam/Ham prediction with confidence score
- 📊 **Model performance dashboard** — accuracy, classification report, and confusion matrix
- 📈 **Interactive Plotly visualizations** — prediction confidence bar chart, class distribution pie chart, and confusion matrix heatmap
- 🌙 **Dark-themed responsive UI**
- ⚡ **Cached model training** for fast app performance

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| ML Library | Scikit-learn |
| Model | Multinomial Naive Bayes |
| Text Vectorization | CountVectorizer (Bag of Words) |
| Visualization | Plotly |
| Web Framework | Streamlit |
| Data Handling | Pandas, NumPy |

---

## 📂 Dataset

The model is trained on the **SMS Spam Collection Dataset**, containing 5,500+ labeled SMS messages categorized as `spam` or `ham`.

Dataset source: [UCI Machine Learning Repository / Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## ⚙️ How It Works

1. **Data Preprocessing** — Cleaned dataset, dropped unused columns, label-encoded target (`spam` / `ham`)
2. **Feature Extraction** — Converted raw text into numerical features using `CountVectorizer` (Bag of Words model)
3. **Train/Test Split** — 80/20 split for training and evaluation
4. **Model Training** — Trained a `MultinomialNB` classifier, well-suited for discrete text/word-count features
5. **Evaluation** — Assessed using accuracy score, confusion matrix, and classification report
6. **Deployment** — Wrapped in an interactive Streamlit app for live predictions

---

## 🚀 Running Locally

1. Clone the repository
```bash
git clone https://github.com/Muhammad-Raafe/Spam-Classification-ML.git
cd Spam-Classification-ML
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

Make sure `spam.csv` is present in the project root directory.

---

## 📁 Project Structure

```
Spam-Classification-ML/
│
├── app.py              # Streamlit web app
├── spam.csv             # Dataset
├── requirements.txt     # Python dependencies
└── README.md             # Project documentation
```

---

## 📊 Model Performance

The Multinomial Naive Bayes model achieves high accuracy on the test set, with detailed metrics (precision, recall, F1-score) available directly in the app's sidebar dashboard.

---

## 🔮 Future Improvements

- Add TF-IDF vectorization as an alternative to CountVectorizer
- Compare performance against Logistic Regression and SVM
- Add text preprocessing (stopword removal, stemming/lemmatization)
- Support batch CSV upload for bulk message classification

---

## 👤 Author

**Muhammad Raafe**
AI/ML Enthusiast | Building a portfolio in Machine Learning & Data Science

GitHub: [@Muhammad-Raafe](https://github.com/Muhammad-Raafe)
