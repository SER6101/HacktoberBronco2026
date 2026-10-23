import random

from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from hobby import Hobby
from skateboarding import Skateboarding

from database import (
    init_db,
    save_questionnaire,
    get_completed_lessons,
    save_lesson_progress
)


app = FastAPI(
    title="HobBob",
    description="A personalized hobby discovery and learning app.",
    version="1.0.0"
)

# Initialize local SQLite storage
init_db()

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
    },
    {
        "name": "Skateboarding",
        "goals": ["Fitness", "Learning"],
        "activities": ["Physical activities"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 75,
        "hours": 3,
        "description": "Learn skateboard tricks, improve balance, and explore skateparks."
    },
    {
        "name": "Painting",
        "goals": ["Creativity", "Relaxation"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 30,
        "hours": 2,
        "description": "Create artwork using watercolors, acrylics, or other paints."
    },
    {
        "name": "Gardening",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Creating", "Exploring"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 20,
        "hours": 2,
        "description": "Grow plants, flowers, vegetables, and herbs."
    },
    {
        "name": "Reading",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Exploring"],
        "social": ["Alone", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Discover new stories, ideas, and knowledge through books."
    },
    {
        "name": "Creative Writing",
        "goals": ["Creativity", "Relaxation"],
        "activities": ["Creating"],
        "social": ["Alone", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Write short stories, poetry, or personal essays."
    },
    {
        "name": "Cycling",
        "goals": ["Fitness", "Relaxation"],
        "activities": ["Physical activities", "Exploring"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 100,
        "hours": 3,
        "description": "Explore your surroundings while improving endurance."
    },
    {
        "name": "Running",
        "goals": ["Fitness", "Relaxation"],
        "activities": ["Physical activities"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Improve stamina and enjoy outdoor exercise."
    },
    {
        "name": "Basketball",
        "goals": ["Fitness", "Learning"],
        "activities": ["Physical activities"],
        "social": ["Small group", "Meeting people", "Either"],
        "cost": 25,
        "hours": 3,
        "description": "Practice shooting, dribbling, and teamwork."
    },
    {
        "name": "Soccer",
        "goals": ["Fitness", "Learning"],
        "activities": ["Physical activities"],
        "social": ["Small group", "Meeting people", "Either"],
        "cost": 25,
        "hours": 3,
        "description": "Improve coordination, endurance, and teamwork."
    },
    {
        "name": "Swimming",
        "goals": ["Fitness", "Relaxation"],
        "activities": ["Physical activities"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 25,
        "hours": 2,
        "description": "Build endurance and enjoy exercise in the water."
    },
    {
        "name": "Dancing",
        "goals": ["Fitness", "Creativity"],
        "activities": ["Physical activities", "Creating"],
        "social": ["Alone", "Small group", "Meeting people", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Explore dance styles and express yourself through movement."
    },
    {
        "name": "Playing Guitar",
        "goals": ["Learning", "Creativity"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 100,
        "hours": 3,
        "description": "Learn chords, songs, and music composition."
    },
    {
        "name": "Playing Piano",
        "goals": ["Learning", "Creativity"],
        "activities": ["Creating", "Problem solving"],
        "social": ["Alone", "Either"],
        "cost": 100,
        "hours": 3,
        "description": "Learn musical techniques and play your favorite songs."
    },
    {
        "name": "Singing",
        "goals": ["Creativity", "Learning"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Meeting people", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Improve your voice and explore musical expression."
    },
    {
        "name": "Chess",
        "goals": ["Learning", "Relaxation"],
        "activities": ["Problem solving"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Develop strategic thinking through chess matches."
    },
    {
        "name": "Video Gaming",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Problem solving", "Exploring"],
        "social": ["Alone", "Small group", "Meeting people", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Explore different game genres and interactive worlds."
    },
    {
        "name": "Board Games",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Problem solving"],
        "social": ["Small group", "Meeting people", "Either"],
        "cost": 20,
        "hours": 2,
        "description": "Enjoy strategy and cooperative games with others."
    },
    {
        "name": "Pottery",
        "goals": ["Creativity", "Relaxation"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 50,
        "hours": 2,
        "description": "Create decorative or functional objects using clay."
    },
    {
        "name": "Knitting",
        "goals": ["Relaxation", "Creativity"],
        "activities": ["Creating"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 15,
        "hours": 2,
        "description": "Create scarves, clothing, and handmade accessories."
    },
    {
        "name": "Birdwatching",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Exploring"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 2,
        "description": "Observe birds and learn about local wildlife."
    },
    {
        "name": "Camping",
        "goals": ["Relaxation", "Learning"],
        "activities": ["Exploring"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 100,
        "hours": 10,
        "description": "Spend time outdoors and learn basic camping skills."
    },
    {
        "name": "Rock Climbing",
        "goals": ["Fitness", "Learning"],
        "activities": ["Physical activities", "Problem solving"],
        "social": ["Alone", "Small group", "Meeting people", "Either"],
        "cost": 50,
        "hours": 3,
        "description": "Develop strength and problem-solving skills through climbing."
    },
    {
        "name": "Origami",
        "goals": ["Creativity", "Relaxation"],
        "activities": ["Creating", "Problem solving"],
        "social": ["Alone", "Small group", "Either"],
        "cost": 0,
        "hours": 1,
        "description": "Create paper sculptures through folding techniques."
    },
    {
        "name": "Learning a Language",
        "goals": ["Learning", "Creativity"],
        "activities": ["Problem solving", "Exploring"],
        "social": ["Alone", "Small group", "Meeting people", "Either"],
        "cost": 0,
        "hours": 3,
        "description": "Explore new languages and cultures through practice."
    }
]


# Hobby Page Object

hobby_pages = {}

for hobby_data in hobbies:
    name = hobby_data["name"]

    if name == "Skateboarding":
        hobby_pages[name.lower()] = Skateboarding()
    else:
        hobby_pages[name.lower()] = Hobby(
            name=name,
            description=hobby_data["description"]
        )


# Request Model

class Questionnaire(BaseModel):
    answers: list[str]


class SkillSelection(BaseModel):
    session_id: str = Field(min_length=1)
    skill: str


class LessonCompletion(BaseModel):
    session_id: str = Field(min_length=1)
    skill: str
    lesson_number: int = Field(ge=1, le=10)
    reading_finished: bool = False
    video_finished: bool = False


class AchievementRequest(BaseModel):
    session_id: str = Field(min_length=1)
    skill: str
    completed_quests: list[int] = Field(default_factory=list)


# Helper Function

def find_hobby(hobby_name):
    hobby = hobby_pages.get(hobby_name.lower())

    if hobby is None:
        raise HTTPException(
            status_code=404,
            detail="Hobby not found"
        )

    return hobby


def validate_hobby_skill(hobby, skill):
    if skill not in hobby.skill_levels:
        raise HTTPException(
            status_code=400,
            detail="Invalid skill level"
        )


def validate_hobby_lessons(hobby):
    if len(hobby.lessons) != hobby.total_lessons:
        raise HTTPException(
            status_code=409,
            detail="This hobby does not have 10 lessons yet"
        )


# Home

@app.get("/")
def home():
    return {
        "message": "Welcome to HobBob",
        "description": "Discover and learn new hobbies!"
    }


# Questionaire

@app.get("/questions")
def get_questions():
    return {
        "questions": questions
    }


# Hobby Recommendation

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

    # Top 3 personalized recommendations
    top_recommendations = recommendations[:3]

    selected_names = {
        item["hobby"] for item in top_recommendations
    }

    # Random recommendation from eligible hobbies
    remaining_hobbies = [
        hobby for hobby in hobbies
        if hobby["name"] not in selected_names
        and hobby["cost"] <= budget_limits[budget]
        and hobby["hours"] <= time_limits[time]
    ]

    random_hobby = None

    if remaining_hobbies:
        random_choice = random.choice(remaining_hobbies)

        random_hobby = {
            "hobby": random_choice["name"],
            "description": random_choice["description"],
            "estimated_cost": random_choice["cost"],
            "hours_per_week": random_choice["hours"]
        }

    response_id = str(uuid4())

    # Save questionnaire in SQLite
    save_questionnaire(
        response_id=response_id,
        answers=data.answers,
        recommendations={
            "personalized": top_recommendations,
            "random": random_hobby
        }
    )

    return {
        "response_id": response_id,
        "recommendations": {
            "personalized": top_recommendations,
            "random": random_hobby,
            "explore_more": {
                "label": "Explore More Hobbies",
                "endpoint": "/hobbies"
            }
        }
    }


# Explore All Hobbies

@app.get("/hobbies")
def get_all_hobbies():

    return {
        "hobbies": [
            {
                "hobby": hobby["name"],
                "description": hobby["description"],
                "estimated_cost": hobby["cost"],
                "hours_per_week": hobby["hours"]
            }
            for hobby in hobbies
        ]
    }


# Hobby Information

@app.get("/hobby/{hobby_name}")
def get_hobby_info(hobby_name: str):

    hobby = find_hobby(hobby_name)

    return {
        "name": hobby.name,
        "description": hobby.description,
        "skill_levels": hobby.skill_levels,
        "total_lessons": hobby.total_lessons,
        "starting_lessons": hobby.starting_lessons,
        "lessons_available": (
            len(hobby.lessons) == hobby.total_lessons
        )
    }


# First Time Visit Selection

@app.post("/hobby/{hobby_name}/select-skill")
def select_skill(
    hobby_name: str,
    data: SkillSelection
):

    hobby = find_hobby(hobby_name)

    validate_hobby_skill(hobby, data.skill)
    validate_hobby_lessons(hobby)

    # Retrieve saved progress from SQLite
    completed_lessons = get_completed_lessons(
        data.session_id,
        hobby.name,
        data.skill
    )

    all_completed = hobby.get_all_completed_lessons(
        data.skill,
        completed_lessons
    )

    # Generate main page with roadmap and sidebar
    page = hobby.get_main_page(
        skill=data.skill,
        completed_lessons=completed_lessons,
        completed_quests=[]
    )

    return {
        "hobby": hobby.name,
        "skill": data.skill,
        "starting_lesson": hobby.get_starting_lesson(
            data.skill
        ),
        "completed_lessons": all_completed,
        "page": page
    }


# Get Specific Lesson

@app.get("/hobby/{hobby_name}/lesson/{lesson_number}")
def get_lesson(
    hobby_name: str,
    lesson_number: int,
    skill: str,
    session_id: str
):

    hobby = find_hobby(hobby_name)

    validate_hobby_skill(hobby, skill)
    validate_hobby_lessons(hobby)

    if not 1 <= lesson_number <= hobby.total_lessons:
        raise HTTPException(
            status_code=400,
            detail="Invalid lesson number"
        )

    completed_lessons = get_completed_lessons(
        session_id,
        hobby.name,
        skill
    )

    if not hobby.is_lesson_unlocked(
        skill,
        lesson_number,
        completed_lessons
    ):
        raise HTTPException(
            status_code=403,
            detail="Lesson is locked"
        )

    return {
        "hobby": hobby.name,
        "skill": skill,
        "lesson_number": lesson_number,
        "lesson": hobby.get_lesson(lesson_number),
        "status": hobby.get_lesson_status(
            skill,
            lesson_number,
            completed_lessons
        ),
        "previous_unlocked": hobby.can_go_previous(
            skill,
            lesson_number
        ),
        "next_unlocked": hobby.can_go_next(
            skill,
            lesson_number,
            completed_lessons
        )
    }


# Complete Lesson

@app.post("/hobby/{hobby_name}/complete-lesson")
def complete_lesson(
    hobby_name: str,
    data: LessonCompletion
):

    hobby = find_hobby(hobby_name)

    validate_hobby_skill(hobby, data.skill)
    validate_hobby_lessons(hobby)

    completed_lessons = get_completed_lessons(
        data.session_id,
        hobby.name,
        data.skill
    )

    # Include automatically completed lessons
    all_completed = hobby.get_all_completed_lessons(
        data.skill,
        completed_lessons
    )

    # Previously completed lessons stay unlocked
    if data.lesson_number in all_completed:
        return {
            "message": "Lesson already completed",
            "lesson_number": data.lesson_number,
            "completed_lessons": all_completed,
            "next_lesson_unlocked": hobby.can_go_next(
                data.skill,
                data.lesson_number,
                completed_lessons
            )
        }

    # Validate completion requirements
    can_complete = hobby.can_complete_lesson(
        skill=data.skill,
        lesson_number=data.lesson_number,
        reading_finished=data.reading_finished,
        video_finished=data.video_finished,
        completed_lessons=completed_lessons
    )

    if not can_complete:
        raise HTTPException(
            status_code=400,
            detail="Lesson requirements not completed"
        )

    # Save progress to SQLite
    save_lesson_progress(
        session_id=data.session_id,
        hobby_name=hobby.name,
        skill=data.skill,
        lesson_number=data.lesson_number,
        reading_finished=data.reading_finished,
        video_finished=data.video_finished
    )

    # Retrieve updated progress
    updated_lessons = get_completed_lessons(
        data.session_id,
        hobby.name,
        data.skill
    )

    if data.lesson_number not in updated_lessons:
        raise HTTPException(
            status_code=500,
            detail="Lesson completion could not be verified"
        )

    return {
        "message": "Lesson completed successfully",
        "lesson_number": data.lesson_number,
        "completed_lessons":
            hobby.get_all_completed_lessons(
                data.skill,
                updated_lessons
            ),
        "next_lesson_unlocked": hobby.can_go_next(
            data.skill,
            data.lesson_number,
            updated_lessons
        ),
        "progress": hobby.get_lesson_progress(
            data.skill,
            updated_lessons
        )
    }


# Lesson Roadmap and Progress

@app.get("/hobby/{hobby_name}/progress/{skill}")
def get_progress(
    hobby_name: str,
    skill: str,
    session_id: str
):

    hobby = find_hobby(hobby_name)

    validate_hobby_skill(hobby, skill)
    validate_hobby_lessons(hobby)

    completed_lessons = get_completed_lessons(
        session_id,
        hobby.name,
        skill
    )

    return {
        "hobby": hobby.name,
        "skill": skill,
        "completed_lessons":
            hobby.get_all_completed_lessons(
                skill,
                completed_lessons
            ),
        "progress": hobby.get_lesson_progress(
            skill,
            completed_lessons
        ),
        "roadmap": hobby.get_roadmap(
            skill,
            completed_lessons
        )
    }


# =========================================
# ACHIEVEMENTS
# =========================================

@app.post("/hobby/{hobby_name}/achievements")
def get_achievements(
    hobby_name: str,
    data: AchievementRequest
):

    hobby = find_hobby(hobby_name)

    validate_hobby_skill(hobby, data.skill)
    validate_hobby_lessons(hobby)

    completed_lessons = get_completed_lessons(
        data.session_id,
        hobby.name,
        data.skill
    )

    if any(
        type(index) is not int or index < 0
        for index in data.completed_quests
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid completed quests"
        )

    return {
        "hobby": hobby.name,
        "achievements": hobby.get_achievements(
            skill=data.skill,
            completed_quests=data.completed_quests,
            completed_lessons=completed_lessons
        )
    }
