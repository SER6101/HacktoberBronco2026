from hobby import Hobby


class Birdwatching(Hobby):
    """Birdwatching learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Birdwatching',
            description='Observe birds and learn about local wildlife.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Ethical observation",
                "reading": "Lesson 1: Ethical observation. In birdwatching, this stage focuses on ethical observation. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Binocular basics",
                "reading": "Lesson 2: Binocular basics. In birdwatching, this stage focuses on binocular basics. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Bird shapes and silhouettes",
                "reading": "Lesson 3: Bird shapes and silhouettes. In birdwatching, this stage focuses on bird shapes and silhouettes. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Habitat clues",
                "reading": "Lesson 4: Habitat clues. In birdwatching, this stage focuses on habitat clues. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Listening for calls",
                "reading": "Lesson 5: Listening for calls. In birdwatching, this stage focuses on listening for calls. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Field notes",
                "reading": "Lesson 6: Field notes. In birdwatching, this stage focuses on field notes. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Seasonal migration",
                "reading": "Lesson 7: Seasonal migration. In birdwatching, this stage focuses on seasonal migration. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Identification by behavior",
                "reading": "Lesson 8: Identification by behavior. In birdwatching, this stage focuses on identification by behavior. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Surveying a local site",
                "reading": "Lesson 9: Surveying a local site. In birdwatching, this stage focuses on surveying a local site. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create a birding journal",
                "reading": "Lesson 10: Create a birding journal. In birdwatching, this stage focuses on create a birding journal. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in birdwatching.",
                "Practice binocular basics in a short session.",
                "Complete a first exercise on bird shapes and silhouettes."
        ],
        "Intermediate": [
                "Practice habitat clues with attention to technique.",
                "Demonstrate progress with listening for calls.",
                "Finish a small challenge involving field notes."
        ],
        "Expert": [
                "Analyze and refine seasonal migration.",
                "Combine techniques while practicing surveying a local site.",
                "Complete and reflect on create a birding journal."
        ]
}
