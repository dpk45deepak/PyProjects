# 🌳 Decision Tree - Complete Guide (Beginner to Advanced)

## 📌 1. What is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm used for both **Classification** (predicting labels) and **Regression** (predicting continuous values). It mimics human decision-making by splitting data based on feature conditions.



### The Structure:
*   **Root Node:** The starting point representing the entire population.
*   **Decision Node:** A sub-node that splits into further branches based on a condition.
*   **Leaf Node:** The final output node where no further splitting occurs.
*   **Branches:** The path connecting nodes (the "if-then" logic).

---

## 🎯 2. Why Use Decision Trees?

| Pros                                                                | Cons                                                              |
| :------------------------------------------------------------------ | :---------------------------------------------------------------- |
| **Easy to interpret:** "White-box" model where logic is visible.    | **Overfitting:** High tendency to memorize training noise.        |
| **No scaling needed:** Works without normalizing data.              | **Instability:** Small changes in data can change the whole tree. |
| **Handles Non-linearity:** Excellent at capturing complex patterns. | **Bias:** Can be biased if one class dominates.                   |

---

## 📊 3. Splitting Criteria (The Math)

The goal of a split is to maximize **homogeneity** (purity) in the child nodes.

### 🔹 1. Gini Impurity
Used primarily by the CART algorithm for classification. It measures the probability of a random element being misclassified.

$$Gini = 1 - \sum_{i=1}^{n} (p_i)^2$$
*   **Range:** 0 (Pure) to 0.5 (Maximum impurity for 2 classes).

### 🔹 2. Entropy & Information Gain
Measures the "disorder" in the data. Information Gain is the reduction in entropy after a split.

$$Entropy(S) = - \sum_{i=1}^{n} p_i \log_2(p_i)$$

### 🔹 2.5 Information Gain
$$Information Gain (I.G) = Entropy(Parent) - \sum_{i=1}^{k} \frac{|S_i|}{|S|} Entropy(S_i)$$

****Select the higher Information Gain features as root nodes.****

### 🔹 3. Variance Reduction (Regression)
Used for continuous targets. The split that results in the lowest weighted Variance/MSE is chosen.

### 🔹Mean Squared Error (Regression)
Used for continuous targets. The split minimizes the variance within the nodes.
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y})^2$$
---

## ⚠️ 4. Overfitting & Pruning

If left unchecked, a Decision Tree will create a leaf for every single data point. We prevent this using **Pruning**.

### 🛠 Hyperparameter Tuning (Pre-Pruning)
*   `max_depth`: Limits the vertical growth of the tree.
*   `min_samples_split`: Minimum samples needed in a node before it can split.
*   `min_samples_leaf`: Minimum samples required to exist at a leaf node.

---

## 🧪 5. Implementation (Python - Scikit-Learn)
```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model with Constraints (Pre-pruning)
model = DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_leaf=5)
model.fit(X_train, y_train)

# 4. Visualize
plt.figure(figsize=(15,10))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()

```
---

## 🔢 4. Handling Numerical Features
Numerical features are handled by finding the **optimal binary split point**:
1.  **Sort:** The feature values are sorted in ascending order.
2.  **Midpoints:** Midpoints between adjacent values are calculated as potential "thresholds."
3.  **Test:** Each threshold (e.g., `Income <= 50k`) is tested using the splitting criteria (Gini/Entropy).
4.  **Select:** The threshold that yields the highest Information Gain is chosen as the split.

---

## ✂️ 5. Pruning: Preventing Overfitting
Decision trees naturally grow until they memorize the noise in the data (Overfitting). Pruning trims the tree back.

### 🔹 A. Pre-Pruning (Early Stopping)
Set constraints **before** the tree finishes growing:
*   `max_depth`: Limits how many levels the tree can have.
*   `min_samples_split`: Minimum samples a node must have to be allowed to split.
*   `min_samples_leaf`: Minimum samples a leaf node must contain.

### 🔹 B. Post-Pruning (Cost Complexity Pruning)
The tree grows to full size, then "weak" branches are removed. This uses a parameter **Alpha ($\alpha$)** to balance tree size and accuracy:
$$R_\alpha(T) = R(T) + \alpha|T|$$
*   **$R(T)$**: Training error of the tree.
*   **$|T|$**: Number of leaf nodes.
*   **$\alpha$**: The penalty for complexity. High $\alpha$ = Smaller, simpler trees.

---

## 🧪 6. Python Implementation (Scikit-Learn)
```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# 1. Load and Split Data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# 2. Train with Pre-Pruning
model = DecisionTreeClassifier(
    criterion='gini', 
    max_depth=4, 
    min_samples_leaf=5,
    ccp_alpha=0.01 # Example of Post-Pruning parameter
)
model.fit(X_train, y_train)

# 3. Visualization
plt.figure(figsize=(12,8))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
```