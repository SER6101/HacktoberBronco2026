class Hobby:

    def __init__(self, name, description):
        self.name = name
        self.description = description

        # Available skill levels
        self.skill_levels = [
            "Beginner",
            "Intermediate",
            "Expert"
        ]

        # Static introduction for all skill levels
        self.introduction = description

        # Skill-specific instructions
        self.instructions = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

        # Skill-specific lessons
        self.lessons = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

        # Skill-specific quests
        self.quests = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

    # Main Hobby Page

    def get_main_page(self):
        return {
            "name": self.name,
            "description": self.description,
            "introduction": self.introduction,
            "skill_levels": self.skill_levels,
            "sidebar": [
                "Introduction",
                "Lessons",
                "Quests",
                "Achievements"
            ]
        }

    # Introduction

    def get_introduction(self):
        # Same introduction regardless of skill level
        return self.introduction

    # Instruction

    def get_instructions(self, skill):
        self.validate_skill(skill)
        return self.instructions[skill]

    # Lesson

    def get_lessons(self, skill):
        self.validate_skill(skill)
        return self.lessons[skill]

    def get_lesson(self, skill, lesson_index):
        lessons = self.get_lessons(skill)

        if not 0 <= lesson_index < len(lessons):
            raise ValueError("Invalid lesson index")

        return lessons[lesson_index]

    # Check if the next lesson is unlocked
    def is_lesson_unlocked(
        self,
        skill,
        lesson_index,
        completed_lessons
    ):
        lessons = self.get_lessons(skill)

        if not 0 <= lesson_index < len(lessons):
            return False

        # First lesson is always available
        if lesson_index == 0:
            return True

        # All previous lessons must be completed
        return all(
            index in completed_lessons
            for index in range(lesson_index)
        )

    # Previous lesson is accessible regardless of completion
    def can_go_previous(self, skill, lesson_index):
        self.validate_skill(skill)
    
        return lesson_index > 0 and lesson_index < len(
            self.get_lessons(skill)
        )
    
    # Next lesson requires current lesson completion
    def can_go_next(
        self,
        skill,
        lesson_index,
        completed_lessons
    ):
        lessons = self.get_lessons(skill)

        # Check whether a next lesson exists
        if not 0 <= lesson_index < len(lessons) - 1:
            return False

        # Check whether the next lesson is unlocked
        return self.is_lesson_unlocked(
            skill,
            lesson_index + 1,
            completed_lessons
        )
    

    # Check whether a lesson can be completed
    def can_complete_lesson(
        self,
        skill,
        lesson_index,
        reading_finished,
        video_finished,
        completed_lessons
    ):
        if not self.is_lesson_unlocked(
            skill,
            lesson_index,
            completed_lessons
        ):
            return False

        lesson = self.get_lesson(skill, lesson_index)

        has_reading = bool(lesson.get("reading"))
        has_video = bool(lesson.get("video_url"))

        # A lesson must contain reading or video content
        if not has_reading and not has_video:
            return False

        # Completing either available format is sufficient
        return (
            (has_reading and reading_finished)
            or
            (has_video and video_finished)
        )

    # Return completion information for a lesson
    def get_lesson_status(
        self,
        skill,
        lesson_index,
        completed_lessons
    ):
        lesson = self.get_lesson(skill, lesson_index)

        completed = lesson_index in completed_lessons

        unlocked = self.is_lesson_unlocked(
            skill,
            lesson_index,
            completed_lessons
        )

        return {
            "lesson_index": lesson_index,
            "title": lesson.get("title", ""),
            "unlocked": unlocked,
            "completed": completed
        }

    # Calculate lesson progress
    def get_lesson_progress(
        self,
        skill,
        completed_lessons
    ):
        lessons = self.get_lessons(skill)

        valid_completed = set(completed_lessons) & set(
            range(len(lessons))
        )

        total = len(lessons)
        completed = len(valid_completed)

        percentage = (
            round(completed / total * 100, 1)
            if total > 0 else 0
        )

        return {
            "completed": completed,
            "total": total,
            "percentage": percentage
        }

    # Quest

    def get_quests(self, skill):
        self.validate_skill(skill)
        return self.quests[skill]

    def get_quest_progress(
        self,
        skill,
        completed_quests
    ):
        quests = self.get_quests(skill)

        valid_completed = set(completed_quests) & set(
            range(len(quests))
        )

        total = len(quests)
        completed = len(valid_completed)

        percentage = (
            round(completed / total * 100, 1)
            if total > 0 else 0
        )

        return {
            "completed": completed,
            "total": total,
            "percentage": percentage
        }

    # Achievements

    def get_achievements(
        self,
        skill,
        completed_quests,
        completed_lessons=None
    ):
        if completed_lessons is None:
            completed_lessons = []

        quest_progress = self.get_quest_progress(
            skill,
            completed_quests
        )

        lesson_progress = self.get_lesson_progress(
            skill,
            completed_lessons
        )

        quest_count = quest_progress["completed"]
        lesson_count = lesson_progress["completed"]

        return {
            "first_quest": quest_count >= 1,

            "three_quests": quest_count >= 3,

            "level_complete": (
                quest_progress["total"] > 0
                and quest_count == quest_progress["total"]
            ),

            "first_lesson": lesson_count >= 1,

            "all_lessons": (
                lesson_progress["total"] > 0
                and lesson_count == lesson_progress["total"]
            )
        }

    # Skill Validation

    def validate_skill(self, skill):
        if skill not in self.skill_levels:
            raise ValueError(
                "Skill must be Beginner, Intermediate, or Expert"
            )
