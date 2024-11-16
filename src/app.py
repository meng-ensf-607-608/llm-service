from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.llm_chain import create_chain
from langserve import add_routes
from src.config import MODEL_TYPE_GEMINI
from src.data_models import PatientInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="ePhysician LLM Service",
  version="1.0",
  description="Physician helper service which provides diagnose suggestions based on patient profile and symptoms",
)

origins = [
    "http://localhost:4200",
    "http://localhost:8080",
    "https://physician-assistant-database-service-38696173603.us-central1.run.app",
    "https://app.algohelios.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, create_chain(MODEL_TYPE_GEMINI), path="/diagnose", input_type=PatientInput)
