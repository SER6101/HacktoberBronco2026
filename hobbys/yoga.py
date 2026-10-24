from .hobby import Hobby


class Yoga(Hobby):
    """Yoga learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Yoga',
            description='Improve flexibility and practice mindfulness.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Safe setup and breathing",
                "reading": "Lesson 1: Safe setup and breathing. In yoga, this stage focuses on safe setup and breathing. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Avoid forcing a pose and modify movements to your comfortable range.",
                "video_url": None
        },
        {
                "title": "Foundational poses",
                "reading": "Lesson 2: Foundational poses. In yoga, this stage focuses on foundational poses. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Gentle mobility",
                "reading": "Lesson 3: Gentle mobility. In yoga, this stage focuses on gentle mobility. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Alignment and balance",
                "reading": "Lesson 4: Alignment and balance. In yoga, this stage focuses on alignment and balance. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Standing sequences",
                "reading": "Lesson 5: Standing sequences. In yoga, this stage focuses on standing sequences. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Breath with movement",
                "reading": "Lesson 6: Breath with movement. In yoga, this stage focuses on breath with movement. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Longer flow design",
                "reading": "Lesson 7: Longer flow design. In yoga, this stage focuses on longer flow design. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Strength and stability",
                "reading": "Lesson 8: Strength and stability. In yoga, this stage focuses on strength and stability. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Mindful modifications",
                "reading": "Lesson 9: Mindful modifications. In yoga, this stage focuses on mindful modifications. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Build a personal practice",
                "reading": "Lesson 10: Build a personal practice. In yoga, this stage focuses on build a personal practice. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in yoga.",
                "Practice foundational poses in a short session.",
                "Complete a first exercise on gentle mobility."
        ],
        "Intermediate": [
                "Practice alignment and balance with attention to technique.",
                "Demonstrate progress with standing sequences.",
                "Finish a small challenge involving breath with movement."
        ],
        "Expert": [
                "Analyze and refine longer flow design.",
                "Combine techniques while practicing mindful modifications.",
                "Complete and reflect on build a personal practice."
        ]
}
