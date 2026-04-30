# 📌 Naive Bayes Algorithm

## 🔹 Definition
Naive Bayes is a **supervised machine learning algorithm** based on **Bayes' Theorem**.  
It is mainly used for **classification tasks** and assumes that all features are **independent** of each other.

👉 Called "Naive" because it assumes **feature independence**, which is often not true in real life.

---

## 🔹 Bayes Theorem


::contentReference[oaicite:0]{index=0}


Where:
- **P(A|B)** → Posterior probability  
- **P(B|A)** → Likelihood  
- **P(A)** → Prior probability  
- **P(B)** → Evidence  

---

## 🔹 Intuition (Simple Understanding)

- It calculates the probability of a class given input features.
- Then chooses the class with the **highest probability**.

👉 Example:
- Email classification:
  - Words like "offer", "win", "free" → likely **Spam**
  - Words like "meeting", "project" → likely **Not Spam**

---

## 🔹 How Naive Bayes Works

1. Calculate prior probability of each class
2. Calculate likelihood of features given class
3. Apply Bayes theorem
4. Predict class with highest probability

---

## 🔹 Types of Naive Bayes

### 1. Gaussian Naive Bayes
- Used for **continuous data**
- Assumes data follows **normal distribution**

---

### 2. Multinomial Naive Bayes
- Used for **text classification**
- Works on **word counts / frequency**

---

### 3. Bernoulli Naive Bayes
- Used for **binary features (0/1)**
- Example: word present or not

---

## 🔹 Advantages

✅ Fast and efficient  
✅ Works well with small datasets  
✅ Performs great in **text classification**  
✅ Handles high dimensional data well  

---

## 🔹 Disadvantages

❌ Assumes feature independence (not realistic)  
❌ Zero probability problem  
❌ Less accurate than complex models sometimes  

---

## 🔹 Zero Probability Problem

If a feature never appeared in training for a class → probability becomes 0

👉 Solution:
- Use **Laplace Smoothing**

---

## 🔹 Applications

- Spam detection 📧  
- Sentiment analysis 😊😡  
- Document classification 📄  
- Medical diagnosis 🏥  

---

## 🔹 When to Use

✔ Text data (NLP tasks)  
✔ High dimensional datasets  
✔ Fast predictions needed  

---

## 🔹 When NOT to Use

❌ When features are highly dependent  
❌ Complex relationships in data  

---

## 🔹 Example Code (Scikit-Learn)

```python
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
nb = GaussianNB()
nb.fit(X_train, y_train)

# Prediction
y_pred = nb.predict(X_test)

# Accuracy
print(accuracy_score(y_test, y_pred))