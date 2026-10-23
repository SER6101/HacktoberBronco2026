
class Hobby:

    def __init__(self, name, description):
        self.name = name
        self.description = description

        # Skill levels selected from the first-visit popup
        self.skill_levels = [
            "Beginner",
            "Intermediate",
            "Expert"
        ]

        # Starting lesson for each skill level
        self.starting_lessons = {
            "Beginner": 1,
            "Intermediate": 4,
            "Expert": 7
        }

        # Every hobby has 10 lesson nodes
        self.total_lessons = 10

        # Child classes define their 10 lessons
        self.lessons = []

        # Skill-specific quests
        self.quests = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

    # SKill Validation

    def validate_skill(self, skill):
        if skill not in self.skill_levels:
            raise ValueError(
                "Skill must be Beginner, Intermediate, or Expert"
            )

    def get_starting_lesson(self, skill):
        self.validate_skill(skill)
        return self.starting_lessons[skill]

    # Automatic Lesson Completion

    def get_auto_completed_lessons(self, skill):
        start = self.get_starting_lesson(skill)

        # Intermediate: [1, 2, 3]
        # Expert: [1, 2, 3, 4, 5, 6]
        return list(range(1, start))

    def get_all_completed_lessons(
        self,
        skill,
        completed_lessons
    ):
        auto_completed = self.get_auto_completed_lessons(skill)

        all_completed = (
            set(auto_completed) |
            set(completed_lessons)
        )

        return sorted(
            number
            for number in all_completed
            if type(number) is int
            and 1 <= number <= self.total_lessons
        )

    # Main Hobby Page

    def get_main_page(
        self,
        skill,
        completed_lessons=None,
        completed_quests=None
    ):
        self.validate_skill(skill)

        if completed_lessons is None:
            completed_lessons = []

        if completed_quests is None:
            completed_quests = []

        progress = self.get_lesson_progress(
            skill,
            completed_lessons
        )

        current_lesson = progress["current_lesson"]

        return {
            "name": self.name,
            "description": self.description,
            "skill": skill,

            # Roadmap at the top
            "roadmap": self.get_roadmap(
                skill,
                completed_lessons
            ),

            # Current lesson in the center
            "current_lesson": current_lesson,
            "lesson": self.get_lesson(current_lesson),

            # Right sidebar
            "sidebar": {
                "position": "right",
                "progress": progress,
                "achievements": self.get_achievements(
                    skill,
                    completed_quests,
                    completed_lessons
                ),
                "quests": self.get_quests(skill)
            }
        }

    # Lesson Content

    def get_lessons(self, skill):
        self.validate_skill(skill)
        return self.lessons

    def get_lesson(self, lesson_number):
        if not 1 <= lesson_number <= self.total_lessons:
            raise ValueError("Invalid lesson number")

        if len(self.lessons) != self.total_lessons:
            raise ValueError(
                "Each hobby must define exactly 10 lessons"
            )

        return self.lessons[lesson_number - 1]

    # Lesson Unlock

    def is_lesson_unlocked(
        self,
        skill,
        lesson_number,
        completed_lessons
    ):
        self.validate_skill(skill)

        if not 1 <= lesson_number <= self.total_lessons:
            return False

        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        # First lesson is always unlocked
        if lesson_number == 1:
            return True

        # All earlier lessons must be completed
        return all(
            number in all_completed
            for number in range(1, lesson_number)
        )

    # Previous lesson never requires completion
    def can_go_previous(self, skill, lesson_number):
        self.validate_skill(skill)

        return 1 < lesson_number <= self.total_lessons

    # Next lesson requires the current lesson completed
    def can_go_next(
        self,
        skill,
        lesson_number,
        completed_lessons
    ):
        self.validate_skill(skill)

        # No next lesson after Lesson 10
        if not 1 <= lesson_number < self.total_lessons:
            return False

        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        return self.is_lesson_unlocked(
            skill,
            lesson_number + 1,
            all_completed
        )

    # Lesson Completion

    def can_complete_lesson(
        self,
        skill,
        lesson_number,
        reading_finished,
        video_finished,
        completed_lessons
    ):
        if not self.is_lesson_unlocked(
            skill,
            lesson_number,
            completed_lessons
        ):
            return False

        lesson = self.get_lesson(lesson_number)

        has_reading = bool(lesson.get("reading"))
        has_video = bool(lesson.get("video_url"))

        if not has_reading and not has_video:
            return False

        # Reading OR video completion is sufficient
        return (
            (has_reading and reading_finished)
            or
            (has_video and video_finished)
        )

    # Lesson Status

    def get_lesson_status(
        self,
        skill,
        lesson_number,
        completed_lessons
    ):
        lesson = self.get_lesson(lesson_number)

        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        return {
            "lesson_number": lesson_number,
            "title": lesson.get("title", ""),
            "completed": lesson_number in all_completed,
            "unlocked": self.is_lesson_unlocked(
                skill,
                lesson_number,
                all_completed
            ),
            "auto_completed": (
                lesson_number in
                self.get_auto_completed_lessons(skill)
            )
        }

    # Lesson Roadmap

    def get_roadmap(self, skill, completed_lessons):
        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        current_lesson = self.get_current_lesson(
            skill,
            completed_lessons
        )

        roadmap = []

        for number in range(1, self.total_lessons + 1):
            roadmap.append({
                "node": number,
                "title": self.get_lesson(number).get(
                    "title", ""
                ),
                "completed": number in all_completed,
                "auto_completed": (
                    number in
                    self.get_auto_completed_lessons(skill)
                ),
                "unlocked": self.is_lesson_unlocked(
                    skill,
                    number,
                    all_completed
                ),
                "current": number == current_lesson
            })

        return roadmap

    # Current Lesson

    def get_current_lesson(
        self,
        skill,
        completed_lessons
    ):
        start = self.get_starting_lesson(skill)

        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        # Find the first unfinished lesson
        for number in range(start, self.total_lessons + 1):
            if number not in all_completed:
                return number

        # All lessons completed
        return self.total_lessons

    # Lesson Progress

    def get_lesson_progress(
        self,
        skill,
        completed_lessons
    ):
        all_completed = self.get_all_completed_lessons(
            skill,
            completed_lessons
        )

        completed = len(all_completed)
        total = self.total_lessons

        percentage = round(
            completed / total * 100, 1
        )

        return {
            "completed": completed,
            "total": total,
            "percentage": percentage,
            "completed_lessons": all_completed,
            "current_lesson": self.get_current_lesson(
                skill,
                completed_lessons
            )
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

        return {
            "completed": completed,
            "total": total,
            "percentage": (
                round(completed / total * 100, 1)
                if total > 0 else 0
            )
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

        lesson_progress = self.get_lesson_progress(
            skill,
            completed_lessons
        )

        quest_progress = self.get_quest_progress(
            skill,
            completed_quests
        )

        lesson_count = lesson_progress["completed"]
        quest_count = quest_progress["completed"]

        return {
            "first_lesson": lesson_count >= 1,
            "three_lessons": lesson_count >= 3,
            "all_lessons": lesson_count == self.total_lessons,

            "first_quest": quest_count >= 1,
            "three_quests": quest_count >= 3,
            "all_quests": (
                quest_progress["total"] > 0
                and quest_count == quest_progress["total"]
            )
        }
