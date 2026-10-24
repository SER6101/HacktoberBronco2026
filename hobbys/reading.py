from hobby import Hobby


class Reading(Hobby):
    """Reading learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Reading',
            description='Discover new stories, ideas, and knowledge through books.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Choose a reading goal",
                "reading": "Lesson 1: Choose a reading goal. In reading, this stage focuses on choose a reading goal. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Find books that fit",
                "reading": "Lesson 2: Find books that fit. In reading, this stage focuses on find books that fit. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Build a reading routine",
                "reading": "Lesson 3: Build a reading routine. In reading, this stage focuses on build a reading routine. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Active reading notes",
                "reading": "Lesson 4: Active reading notes. In reading, this stage focuses on active reading notes. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Recognize themes",
                "reading": "Lesson 5: Recognize themes. In reading, this stage focuses on recognize themes. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Discuss interpretations",
                "reading": "Lesson 6: Discuss interpretations. In reading, this stage focuses on discuss interpretations. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Compare authors",
                "reading": "Lesson 7: Compare authors. In reading, this stage focuses on compare authors. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Analyze narrative structure",
                "reading": "Lesson 8: Analyze narrative structure. In reading, this stage focuses on analyze narrative structure. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Explore unfamiliar genres",
                "reading": "Lesson 9: Explore unfamiliar genres. In reading, this stage focuses on explore unfamiliar genres. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create a reading reflection",
                "reading": "Lesson 10: Create a reading reflection. In reading, this stage focuses on create a reading reflection. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in reading.",
                "Practice find books that fit in a short session.",
                "Complete a first exercise on build a reading routine."
        ],
        "Intermediate": [
                "Practice active reading notes with attention to technique.",
                "Demonstrate progress with recognize themes.",
                "Finish a small challenge involving discuss interpretations."
        ],
        "Expert": [
                "Analyze and refine compare authors.",
                "Combine techniques while practicing explore unfamiliar genres.",
                "Complete and reflect on create a reading reflection."
        ]
}
