from hobby import Hobby


class Gardening(Hobby):
    """Gardening learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Gardening',
            description='Grow plants, flowers, vegetables, and herbs.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Choose a growing space",
                "reading": "Lesson 1: Choose a growing space. In gardening, this stage focuses on choose a growing space. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Understand sunlight",
                "reading": "Lesson 2: Understand sunlight. In gardening, this stage focuses on understand sunlight. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Soil and containers",
                "reading": "Lesson 3: Soil and containers. In gardening, this stage focuses on soil and containers. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Sowing and transplanting",
                "reading": "Lesson 4: Sowing and transplanting. In gardening, this stage focuses on sowing and transplanting. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Watering routines",
                "reading": "Lesson 5: Watering routines. In gardening, this stage focuses on watering routines. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Recognize plant stress",
                "reading": "Lesson 6: Recognize plant stress. In gardening, this stage focuses on recognize plant stress. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Pruning and maintenance",
                "reading": "Lesson 7: Pruning and maintenance. In gardening, this stage focuses on pruning and maintenance. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Pest prevention",
                "reading": "Lesson 8: Pest prevention. In gardening, this stage focuses on pest prevention. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Seasonal garden planning",
                "reading": "Lesson 9: Seasonal garden planning. In gardening, this stage focuses on seasonal garden planning. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Harvest and seed saving",
                "reading": "Lesson 10: Harvest and seed saving. In gardening, this stage focuses on harvest and seed saving. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in gardening.",
                "Practice understand sunlight in a short session.",
                "Complete a first exercise on soil and containers."
        ],
        "Intermediate": [
                "Practice sowing and transplanting with attention to technique.",
                "Demonstrate progress with watering routines.",
                "Finish a small challenge involving recognize plant stress."
        ],
        "Expert": [
                "Analyze and refine pruning and maintenance.",
                "Combine techniques while practicing seasonal garden planning.",
                "Complete and reflect on harvest and seed saving."
        ]
}
