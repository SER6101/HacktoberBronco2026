from hobby import Hobby


class VideoGaming(Hobby):
    """Video Gaming learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Video Gaming',
            description='Explore different game genres and interactive worlds.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Choose a game and goals",
                "reading": "Lesson 1: Choose a game and goals. In video gaming, this stage focuses on choose a game and goals. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Controls and settings",
                "reading": "Lesson 2: Controls and settings. In video gaming, this stage focuses on controls and settings. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Core mechanics",
                "reading": "Lesson 3: Core mechanics. In video gaming, this stage focuses on core mechanics. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Practice and feedback",
                "reading": "Lesson 4: Practice and feedback. In video gaming, this stage focuses on practice and feedback. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Map awareness",
                "reading": "Lesson 5: Map awareness. In video gaming, this stage focuses on map awareness. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Team communication",
                "reading": "Lesson 6: Team communication. In video gaming, this stage focuses on team communication. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Strategy adaptation",
                "reading": "Lesson 7: Strategy adaptation. In video gaming, this stage focuses on strategy adaptation. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Reviewing replays",
                "reading": "Lesson 8: Reviewing replays. In video gaming, this stage focuses on reviewing replays. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Advanced challenge planning",
                "reading": "Lesson 9: Advanced challenge planning. In video gaming, this stage focuses on advanced challenge planning. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Create a personal improvement plan",
                "reading": "Lesson 10: Create a personal improvement plan. In video gaming, this stage focuses on create a personal improvement plan. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in video gaming.",
                "Practice controls and settings in a short session.",
                "Complete a first exercise on core mechanics."
        ],
        "Intermediate": [
                "Practice practice and feedback with attention to technique.",
                "Demonstrate progress with map awareness.",
                "Finish a small challenge involving team communication."
        ],
        "Expert": [
                "Analyze and refine strategy adaptation.",
                "Combine techniques while practicing advanced challenge planning.",
                "Complete and reflect on create a personal improvement plan."
        ]
}
