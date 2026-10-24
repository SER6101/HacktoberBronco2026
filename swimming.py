from hobby import Hobby


class Swimming(Hobby):
    """Swimming learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Swimming',
            description='Build endurance and enjoy exercise in the water.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Pool safety and supervision",
                "reading": "Lesson 1: Pool safety and supervision. In swimming, this stage focuses on pool safety and supervision. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Practice with appropriate supervision and never swim alone.",
                "video_url": None
        },
        {
                "title": "Breathing at the wall",
                "reading": "Lesson 2: Breathing at the wall. In swimming, this stage focuses on breathing at the wall. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Floating with support",
                "reading": "Lesson 3: Floating with support. In swimming, this stage focuses on floating with support. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Body position",
                "reading": "Lesson 4: Body position. In swimming, this stage focuses on body position. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Basic kicking",
                "reading": "Lesson 5: Basic kicking. In swimming, this stage focuses on basic kicking. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Coordinating strokes",
                "reading": "Lesson 6: Coordinating strokes. In swimming, this stage focuses on coordinating strokes. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Efficient freestyle",
                "reading": "Lesson 7: Efficient freestyle. In swimming, this stage focuses on efficient freestyle. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Turns and pacing",
                "reading": "Lesson 8: Turns and pacing. In swimming, this stage focuses on turns and pacing. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Endurance sets",
                "reading": "Lesson 9: Endurance sets. In swimming, this stage focuses on endurance sets. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Build a safe swim session",
                "reading": "Lesson 10: Build a safe swim session. In swimming, this stage focuses on build a safe swim session. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in swimming.",
                "Practice breathing at the wall in a short session.",
                "Complete a first exercise on floating with support."
        ],
        "Intermediate": [
                "Practice body position with attention to technique.",
                "Demonstrate progress with basic kicking.",
                "Finish a small challenge involving coordinating strokes."
        ],
        "Expert": [
                "Analyze and refine efficient freestyle.",
                "Combine techniques while practicing endurance sets.",
                "Complete and reflect on build a safe swim session."
        ]
}
