from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks data
with open("marks.json", "r") as f:
    student_marks = json.load(f)  # Assuming marks are stored as {"name": marks}

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [student_marks.get(n, None) for n in name]  # Get marks for each name
    return {"marks": marks}
