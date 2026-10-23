from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInterests(BaseModel):
    user_id: int
    interests: list[str]

# Temporary storage
users = {}

@app.post("/save-interests")
def save_interests(data: UserInterests):

    users[data.user_id] = data.interests

    return {
        "message": "Interests saved!",
        "interests": data.interests
    }
