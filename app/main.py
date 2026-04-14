from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from app.services.file_service import save_file, load_dataframe
from app.services.ml_service import analyze_data, train_model, predict
from app.models.schemas import PredictRequest

app = FastAPI(title="AutoML API")

# Add CORS middleware to allow Streamlit to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    try:
        file_id, df = await save_file(file)
        return {
            "file_id": file_id,
            "columns": list(df.columns),
            "preview": df.head().to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/analyze/{file_id}")
def analyze(file_id: str):
    try:
        df = load_dataframe(file_id)
        return analyze_data(df)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

@app.post("/train/{file_id}")
def train(file_id: str, target: str):
    try:
        df = load_dataframe(file_id)
        return train_model(df, file_id, target)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/data/{file_id}")
def get_data(file_id: str):
    try:
        df = load_dataframe(file_id)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

@app.post("/predict/{file_id}")
def predict_api(file_id: str, request: PredictRequest):
    try:
        result = predict(file_id, request.data)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)