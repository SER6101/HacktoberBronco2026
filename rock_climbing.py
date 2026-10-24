from hobby import Hobby


class RockClimbing(Hobby):
    """Rock Climbing learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Rock Climbing',
            description='Develop strength and problem-solving skills through climbing.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Gym rules and safety",
                "reading": "Lesson 1: Gym rules and safety. In rock climbing, this stage focuses on gym rules and safety. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Use qualified instruction and follow the gym or guide safety system; never improvise rope protection.",
                "video_url": None
        },
        {
                "title": "Harness and equipment basics",
                "reading": "Lesson 2: Harness and equipment basics. In rock climbing, this stage focuses on harness and equipment basics. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Foot placement",
                "reading": "Lesson 3: Foot placement. In rock climbing, this stage focuses on foot placement. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Body positioning",
                "reading": "Lesson 4: Body positioning. In rock climbing, this stage focuses on body positioning. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Reading a route",
                "reading": "Lesson 5: Reading a route. In rock climbing, this stage focuses on reading a route. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Balance and efficient movement",
                "reading": "Lesson 6: Balance and efficient movement. In rock climbing, this stage focuses on balance and efficient movement. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Climbing technique drills",
                "reading": "Lesson 7: Climbing technique drills. In rock climbing, this stage focuses on climbing technique drills. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Rest and recovery",
                "reading": "Lesson 8: Rest and recovery. In rock climbing, this stage focuses on rest and recovery. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Route analysis",
                "reading": "Lesson 9: Route analysis. In rock climbing, this stage focuses on route analysis. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Plan a supervised climbing session",
                "reading": "Lesson 10: Plan a supervised climbing session. In rock climbing, this stage focuses on plan a supervised climbing session. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in rock climbing.",
                "Practice harness and equipment basics in a short session.",
                "Complete a first exercise on foot placement."
        ],
        "Intermediate": [
                "Practice body positioning with attention to technique.",
                "Demonstrate progress with reading a route.",
                "Finish a small challenge involving balance and efficient movement."
        ],
        "Expert": [
                "Analyze and refine climbing technique drills.",
                "Combine techniques while practicing route analysis.",
                "Complete and reflect on plan a supervised climbing session."
        ]
}
