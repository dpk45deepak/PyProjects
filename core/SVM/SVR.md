# 📗 Support Vector Regression (SVR) — Complete Notes

---

## 🧠 1. Introduction

Support Vector Regression (SVR) is the regression version of SVM.

👉 Instead of classifying data, SVR predicts **continuous values**.

**Goal:**
Fit a function that has **at most ε deviation** from actual values while keeping the model as flat as possible.

---

## 📊 2. Key Idea

Unlike linear regression (which minimizes error directly),

👉 SVR tries to:
- Ignore small errors (within a threshold)
- Penalize only large errors

---

## 📐 3. SVR Function

f(x) = w^T x + b

Where:
- w = weights
- b = bias

---

## 📏 4. ε (Epsilon) — Tube Concept

SVR introduces a margin (called ε-tube):

- Predictions within ε distance → **no penalty**
- Outside ε → **penalty applied**

👉 This creates a "tube" around the regression line.

---

## 🔥 5. Loss Function (ε-insensitive loss)

max(0, |y - f(x)| - ε)

---

## 🧠 6. Interpretation

| Condition | Meaning  | Loss |
| --------- | -------- | ---- |
|           | y - f(x) | ≤ ε  | Acceptable error | 0         |
|           | y - f(x) | > ε  | Large error      | Penalized |

---

## ⭐ 7. Support Vectors in SVR

Support vectors are:

👉 Points **outside the ε-tube**

These points influence the regression line.

---

## ⚙️ 8. Optimization Objective

Minimize:

1/2 ||w||² + C Σ ξ

Where:
- ξ = error outside ε
- C = regularization parameter

---

## 🎯 9. Role of C

- Large C → tries to fit data closely (less tolerance)
- Small C → allows more flexibility (smoother curve)

---

## 🔄 10. Kernel Trick in SVR

Same as SVM, used for non-linear regression.

### Common Kernels:

- Linear
- Polynomial
- RBF (most used)
- Sigmoid

---

## 📊 11. Types of SVR

- Linear SVR
- Non-linear SVR (using kernels)

---

## ⚡ 12. Advantages

- Works well for non-linear data
- Robust to outliers (due to ε)
- Flexible using kernels

---

## ⚠️ 13. Disadvantages

- Hard to tune parameters (C, ε, gamma)
- Slow for large datasets
- Sensitive to feature scaling

---

## 🧪 14. Implementation (Python)

```python
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import numpy as np

# Dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 1.8, 3.0, 3.8, 5.1])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = SVR(kernel='rbf', C=1.0, epsilon=0.1)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

```

### 📈 15. Hyperparameters
- C → Regularization
- kernel → Type of boundary
- gamma → Influence of points
- degree → For polynomial kernel