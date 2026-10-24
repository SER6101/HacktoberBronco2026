from .hobby import Hobby


class Photography(Hobby):
    """Photography learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Photography',
            description='Capture interesting moments using a camera or phone.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Camera or phone basics",
                "reading": "Lesson 1: Camera or phone basics. In photography, this stage focuses on camera or phone basics. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Focus and exposure",
                "reading": "Lesson 2: Focus and exposure. In photography, this stage focuses on focus and exposure. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Composition and framing",
                "reading": "Lesson 3: Composition and framing. In photography, this stage focuses on composition and framing. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Working with natural light",
                "reading": "Lesson 4: Working with natural light. In photography, this stage focuses on working with natural light. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Portrait fundamentals",
                "reading": "Lesson 5: Portrait fundamentals. In photography, this stage focuses on portrait fundamentals. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Motion and shutter",
                "reading": "Lesson 6: Motion and shutter. In photography, this stage focuses on motion and shutter. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Manual exposure",
                "reading": "Lesson 7: Manual exposure. In photography, this stage focuses on manual exposure. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Editing workflow",
                "reading": "Lesson 8: Editing workflow. In photography, this stage focuses on editing workflow. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Visual storytelling",
                "reading": "Lesson 9: Visual storytelling. In photography, this stage focuses on visual storytelling. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create a photo series",
                "reading": "Lesson 10: Create a photo series. In photography, this stage focuses on create a photo series. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in photography.",
                "Practice focus and exposure in a short session.",
                "Complete a first exercise on composition and framing."
        ],
        "Intermediate": [
                "Practice working with natural light with attention to technique.",
                "Demonstrate progress with portrait fundamentals.",
                "Finish a small challenge involving motion and shutter."
        ],
        "Expert": [
                "Analyze and refine manual exposure.",
                "Combine techniques while practicing visual storytelling.",
                "Complete and reflect on create a photo series."
        ]
}
