from hobby import Hobby


class Drawing(Hobby):
    """Drawing learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Drawing',
            description='Express yourself through sketches and art.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Tools and paper",
                "reading": "Lesson 1: Tools and paper. In drawing, this stage focuses on tools and paper. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Lines and shapes",
                "reading": "Lesson 2: Lines and shapes. In drawing, this stage focuses on lines and shapes. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Light and shadow",
                "reading": "Lesson 3: Light and shadow. In drawing, this stage focuses on light and shadow. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Proportions",
                "reading": "Lesson 4: Proportions. In drawing, this stage focuses on proportions. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Perspective basics",
                "reading": "Lesson 5: Perspective basics. In drawing, this stage focuses on perspective basics. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Texture studies",
                "reading": "Lesson 6: Texture studies. In drawing, this stage focuses on texture studies. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Gesture drawing",
                "reading": "Lesson 7: Gesture drawing. In drawing, this stage focuses on gesture drawing. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Composition",
                "reading": "Lesson 8: Composition. In drawing, this stage focuses on composition. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Portrait study",
                "reading": "Lesson 9: Portrait study. In drawing, this stage focuses on portrait study. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Personal sketch portfolio",
                "reading": "Lesson 10: Personal sketch portfolio. In drawing, this stage focuses on personal sketch portfolio. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in drawing.",
                "Practice lines and shapes in a short session.",
                "Complete a first exercise on light and shadow."
        ],
        "Intermediate": [
                "Practice proportions with attention to technique.",
                "Demonstrate progress with perspective basics.",
                "Finish a small challenge involving texture studies."
        ],
        "Expert": [
                "Analyze and refine gesture drawing.",
                "Combine techniques while practicing portrait study.",
                "Complete and reflect on personal sketch portfolio."
        ]
}
