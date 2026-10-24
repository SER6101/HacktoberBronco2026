from .hobby import Hobby


class Coding(Hobby):
    """Coding learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Coding',
            description='Build small projects and learn programming.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Editor and first program",
                "reading": "Lesson 1: Editor and first program. In coding, this stage focuses on editor and first program. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Variables and values",
                "reading": "Lesson 2: Variables and values. In coding, this stage focuses on variables and values. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Conditions and loops",
                "reading": "Lesson 3: Conditions and loops. In coding, this stage focuses on conditions and loops. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Functions",
                "reading": "Lesson 4: Functions. In coding, this stage focuses on functions. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Lists and dictionaries",
                "reading": "Lesson 5: Lists and dictionaries. In coding, this stage focuses on lists and dictionaries. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Debugging",
                "reading": "Lesson 6: Debugging. In coding, this stage focuses on debugging. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Working with files",
                "reading": "Lesson 7: Working with files. In coding, this stage focuses on working with files. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Using APIs",
                "reading": "Lesson 8: Using APIs. In coding, this stage focuses on using apis. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Testing and refactoring",
                "reading": "Lesson 9: Testing and refactoring. In coding, this stage focuses on testing and refactoring. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Build a small application",
                "reading": "Lesson 10: Build a small application. In coding, this stage focuses on build a small application. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in coding.",
                "Practice variables and values in a short session.",
                "Complete a first exercise on conditions and loops."
        ],
        "Intermediate": [
                "Practice functions with attention to technique.",
                "Demonstrate progress with lists and dictionaries.",
                "Finish a small challenge involving debugging."
        ],
        "Expert": [
                "Analyze and refine working with files.",
                "Combine techniques while practicing testing and refactoring.",
                "Complete and reflect on build a small application."
        ]
}
