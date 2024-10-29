import uvicorn
import os
from src.app import app

def start_server():
    uvicorn.run(app, host=os.getenv('APP_HOST', "localhost"), port=int(os.getenv('APP_PORT', 8080)))

if __name__ == "__main__":
    start_server()
