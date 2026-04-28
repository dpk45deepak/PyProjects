# 📊 Logistic Regression

## 📌 Definition

Logistic Regression is a **supervised machine learning algorithm** used for **classification problems**, where the output is categorical (e.g., Yes/No, 0/1, True/False).

Unlike Linear Regression, it predicts the **probability** that a given input belongs to a particular class.

---

## 🧠 Intuition

Instead of predicting continuous values, Logistic Regression:

* Maps input features to a **probability (0 to 1)**
* Uses a **threshold (usually 0.5)** to classify output

---

## 🔢 Mathematical Concept

The core of Logistic Regression is the **Sigmoid Function**:

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

Where:

* ( z = w_1x_1 + w_2x_2 + ... + b )
* Output is always between **0 and 1**

---

## 📉 Sigmoid Curve (S-Shape)

* If output > 0.5 → Class = 1
* If output < 0.5 → Class = 0

---

## ⚙️ Working Steps

1. Input features are multiplied with weights
2. Linear combination is calculated
3. Sigmoid function is applied
4. Output probability is generated
5. Threshold is applied for classification

---

## 📦 Types of Logistic Regression

1. **Binary Logistic Regression**

   * Output: 0 or 1

2. **Multinomial Logistic Regression**

   * More than 2 classes

3. **Ordinal Logistic Regression**

   * Ordered categories (e.g., Low, Medium, High)

---

## 🎯 Applications

* Spam Detection (Email)
* Disease Prediction (Diabetes, Heart Disease)
* Credit Risk Analysis
* Customer Churn Prediction

---

## 📊 Advantages

* Simple and easy to implement
* Works well with linearly separable data
* Provides probability output
* Efficient for small to medium datasets

---

## ⚠️ Limitations

* Cannot capture complex non-linear relationships
* Sensitive to outliers
* Requires feature engineering for better performance

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Curve

---

## 🧮 Cost Function (Log Loss)

[
Loss = -\frac{1}{n} \sum [y \log(p) + (1-y)\log(1-p)]
]

---

## 🛠️ Example (Python - Scikit-learn)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load dataset
X, y = load_iris(return_X_y=True)

# Binary classification (filtering)
X, y = X[y != 2], y[y != 2]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print(predictions)
```

---

## 💡 Key Takeaways

* Logistic Regression is used for **classification, not regression**
* Uses **Sigmoid function** for probability mapping
* Output is **probabilistic + interpretable**
* One of the most **important foundational ML algorithms**

---

## 🚀 When to Use?

Use Logistic Regression when:

* You have **binary or categorical output**
* Data is relatively **simple and linearly separable**
* You need a **baseline model**

---

## 📚 References

* Scikit-learn Documentation
* Machine Learning by Andrew Ng
* ISLR (Introduction to Statistical Learning)
