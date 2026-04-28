# 📌 Hyperparameter Tuning

## 🔍 What are Hyperparameters?

Hyperparameters are the parameters that are set before training a machine learning model.  
They are not learned from the data but control the learning process.

### 🧠 Examples:
- Learning rate
- Number of trees (Random Forest)
- Depth of tree
- Number of neighbors (KNN)

---

## ⚙️ Why Hyperparameter Tuning is Important?

- Improves model performance  
- Reduces overfitting and underfitting  
- Helps find the best parameter combination  
- Increases model generalization  

---

## 🛠️ Common Hyperparameters

### 📌 Linear Regression
- `fit_intercept`
- `normalize`

### 📌 Decision Tree
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

### 📌 Random Forest
- `n_estimators`
- `max_depth`
- `max_features`

### 📌 KNN
- `n_neighbors`
- `weights`
- `metric`

---

## 🔄 Hyperparameter Tuning Methods

### 1️⃣ Grid Search

- Tries all possible combinations  
- Computationally expensive but accurate  

```python
from sklearn.model_selection import GridSearchCV