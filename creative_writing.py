from hobby import Hobby


class CreativeWriting(Hobby):
    """Creative Writing learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Creative Writing',
            description='Write short stories, poetry, or personal essays.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Find a story idea",
                "reading": "Lesson 1: Find a story idea. In creative writing, this stage focuses on find a story idea. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Character sketches",
                "reading": "Lesson 2: Character sketches. In creative writing, this stage focuses on character sketches. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Setting and sensory detail",
                "reading": "Lesson 3: Setting and sensory detail. In creative writing, this stage focuses on setting and sensory detail. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Plot structure",
                "reading": "Lesson 4: Plot structure. In creative writing, this stage focuses on plot structure. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Dialogue",
                "reading": "Lesson 5: Dialogue. In creative writing, this stage focuses on dialogue. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Draft a scene",
                "reading": "Lesson 6: Draft a scene. In creative writing, this stage focuses on draft a scene. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Point of view",
                "reading": "Lesson 7: Point of view. In creative writing, this stage focuses on point of view. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Revision and pacing",
                "reading": "Lesson 8: Revision and pacing. In creative writing, this stage focuses on revision and pacing. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Editing for clarity",
                "reading": "Lesson 9: Editing for clarity. In creative writing, this stage focuses on editing for clarity. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Finish a short story",
                "reading": "Lesson 10: Finish a short story. In creative writing, this stage focuses on finish a short story. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in creative writing.",
                "Practice character sketches in a short session.",
                "Complete a first exercise on setting and sensory detail."
        ],
        "Intermediate": [
                "Practice plot structure with attention to technique.",
                "Demonstrate progress with dialogue.",
                "Finish a small challenge involving draft a scene."
        ],
        "Expert": [
                "Analyze and refine point of view.",
                "Combine techniques while practicing editing for clarity.",
                "Complete and reflect on finish a short story."
        ]
}
