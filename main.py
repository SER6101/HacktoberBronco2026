from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4

app = FastAPI()

# Interest categories displayed on the frontend
categories = [
    "Gaming",
    "Music",
    "Sports",
    "Technology",
    "Fashion",
    "Art",
    "Food",
    "Travel"
]

# Temporary storage
user_interests = {}


# Structure of data sent by the frontend
class InterestSelection(BaseModel):
    interests: list[str] = Field(min_length=1)


# Homepage
@app.get("/")
def home():
    return {"message": "Interest Questionnaire API"}


# Send available interests to the frontend
@app.get("/interests")
def get_interests():
    return {"categories": categories}


# Save interests selected by a visitor
@app.post("/interests")
def save_interests(selection: InterestSelection):

    selected = list(dict.fromkeys(selection.interests))

    # Check that interests are valid
    for interest in selected:
        if interest not in categories:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid interest: {interest}"
            )

    # Generate an anonymous ID
    session_id = str(uuid4())

    # Store selections temporarily
    user_interests[session_id] = selected

    return {
        "message": "Interests saved successfully",
        "session_id": session_id,
        "interests": selected
    }


# Retrieve selections using the session ID
@app.get("/interests/{session_id}")
def get_saved_interests(session_id: str):

    if session_id not in user_interests:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return {
        "session_id": session_id,
        "interests": user_interests[session_id]
    }
