from hobby import Hobby


class Cycling(Hobby):
    """Cycling learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Cycling',
            description='Explore your surroundings while improving endurance.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Bike fit and helmet",
                "reading": "Lesson 1: Bike fit and helmet. In cycling, this stage focuses on bike fit and helmet. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Use a properly fitted helmet and follow local traffic rules.",
                "video_url": None
        },
        {
                "title": "Basic bike inspection",
                "reading": "Lesson 2: Basic bike inspection. In cycling, this stage focuses on basic bike inspection. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Starting and stopping",
                "reading": "Lesson 3: Starting and stopping. In cycling, this stage focuses on starting and stopping. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Shifting gears",
                "reading": "Lesson 4: Shifting gears. In cycling, this stage focuses on shifting gears. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Cornering and signaling",
                "reading": "Lesson 5: Cornering and signaling. In cycling, this stage focuses on cornering and signaling. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Route planning",
                "reading": "Lesson 6: Route planning. In cycling, this stage focuses on route planning. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Climbing and cadence",
                "reading": "Lesson 7: Climbing and cadence. In cycling, this stage focuses on climbing and cadence. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Handling varied terrain",
                "reading": "Lesson 8: Handling varied terrain. In cycling, this stage focuses on handling varied terrain. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Long-ride preparation",
                "reading": "Lesson 9: Long-ride preparation. In cycling, this stage focuses on long-ride preparation. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Plan a safe cycling route",
                "reading": "Lesson 10: Plan a safe cycling route. In cycling, this stage focuses on plan a safe cycling route. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in cycling.",
                "Practice basic bike inspection in a short session.",
                "Complete a first exercise on starting and stopping."
        ],
        "Intermediate": [
                "Practice shifting gears with attention to technique.",
                "Demonstrate progress with cornering and signaling.",
                "Finish a small challenge involving route planning."
        ],
        "Expert": [
                "Analyze and refine climbing and cadence.",
                "Combine techniques while practicing long-ride preparation.",
                "Complete and reflect on plan a safe cycling route."
        ]
}
