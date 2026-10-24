from hobby import Hobby


class Dancing(Hobby):
    """Dancing learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Dancing',
            description='Explore dance styles and express yourself through movement.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Warm-up and rhythm",
                "reading": "Lesson 1: Warm-up and rhythm. In dancing, this stage focuses on warm-up and rhythm. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Counting musical beats",
                "reading": "Lesson 2: Counting musical beats. In dancing, this stage focuses on counting musical beats. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Basic footwork",
                "reading": "Lesson 3: Basic footwork. In dancing, this stage focuses on basic footwork. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Weight transfer",
                "reading": "Lesson 4: Weight transfer. In dancing, this stage focuses on weight transfer. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Learning a short sequence",
                "reading": "Lesson 5: Learning a short sequence. In dancing, this stage focuses on learning a short sequence. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Turns and transitions",
                "reading": "Lesson 6: Turns and transitions. In dancing, this stage focuses on turns and transitions. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Musical interpretation",
                "reading": "Lesson 7: Musical interpretation. In dancing, this stage focuses on musical interpretation. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Movement quality",
                "reading": "Lesson 8: Movement quality. In dancing, this stage focuses on movement quality. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Choreography design",
                "reading": "Lesson 9: Choreography design. In dancing, this stage focuses on choreography design. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Perform a complete routine",
                "reading": "Lesson 10: Perform a complete routine. In dancing, this stage focuses on perform a complete routine. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in dancing.",
                "Practice counting musical beats in a short session.",
                "Complete a first exercise on basic footwork."
        ],
        "Intermediate": [
                "Practice weight transfer with attention to technique.",
                "Demonstrate progress with learning a short sequence.",
                "Finish a small challenge involving turns and transitions."
        ],
        "Expert": [
                "Analyze and refine musical interpretation.",
                "Combine techniques while practicing choreography design.",
                "Complete and reflect on perform a complete routine."
        ]
}
