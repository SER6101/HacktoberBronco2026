from hobby import Hobby


class Basketball(Hobby):
    """Basketball learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Basketball',
            description='Practice shooting, dribbling, and teamwork.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Court safety and rules",
                "reading": "Lesson 1: Court safety and rules. In basketball, this stage focuses on court safety and rules. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Warm up and use a suitable playing area.",
                "video_url": None
        },
        {
                "title": "Dribbling fundamentals",
                "reading": "Lesson 2: Dribbling fundamentals. In basketball, this stage focuses on dribbling fundamentals. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Shooting form",
                "reading": "Lesson 3: Shooting form. In basketball, this stage focuses on shooting form. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Passing and catching",
                "reading": "Lesson 4: Passing and catching. In basketball, this stage focuses on passing and catching. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Defensive stance",
                "reading": "Lesson 5: Defensive stance. In basketball, this stage focuses on defensive stance. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Layups and footwork",
                "reading": "Lesson 6: Layups and footwork. In basketball, this stage focuses on layups and footwork. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Off-ball movement",
                "reading": "Lesson 7: Off-ball movement. In basketball, this stage focuses on off-ball movement. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Team communication",
                "reading": "Lesson 8: Team communication. In basketball, this stage focuses on team communication. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Reading game situations",
                "reading": "Lesson 9: Reading game situations. In basketball, this stage focuses on reading game situations. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Practice a complete game plan",
                "reading": "Lesson 10: Practice a complete game plan. In basketball, this stage focuses on practice a complete game plan. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in basketball.",
                "Practice dribbling fundamentals in a short session.",
                "Complete a first exercise on shooting form."
        ],
        "Intermediate": [
                "Practice passing and catching with attention to technique.",
                "Demonstrate progress with defensive stance.",
                "Finish a small challenge involving layups and footwork."
        ],
        "Expert": [
                "Analyze and refine off-ball movement.",
                "Combine techniques while practicing reading game situations.",
                "Complete and reflect on practice a complete game plan."
        ]
}
