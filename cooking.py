from hobby import Hobby


class Cooking(Hobby):
    """Cooking learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Cooking',
            description='Experiment with recipes and flavors.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Kitchen safety",
                "reading": "Lesson 1: Kitchen safety. In cooking, this stage focuses on kitchen safety. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Use safe food handling and be cautious around hot surfaces and sharp tools.",
                "video_url": None
        },
        {
                "title": "Measuring ingredients",
                "reading": "Lesson 2: Measuring ingredients. In cooking, this stage focuses on measuring ingredients. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Knife skills",
                "reading": "Lesson 3: Knife skills. In cooking, this stage focuses on knife skills. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Heat control",
                "reading": "Lesson 4: Heat control. In cooking, this stage focuses on heat control. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Seasoning basics",
                "reading": "Lesson 5: Seasoning basics. In cooking, this stage focuses on seasoning basics. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Cooking a balanced meal",
                "reading": "Lesson 6: Cooking a balanced meal. In cooking, this stage focuses on cooking a balanced meal. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Sauces and reductions",
                "reading": "Lesson 7: Sauces and reductions. In cooking, this stage focuses on sauces and reductions. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Timing multiple dishes",
                "reading": "Lesson 8: Timing multiple dishes. In cooking, this stage focuses on timing multiple dishes. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Recipe adaptation",
                "reading": "Lesson 9: Recipe adaptation. In cooking, this stage focuses on recipe adaptation. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Plan a complete menu",
                "reading": "Lesson 10: Plan a complete menu. In cooking, this stage focuses on plan a complete menu. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in cooking.",
                "Practice measuring ingredients in a short session.",
                "Complete a first exercise on knife skills."
        ],
        "Intermediate": [
                "Practice heat control with attention to technique.",
                "Demonstrate progress with seasoning basics.",
                "Finish a small challenge involving cooking a balanced meal."
        ],
        "Expert": [
                "Analyze and refine sauces and reductions.",
                "Combine techniques while practicing recipe adaptation.",
                "Complete and reflect on plan a complete menu."
        ]
}
