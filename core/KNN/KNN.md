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

## 🔍 Variants of K-Nearest Neighbors (KNN)

KNN is simple but can become **slow** when the dataset grows large because it calculates distance with *every point*.  
To solve this, optimized data structures like **KD-Tree** and **Ball Tree** are used.

---

## 🌳 1. KD-Tree (K-Dimensional Tree)

### 📌 Definition
A **KD-Tree** is a space-partitioning data structure used to organize points in a k-dimensional space.  
It helps in reducing the number of distance calculations.

### ⚙️ How it Works
- The dataset is recursively split into two halves.
- Each split is based on one feature (dimension).
- It forms a **binary tree** structure.
- At each level, a different dimension is used for splitting.

### 🧠 Intuition
Instead of checking all points:
👉 KD-Tree eliminates large portions of data that are far away.

### ✅ Advantages
- Faster than brute-force KNN for **low-dimensional data**
- Efficient search using tree traversal
- Reduces time complexity significantly

### ❌ Disadvantages
- Performance drops in **high-dimensional data** (curse of dimensionality)
- Tree balancing can be costly

### ⏱️ Complexity
- Build Time: `O(n log n)`
- Query Time: `O(log n)` (average)

---

## ⚽ 2. Ball Tree

### 📌 Definition
A **Ball Tree** partitions data into nested hyperspheres (balls) instead of splitting by axis like KD-Tree.

### ⚙️ How it Works
- Data is divided into clusters (balls)
- Each node contains a **center point and radius**
- Points inside a ball are grouped together
- Search eliminates entire balls if they are far from the query point

### 🧠 Intuition
Instead of splitting space into boxes (like KD-Tree):
👉 Ball Tree groups nearby points into circular regions

### ✅ Advantages
- Works better for **high-dimensional data**
- More flexible than KD-Tree
- Efficient for complex datasets

### ❌ Disadvantages
- Slightly more complex to implement
- Slower than KD-Tree in low dimensions

### ⏱️ Complexity
- Build Time: `O(n log n)`
- Query Time: `O(log n)` (average)

---

## ⚔️ KD-Tree vs Ball Tree

| Feature     | KD-Tree 🌳           | Ball Tree ⚽          |
| ----------- | ------------------- | -------------------- |
| Structure   | Axis-aligned splits | Hypersphere clusters |
| Best for    | Low dimensions      | High dimensions      |
| Speed       | Faster (low dim)    | Faster (high dim)    |
| Flexibility | Less flexible       | More flexible        |
| Complexity  | Simpler             | Slightly complex     |

---

## 🧠 When to Use What?

- Use **KD-Tree** 👉 when features are **less (≤ 10-15 dimensions)**
- Use **Ball Tree** 👉 when data is **high-dimensional or complex**
- Use **Brute Force** 👉 when dataset is **small**

---

## 💻 Implementation in Scikit-Learn

```python
from sklearn.neighbors import KNeighborsClassifier

# Using KD-Tree
knn_kd = KNeighborsClassifier(algorithm='kd_tree')
knn_kd.fit(X_train, y_train)

# Using Ball Tree
knn_ball = KNeighborsClassifier(algorithm='ball_tree')
knn_ball.fit(X_train, y_train)

# Auto (chooses best)
knn_auto = KNeighborsClassifier(algorithm='auto')
knn_auto.fit(X_train, y_train)
```