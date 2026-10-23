class Hobby:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.skill_levels = [
            "Beginner",
            "Intermediate",
            "Expert"
        ]

        self.instructions = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

        self.quests = {
            "Beginner": [],
            "Intermediate": [],
            "Expert": []
        }

    # Return the main hobby page information
    def get_main_page(self):
        return {
            "name": self.name,
            "description": self.description,
            "skill_levels": self.skill_levels,
            "sidebar": [
                "Introduction",
                "Quests",
                "Achievements"
            ]
        }

    # Return instructions based on skill level
    def get_instructions(self, skill):
        return self.instructions.get(skill, [])

    # Return quests based on skill level
    def get_quests(self, skill):
        return self.quests.get(skill, [])

    # Calculate achievements from completed quests
    def get_achievements(self, skill, completed_quests):
        quests = self.get_quests(skill)

        completed = len(
            set(completed_quests) &
            set(range(len(quests)))
        )

        return {
            "first_quest": completed >= 1,
            "three_quests": completed >= 3,
            "level_complete": (
                len(quests) > 0 and completed == len(quests)
            )
        }
