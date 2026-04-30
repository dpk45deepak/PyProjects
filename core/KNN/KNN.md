# 📌 K-Nearest Neighbors (KNN)

## 🔹 Definition
K-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used for both **classification** and **regression** tasks.  
It works by finding the **K closest data points (neighbors)** to a given input and making predictions based on them.

---

## 🔹 Intuition (Simple Understanding)
- Think of KNN as:  
  👉 "Tell me who your neighbors are, and I will tell you who you are."

- Example:
  - If most nearby points are **Red → classify as Red**
  - If most are **Blue → classify as Blue**

---

## 🔹 How KNN Works

1. Choose value of **K**
2. Calculate distance between new point and all training points
3. Select **K nearest neighbors**
4. Perform:
   - **Majority voting (Classification)**
   - **Average (Regression)**

---

## 🔹 Distance Metrics

### 1. Euclidean Distance (Most Common)
\[
d = \sqrt{\sum (x_i - y_i)^2}
\]

### 2. Manhattan Distance
\[
d = \sum |x_i - y_i|
\]

### 3. Minkowski Distance
General form of distance.

---

## 🔹 Types of KNN

### 1. KNN Classification
- Output: **Discrete label**
- Example: Spam or Not Spam

### 2. KNN Regression
- Output: **Continuous value**
- Example: Predict house price

---

## 🔹 Choosing Optimal K

- Small K → Overfitting
- Large K → Underfitting

👉 Use:
- Cross-validation
- Elbow method (trial and error)

---

## 🔹 Advantages

✅ Simple and easy to understand  
✅ No training phase (Lazy learner)  
✅ Works well with small datasets  

---

## 🔹 Disadvantages

❌ Slow for large datasets  
❌ Sensitive to noise  
❌ Requires feature scaling  

---

## 🔹 Feature Scaling Importance

KNN is distance-based, so scaling is **VERY IMPORTANT**

Use:
- StandardScaler
- MinMaxScaler

---

## 🔹 Variants of KNN

### 1. Weighted KNN
- Neighbors closer to the point have **more influence**
- Helps improve accuracy

---

### 2. KD-Tree Based KNN
- Uses tree structure to **speed up nearest neighbor search**
- Efficient for large datasets

---

### 3. Ball Tree KNN
- Alternative to KD-Tree
- Works better in **higher dimensions**

---

### 4. Radius Neighbors
- Instead of fixed K, uses a **distance radius**
- Includes all points within that radius

---

### 5. Approximate KNN
- Faster but slightly less accurate
- Used in large-scale applications

---

## 🔹 Real Life Applications

- Recommendation systems (Netflix, Amazon)
- Image classification
- Fraud detection
- Medical diagnosis

---

## 🔹 When to Use KNN

✔ Small datasets  
✔ Clear separation between classes  
✔ Low dimensional data  

---

## 🔹 When NOT to Use

❌ Large datasets  
❌ High dimensional data (Curse of Dimensionality)  
❌ Real-time prediction systems  

---

## 🔹 Example Code (Scikit-Learn)

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Evaluate
accuracy = knn.score(X_test, y_test)
print("Accuracy:", accuracy)
```