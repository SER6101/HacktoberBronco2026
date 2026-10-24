from hobby import Hobby


class LearningALanguage(Hobby):
    """Learning a Language learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Learning a Language',
            description='Explore new languages and cultures through practice.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Choose a target and goal",
                "reading": "Lesson 1: Choose a target and goal. In learning a language, this stage focuses on choose a target and goal. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Sounds and pronunciation",
                "reading": "Lesson 2: Sounds and pronunciation. In learning a language, this stage focuses on sounds and pronunciation. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Everyday greetings",
                "reading": "Lesson 3: Everyday greetings. In learning a language, this stage focuses on everyday greetings. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Useful vocabulary",
                "reading": "Lesson 4: Useful vocabulary. In learning a language, this stage focuses on useful vocabulary. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Basic sentence patterns",
                "reading": "Lesson 5: Basic sentence patterns. In learning a language, this stage focuses on basic sentence patterns. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Listening practice",
                "reading": "Lesson 6: Listening practice. In learning a language, this stage focuses on listening practice. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Conversational questions",
                "reading": "Lesson 7: Conversational questions. In learning a language, this stage focuses on conversational questions. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Reading short texts",
                "reading": "Lesson 8: Reading short texts. In learning a language, this stage focuses on reading short texts. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Speaking with feedback",
                "reading": "Lesson 9: Speaking with feedback. In learning a language, this stage focuses on speaking with feedback. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Build a language study routine",
                "reading": "Lesson 10: Build a language study routine. In learning a language, this stage focuses on build a language study routine. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in learning a language.",
                "Practice sounds and pronunciation in a short session.",
                "Complete a first exercise on everyday greetings."
        ],
        "Intermediate": [
                "Practice useful vocabulary with attention to technique.",
                "Demonstrate progress with basic sentence patterns.",
                "Finish a small challenge involving listening practice."
        ],
        "Expert": [
                "Analyze and refine conversational questions.",
                "Combine techniques while practicing speaking with feedback.",
                "Complete and reflect on build a language study routine."
        ]
}
