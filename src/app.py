from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os
from src.chain import create_chain
from langserve import add_routes


app = FastAPI(
  title="ePhysician LLM Service",
  version="1.0",
  description="Physician helper service which provides diagnose suggestions based on patient profile and symptoms",
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, create_chain(), path="/diagnose")
