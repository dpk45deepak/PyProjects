from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

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

@app.get("/health")
async def health(request: Request):
    return {
        "status": "OK",
        "msg": "Hello, Sir! this backend it working a s expected!!",
        "code": 200
    }

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

# --- MODEL LAB SECTION ---

@app.get("/lab", response_class=HTMLResponse)
async def model_lab(request: Request):
    """Initial view of the Model Lab page"""
    return templates.TemplateResponse(
        request=request,
        name="model_lab.html",
        context={**USER_DATA, "prediction": None}
    )

@app.get("/predict", response_class=HTMLResponse)
@app.post("/predict", response_class=HTMLResponse)
async def get_prediction(
    request: Request,
    sqft: int = Form(None),    # Changed to None so GET request doesn't crash
    beds: int = Form(None),
    year: int = Form(None),
    quality: int = Form(None)
):
    prediction = None
    
    # Only run ML logic if this is a POST request with data
    if request.method == "POST" and sqft is not None:
        # Your ML Logic
        mock_val = 50000 + (sqft * 150) + (beds * 10000) + (quality * 5000)
        prediction = f"{mock_val:,}"

    return templates.TemplateResponse(
        request=request,
        name="model_lab.html",
        context={
            **USER_DATA,
            "prediction": prediction,
            "prev_sqft": sqft,
            "prev_beds": beds,
            "prev_year": year,
            "prev_quality": quality
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)