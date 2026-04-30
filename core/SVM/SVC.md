# 📘 Support Vector Machine (SVM) — Complete Notes

---

## 🧠 1. Introduction

Support Vector Machine (SVM) is a **supervised machine learning algorithm** used for:

- Classification
- Regression (SVR)
- Outlier detection

**Goal:**
Find the optimal hyperplane that separates classes with maximum margin.

---

## 📊 2. Hyperplane

A hyperplane is a decision boundary.

- 2D → Line  
- 3D → Plane  
- n-D → Hyperplane  

**Equation:**

w^T x + b = 0

Where:
- w = weights
- x = features
- b = bias

---

## 📏 3. Margin

Margin = distance between hyperplane and closest points.

**Goal:**
Maximize margin for better generalization.

---

## ⭐ 4. Support Vectors

Support vectors are the closest data points to the decision boundary.

They determine the position of the hyperplane.

---

## 📐 5. Why +1 and -1?

Labels are defined as:

y ∈ {+1, -1}

We scale the model such that:

w^T x + b = +1 → positive class  
w^T x + b = -1 → negative class  

This is done for **mathematical normalization**.

---

## 📊 6. Constraint

y_i (w^T x_i + b) ≥ 1

Ensures:
- Correct classification
- Minimum margin maintained

---

## ⚙️ 7. Optimization Objective

Minimize:

1/2 ||w||²

Subject to:

y_i (w^T x_i + b) ≥ 1

---

## 🔥 8. Hinge Loss

Formula:

max(0, 1 - y(w^T x + b))

### Interpretation:

- If y(wx + b) ≥ 1 → Loss = 0 (correct & confident)
- If 0 < y(wx + b) < 1 → small loss
- If y(wx + b) ≤ 0 → large loss (wrong prediction)

---

## 🧩 9. Hard Margin vs Soft Margin

### Hard Margin
- No misclassification allowed
- Only for perfectly separable data

### Soft Margin
- Allows errors
- Uses regularization parameter C

---

## 🎯 10. Regularization (C)

- Large C → low error, small margin (overfitting)
- Small C → more error, large margin (better generalization)

---

## 🔄 11. Kernel Trick

Used when data is not linearly separable.

Transforms data into higher dimensions.

---

### Common Kernels:

- Linear: x^T x'
- Polynomial: (x^T x' + 1)^d
- RBF: exp(-γ||x - x'||²)
- Sigmoid: tanh(x^T x')

---

## ⚡ 12. Advantages

- Works in high dimensions
- Effective with small datasets
- Memory efficient
- Strong theoretical foundation

---

## ⚠️ 13. Disadvantages

- Slow for large datasets
- Hard to tune
- Sensitive to noise
- Less interpretable

---

## 🧪 14. Implementation (Python)

```python
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = SVC(kernel='rbf', C=1.0, gamma='scale')

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


```

### 📈 15. Hyperparameters
- C → Regularization
- kernel → Type of boundary
- gamma → Influence of points
- degree → For polynomial kernel