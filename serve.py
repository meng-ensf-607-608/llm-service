from fastapi import FastAPI
from langserve import add_routes
from fastapi.responses import RedirectResponse
import uvicorn
import os

from src.chain import create_chain


app = FastAPI(
  title="ePhysician LLM Service",
  version="1.0",
  description="Physician helper service which provides diagnose suggestions based on patient profile and symptoms",
)
    
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

gemini_version = os.getenv("GOOGLE_LLM_MODEL")


def configure_routes():
    add_routes(app, create_chain(gemini_version), path="/diagnose")

def start_server():
    uvicorn.run(app, host=os.getenv('APP_HOST', "localhost"), port=os.getenv('APP_PORT', 8080))

if __name__ == "__main__":
    configure_routes()
    start_server()
