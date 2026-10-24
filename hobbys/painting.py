from .hobby import Hobby


class Painting(Hobby):
    """Painting learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Painting',
            description='Create artwork using watercolors, acrylics, or other paints.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Brushes and surfaces",
                "reading": "Lesson 1: Brushes and surfaces. In painting, this stage focuses on brushes and surfaces. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Color mixing",
                "reading": "Lesson 2: Color mixing. In painting, this stage focuses on color mixing. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Simple washes",
                "reading": "Lesson 3: Simple washes. In painting, this stage focuses on simple washes. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Value and contrast",
                "reading": "Lesson 4: Value and contrast. In painting, this stage focuses on value and contrast. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Layering techniques",
                "reading": "Lesson 5: Layering techniques. In painting, this stage focuses on layering techniques. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Still-life study",
                "reading": "Lesson 6: Still-life study. In painting, this stage focuses on still-life study. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Color harmony",
                "reading": "Lesson 7: Color harmony. In painting, this stage focuses on color harmony. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Texture and edges",
                "reading": "Lesson 8: Texture and edges. In painting, this stage focuses on texture and edges. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Expressive composition",
                "reading": "Lesson 9: Expressive composition. In painting, this stage focuses on expressive composition. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Complete a final painting",
                "reading": "Lesson 10: Complete a final painting. In painting, this stage focuses on complete a final painting. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in painting.",
                "Practice color mixing in a short session.",
                "Complete a first exercise on simple washes."
        ],
        "Intermediate": [
                "Practice value and contrast with attention to technique.",
                "Demonstrate progress with layering techniques.",
                "Finish a small challenge involving still-life study."
        ],
        "Expert": [
                "Analyze and refine color harmony.",
                "Combine techniques while practicing expressive composition.",
                "Complete and reflect on complete a final painting."
        ]
}
