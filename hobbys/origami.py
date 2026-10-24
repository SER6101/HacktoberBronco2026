from .hobby import Hobby


class Origami(Hobby):
    """Origami learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Origami',
            description='Create paper sculptures through folding techniques.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Paper selection",
                "reading": "Lesson 1: Paper selection. In origami, this stage focuses on paper selection. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Basic valley and mountain folds",
                "reading": "Lesson 2: Basic valley and mountain folds. In origami, this stage focuses on basic valley and mountain folds. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Simple animal model",
                "reading": "Lesson 3: Simple animal model. In origami, this stage focuses on simple animal model. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Accurate creases",
                "reading": "Lesson 4: Accurate creases. In origami, this stage focuses on accurate creases. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Common bases",
                "reading": "Lesson 5: Common bases. In origami, this stage focuses on common bases. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Reading diagram symbols",
                "reading": "Lesson 6: Reading diagram symbols. In origami, this stage focuses on reading diagram symbols. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Modular units",
                "reading": "Lesson 7: Modular units. In origami, this stage focuses on modular units. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Complex sequences",
                "reading": "Lesson 8: Complex sequences. In origami, this stage focuses on complex sequences. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Design variations",
                "reading": "Lesson 9: Design variations. In origami, this stage focuses on design variations. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create an origami display",
                "reading": "Lesson 10: Create an origami display. In origami, this stage focuses on create an origami display. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in origami.",
                "Practice basic valley and mountain folds in a short session.",
                "Complete a first exercise on simple animal model."
        ],
        "Intermediate": [
                "Practice accurate creases with attention to technique.",
                "Demonstrate progress with common bases.",
                "Finish a small challenge involving reading diagram symbols."
        ],
        "Expert": [
                "Analyze and refine modular units.",
                "Combine techniques while practicing design variations.",
                "Complete and reflect on create an origami display."
        ]
}
