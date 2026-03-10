# 🚀 Machine Learning Algorithm Explorer

Machine Learning Algorithm Explorer is an **interactive AutoML-style platform** that allows users to upload datasets, automatically preprocess the data, train multiple machine learning models, and compare their performance.

The system helps users **identify the best algorithm for their dataset** and provides **visual insights into model performance**.

---

## 📌 Features

- Upload any CSV dataset
- Automatic data preprocessing
- Detects whether the problem is **Classification or Regression**
- Trains multiple machine learning models
- Model comparison dashboard
- Best model recommendation
- Interactive visualization for each model

---

## 🧠 Supported Algorithms

### Classification

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes
- Gradient Boosting
- XGBoost

### Regression

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Support Vector Regression (SVR)
- Gradient Boosting Regressor

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Scikit-Learn | Machine learning algorithms |
| XGBoost | Gradient boosting implementation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| Streamlit | Interactive UI |

---

## ⚙️ Project Workflow

1. Upload CSV dataset  
2. Automatic dataset analysis  
3. Data preprocessing  
4. Model training  
5. Performance evaluation  
6. Best model recommendation  
7. Model visualization  

---

## 📂 Project Structure


ML-Algorithm-Explorer
│
├── app.py
├── preprocessing.py
├── models.py
├── evaluation.py
├── visualization.py
│
├── datasets/
│
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone [https://github.com/Swara-art/AutoML]
cd ml-algorithm-explorer
```
2. Install dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
streamlit run app.py
```

The application will open in your browser.

## 🔮 Future Improvements

1. Hyperparameter tuning
2. Automatic feature engineering
3. Deep learning model support
4. Model explainability using SHAP
5. Cloud deployment
