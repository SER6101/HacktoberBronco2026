from .hobby import Hobby


class Running(Hobby):
    """Running learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Running',
            description='Improve stamina and enjoy outdoor exercise.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Shoes and warm-up",
                "reading": "Lesson 1: Shoes and warm-up. In running, this stage focuses on shoes and warm-up. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Increase training gradually and stop if you experience concerning pain.",
                "video_url": None
        },
        {
                "title": "Easy running pace",
                "reading": "Lesson 2: Easy running pace. In running, this stage focuses on easy running pace. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Recovery basics",
                "reading": "Lesson 3: Recovery basics. In running, this stage focuses on recovery basics. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Run-walk intervals",
                "reading": "Lesson 4: Run-walk intervals. In running, this stage focuses on run-walk intervals. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Breathing and form",
                "reading": "Lesson 5: Breathing and form. In running, this stage focuses on breathing and form. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Weekly routine",
                "reading": "Lesson 6: Weekly routine. In running, this stage focuses on weekly routine. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Endurance building",
                "reading": "Lesson 7: Endurance building. In running, this stage focuses on endurance building. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Tempo and intervals",
                "reading": "Lesson 8: Tempo and intervals. In running, this stage focuses on tempo and intervals. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Race-day planning",
                "reading": "Lesson 9: Race-day planning. In running, this stage focuses on race-day planning. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create a training plan",
                "reading": "Lesson 10: Create a training plan. In running, this stage focuses on create a training plan. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in running.",
                "Practice easy running pace in a short session.",
                "Complete a first exercise on recovery basics."
        ],
        "Intermediate": [
                "Practice run-walk intervals with attention to technique.",
                "Demonstrate progress with breathing and form.",
                "Finish a small challenge involving weekly routine."
        ],
        "Expert": [
                "Analyze and refine endurance building.",
                "Combine techniques while practicing race-day planning.",
                "Complete and reflect on create a training plan."
        ]
}
