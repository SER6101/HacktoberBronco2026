from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from database import save_questionnaire

app = FastAPI(title="Personal Hobby Discovery")

questions = [
    {
        "id": 1,
        "question": "What do you hope to gain from a hobby?",
        "options": [
            "Relaxation",
            "Learning",
            "Fitness",
            "Creativity"
        ]
    },
    {
        "id": 2,
        "question": "What activities do you enjoy?",
        "options": [
            "Creating",
            "Exploring",
            "Problem solving",
            "Physical activities"
        ]
    },
    {
        "id": 3,
        "question": "How do you prefer spending free time?",
        "options": [
            "Alone",
            "Small group",
            "Meeting people",
            "Either"
        ]
    },
    {
        "id": 4,
        "question": "What is your starting budget?",
        "options": [
            "Free",
            "Under $25",
            "$25-$100",
            "Over $100"
        ]
    },
    {
        "id": 5,
        "question": "How much time do you have each week?",
        "options": [
            "Under 2 hours",
            "2-5 hours",
            "5-10 hours",
            "Over 10 hours"
        ]
    }
]

# Hobby catalog with preferences and requirements
hobbies = [
    {
        "name": "Drawing",
        "goals": ["Relaxation", "Creativity"],
        "activities": ["Creating"],
        "social": ["Alone", "Either"],
        "cost": 0,
        "hours": 1,
        "description": "Express yourself through sketches and art."
    },
    {
        "name": "Hiking",
        "goals": ["Fitness", "Relaxation"],
        "activities": ["Exploring", "Physical activities"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Explore nature and stay physically active."
    },
    {
        "name": "Coding",
        "goals": ["Learning", "Creativity"],
        "activities": ["Problem solving", "Creating"],
        "social": ["Alone", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Build small projects and learn programming."
    },
    {
        "name": "Cooking",
        "goals": ["Learning", "Creativity"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 25,
        "hours": 2,
        "description": "Experiment with recipes and flavors."
    },
    {
        "name": "Yoga",
        "goals": ["Relaxation", "Fitness"],
        "activities": ["Physical activities"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 1,
        "description": "Improve flexibility and practice mindfulness."
    },
    {
        "name": "Photography",
        "goals": ["Creativity", "Learning"],
        "activities": ["Exploring", "Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 25,
        "hours": 2,
        "description": "Capture interesting moments using a camera or phone."
    }
]


class Questionnaire(BaseModel):
    answers: list[str]


@app.get("/")
def home():
    return {"message": "Welcome to Personal Hobby Discovery"}


@app.get("/questions")
def get_questions():
    return {"questions": questions}


@app.post("/recommend")
def recommend(data: Questionnaire):

    if len(data.answers) != 5:
        raise HTTPException(
            status_code=400,
            detail="Please answer all five questions."
        )

    for index, answer in enumerate(data.answers):
        if answer not in questions[index]["options"]:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid answer for question {index + 1}"
            )

    goal, activity, social, budget, time = data.answers

    budget_limits = {
        "Free": 0,
        "Under $25": 25,
        "$25-$100": 100,
        "Over $100": float("inf")
    }

    time_limits = {
        "Under 2 hours": 2,
        "2-5 hours": 5,
        "5-10 hours": 10,
        "Over 10 hours": float("inf")
    }

    recommendations = []

    for hobby in hobbies:

        # Filter out hobbies that exceed constraints
        if hobby["cost"] > budget_limits[budget]:
            continue

        if hobby["hours"] > time_limits[time]:
            continue

        score = 0

        if goal in hobby["goals"]:
            score += 3

        if activity in hobby["activities"]:
            score += 2

        if social in hobby["social"]:
            score += 2

        recommendations.append({
            "hobby": hobby["name"],
            "score": score,
            "description": hobby["description"],
            "estimated_cost": hobby["cost"],
            "hours_per_week": hobby["hours"]
        })

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    top_recommendations = recommendations[:3]

    response_id = str(uuid4())

    save_questionnaire(
        response_id=response_id,
        answers=data.answers,
        recommendations=top_recommendations
    )

    return {
        "response_id": response_id,
        "message": "Questionnaire saved successfully",
        "recommendations": top_recommendations
    }
