from hobby import Hobby


class Soccer(Hobby):
    """Soccer learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Soccer',
            description='Improve coordination, endurance, and teamwork.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Field safety and rules",
                "reading": "Lesson 1: Field safety and rules. In soccer, this stage focuses on field safety and rules. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Warm up and use appropriate footwear and a safe field.",
                "video_url": None
        },
        {
                "title": "Ball control",
                "reading": "Lesson 2: Ball control. In soccer, this stage focuses on ball control. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Passing technique",
                "reading": "Lesson 3: Passing technique. In soccer, this stage focuses on passing technique. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Dribbling under pressure",
                "reading": "Lesson 4: Dribbling under pressure. In soccer, this stage focuses on dribbling under pressure. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Receiving and turning",
                "reading": "Lesson 5: Receiving and turning. In soccer, this stage focuses on receiving and turning. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Shooting technique",
                "reading": "Lesson 6: Shooting technique. In soccer, this stage focuses on shooting technique. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Defensive positioning",
                "reading": "Lesson 7: Defensive positioning. In soccer, this stage focuses on defensive positioning. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Team formations",
                "reading": "Lesson 8: Team formations. In soccer, this stage focuses on team formations. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Decision making",
                "reading": "Lesson 9: Decision making. In soccer, this stage focuses on decision making. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Design a team practice",
                "reading": "Lesson 10: Design a team practice. In soccer, this stage focuses on design a team practice. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in soccer.",
                "Practice ball control in a short session.",
                "Complete a first exercise on passing technique."
        ],
        "Intermediate": [
                "Practice dribbling under pressure with attention to technique.",
                "Demonstrate progress with receiving and turning.",
                "Finish a small challenge involving shooting technique."
        ],
        "Expert": [
                "Analyze and refine defensive positioning.",
                "Combine techniques while practicing decision making.",
                "Complete and reflect on design a team practice."
        ]
}
