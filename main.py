import joblib
import pandas as pd
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
# --- NEW IMPORTS ---
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# --- 1. Define Input Data Model ---
class AirfareFeatures(BaseModel):
    nsmiles: float = Field(..., example=1589.0)
    passengers: float = Field(..., example=229.0)
    large_ms: float = Field(..., example=0.6179)
    lf_ms: float = Field(..., example=0.3444)
    competition_ratio: float = Field(..., example=1.794)
    Year: int = Field(..., example=2023)
    quarter: int = Field(..., example=3)
    carrier_lg: str = Field(..., example="AA")
    carrier_low: str = Field(..., example="DL")
    airport_1: str = Field(..., example="JFK")
    airport_2: str = Field(..., example="LAX")
    route: str = Field(..., example="JFK_LAX")
    year_quarter: str = Field(..., example="2023_Q3")

# --- 2. Define Output Data Model ---
class PredictionOut(BaseModel):
    predicted_fare: float

# --- 3. Create FastAPI app ---
app = FastAPI(
    title="Airfare Price Prediction API",
    description="API for predicting U.S. airfare using an XGBoost model."
)

# --- 4. Add CORS Middleware ---
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- NEW: MOUNT STATIC FILES ---
# This tells FastAPI to look inside a folder named 'static' for your HTML/CSS/JS
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# --- 5. Load the Model ---
try:
    model = joblib.load('airfare_model_pipeline.joblib')
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    print("❌ ERROR: 'airfare_model_pipeline.joblib' not found.")
    model = None

# --- 6. Updated Endpoints ---

# CHANGE: This now serves your index.html file
@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        with open("static/index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return """
        <h1>SkyCast API is Running</h1>
        <p>But <b>static/index.html</b> was not found. 
        Create a 'static' folder and put your HTML there!</p>
        """

@app.post("/predict", response_model=PredictionOut)
def predict_fare(features: AirfareFeatures):
    if model is None:
        return {"error": "Model not loaded. Please check server logs."}

    input_data = pd.DataFrame([features.model_dump()])
    prediction = model.predict(input_data)[0]
    
    return {"predicted_fare": round(float(prediction), 2)}