from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import pickle
import joblib
import numpy as np
import pandas as pd

# Initialize FastAPI
app = FastAPI()

# Templates & Static Files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Shared Data
USER_DATA = {
    "name": "Deepak Kumar",
    "role": "Aspiring Data Scientist & ML Engineer",
    "github": "https://github.com/dpk45deepak",
}

# --- 1. LOAD MACHINE LEARNING MODELS ---

# Linear Regression Model
try:
    lr_model = pickle.load(open('../../models/LinearRegression/simple_linear_regression_model.pkl', 'rb'))
except FileNotFoundError:
    lr_model = None

# Naive Bayes Model
try:
    nb_model = pickle.load(open('../../models/NaiveBayes/naive_bayes_model.pkl', 'rb'))
except FileNotFoundError:
    nb_model = None

# KNN Model
try:
    knn_model = joblib.load('../../models/KNN/knn_model.pkl')
except FileNotFoundError:
    knn_model = None

# Decision Tree Model
try:
    dt_model = joblib.load('../../models/DecisionTree/decision_tree_model.joblib')
except FileNotFoundError:
    dt_model = None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    projects = [
        {"title": "Crop Recommendation System", "desc": "ML model to suggest best crop based on soil data", "tech": "ML, FastAPI, NumPy"},
        {"title": "Trip Recommendation System", "desc": "Personalized travel recommendations", "tech": "ML, React, FastAPI"},
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={**USER_DATA, "projects": projects}
    )


# --- 2. MODEL LAB ROUTING ---

# Redirect general /lab to the first model
@app.get("/lab")
async def lab_redirect():
    return RedirectResponse(url="/lab/lr")

@app.get("/lab/{model_id}", response_class=HTMLResponse)
async def model_lab(request: Request, model_id: str):
    """Renders the lab page dynamically based on the selected model."""
    if model_id not in ["lr", "nb", "knn", "dt"]:
        return RedirectResponse(url="/lab/lr")

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html", 
        context={**USER_DATA, "active_model": model_id, "prediction": None}
    )

# --- 3. PREDICTION ENDPOINTS ---

@app.post("/predict/lr", response_class=HTMLResponse)
async def predict_lr(request: Request, weight: float = Form(...)):
    if lr_model:
        pred_val = lr_model.predict([[weight]])[0]
    else:
        pred_val = (weight * 0.9) + 110 # Fallback mock

    prediction = f"{pred_val:.2f} cm"

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html", 
        context={"request": request, **USER_DATA, "active_model": "lr", "prediction": prediction, "prev_inputs": {"weight": weight}}
    )

@app.post("/predict/nb", response_class=HTMLResponse)
async def predict_nb(
    request: Request, 
    total_bill: float = Form(...), 
    tip: float = Form(...), 
    size: int = Form(...),
    sex: str = Form(...),
    smoker: str = Form(...),
    day: str = Form(...)
):
    sex_Male = 1 if sex == "Male" else 0
    smoker_Yes = 1 if smoker == "Yes" else 0
    day_Sat = 1 if day == "Sat" else 0
    day_Sun = 1 if day == "Sun" else 0
    day_Thur = 1 if day == "Thur" else 0

    if nb_model:
        sample_df = pd.DataFrame([{
            'total_bill': total_bill, 'tip': tip, 'size': size,
            'sex_Male': sex_Male, 'smoker_Yes': smoker_Yes,
            'day_Sat': day_Sat, 'day_Sun': day_Sun, 'day_Thur': day_Thur
        }])
        pred_val = nb_model.predict(sample_df)[0]
    else:
        pred_val = "Dinner" if total_bill > 20 else "Lunch" # Fallback mock

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html", 
        context={"request": request, **USER_DATA, "active_model": "nb", "prediction": str(pred_val).capitalize(), "prev_inputs": {"total_bill": total_bill, "tip": tip, "size": size, "sex": sex, "smoker": smoker, "day": day}}
    )

@app.post("/predict/knn", response_class=HTMLResponse)
async def predict_knn(
    request: Request,
    feature1: float = Form(...),
    feature2: float = Form(...),
    feature3: float = Form(...)
):
    if knn_model:
        input_values = np.array([[feature1, feature2, feature3]])
        pred_val = knn_model.predict(input_values)[0]
    else:
        pred_val = "Class A" if feature1 > 0 else "Class B" # Fallback mock

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html", 
        context={"request": request, **USER_DATA, "active_model": "knn", "prediction": str(pred_val), "prev_inputs": {"feature1": feature1, "feature2": feature2, "feature3": feature3}}
    )

@app.post("/predict/dt", response_class=HTMLResponse)
async def predict_dt(
    request: Request,
    feature1: float = Form(...),
    feature2: float = Form(...),
    feature3: float = Form(...),
    feature4: float = Form(...)
):
    if dt_model:
        input_values = np.array([[feature1, feature2, feature3, feature4]])
        pred_val = dt_model.predict(input_values)[0]
    else:
        pred_val = "Setosa" if feature1 < 5 else "Versicolor" # Fallback mock

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html",
        context={"request": request, **USER_DATA, "active_model": "dt", "prediction": str(pred_val), "prev_inputs": {"feature1": feature1, "feature2": feature2, "feature3": feature3, "feature4": feature4}}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)