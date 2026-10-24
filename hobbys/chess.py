from .hobby import Hobby


class Chess(Hobby):
    """Chess learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Chess',
            description='Develop strategic thinking through chess matches.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Board and piece movement",
                "reading": "Lesson 1: Board and piece movement. In chess, this stage focuses on board and piece movement. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Check and checkmate",
                "reading": "Lesson 2: Check and checkmate. In chess, this stage focuses on check and checkmate. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Opening principles",
                "reading": "Lesson 3: Opening principles. In chess, this stage focuses on opening principles. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Tactics and forks",
                "reading": "Lesson 4: Tactics and forks. In chess, this stage focuses on tactics and forks. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Pins and skewers",
                "reading": "Lesson 5: Pins and skewers. In chess, this stage focuses on pins and skewers. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Endgame basics",
                "reading": "Lesson 6: Endgame basics. In chess, this stage focuses on endgame basics. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Calculation practice",
                "reading": "Lesson 7: Calculation practice. In chess, this stage focuses on calculation practice. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Pawn structures",
                "reading": "Lesson 8: Pawn structures. In chess, this stage focuses on pawn structures. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Game analysis",
                "reading": "Lesson 9: Game analysis. In chess, this stage focuses on game analysis. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Build a study repertoire",
                "reading": "Lesson 10: Build a study repertoire. In chess, this stage focuses on build a study repertoire. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in chess.",
                "Practice check and checkmate in a short session.",
                "Complete a first exercise on opening principles."
        ],
        "Intermediate": [
                "Practice tactics and forks with attention to technique.",
                "Demonstrate progress with pins and skewers.",
                "Finish a small challenge involving endgame basics."
        ],
        "Expert": [
                "Analyze and refine calculation practice.",
                "Combine techniques while practicing game analysis.",
                "Complete and reflect on build a study repertoire."
        ]
}
