from .hobby import Hobby


class BoardGames(Hobby):
    """Board Games learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Board Games',
            description='Enjoy strategy and cooperative games with others.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Game components",
                "reading": "Lesson 1: Game components. In board games, this stage focuses on game components. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Rules and turn order",
                "reading": "Lesson 2: Rules and turn order. In board games, this stage focuses on rules and turn order. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Playing a practice round",
                "reading": "Lesson 3: Playing a practice round. In board games, this stage focuses on playing a practice round. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Planning ahead",
                "reading": "Lesson 4: Planning ahead. In board games, this stage focuses on planning ahead. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Resource management",
                "reading": "Lesson 5: Resource management. In board games, this stage focuses on resource management. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Cooperative communication",
                "reading": "Lesson 6: Cooperative communication. In board games, this stage focuses on cooperative communication. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Probability and tradeoffs",
                "reading": "Lesson 7: Probability and tradeoffs. In board games, this stage focuses on probability and tradeoffs. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Reading opponents",
                "reading": "Lesson 8: Reading opponents. In board games, this stage focuses on reading opponents. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Strategy review",
                "reading": "Lesson 9: Strategy review. In board games, this stage focuses on strategy review. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Host a game session",
                "reading": "Lesson 10: Host a game session. In board games, this stage focuses on host a game session. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in board games.",
                "Practice rules and turn order in a short session.",
                "Complete a first exercise on playing a practice round."
        ],
        "Intermediate": [
                "Practice planning ahead with attention to technique.",
                "Demonstrate progress with resource management.",
                "Finish a small challenge involving cooperative communication."
        ],
        "Expert": [
                "Analyze and refine probability and tradeoffs.",
                "Combine techniques while practicing strategy review.",
                "Complete and reflect on host a game session."
        ]
}
