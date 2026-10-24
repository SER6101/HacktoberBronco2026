from hobby import Hobby


class PlayingPiano(Hobby):
    """Playing Piano learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Playing Piano',
            description='Learn musical techniques and play your favorite songs.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Keyboard layout",
                "reading": "Lesson 1: Keyboard layout. In playing piano, this stage focuses on keyboard layout. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Posture and hand shape",
                "reading": "Lesson 2: Posture and hand shape. In playing piano, this stage focuses on posture and hand shape. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Reading simple notes",
                "reading": "Lesson 3: Reading simple notes. In playing piano, this stage focuses on reading simple notes. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Scales and fingerings",
                "reading": "Lesson 4: Scales and fingerings. In playing piano, this stage focuses on scales and fingerings. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Basic chords",
                "reading": "Lesson 5: Basic chords. In playing piano, this stage focuses on basic chords. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Two-hand coordination",
                "reading": "Lesson 6: Two-hand coordination. In playing piano, this stage focuses on two-hand coordination. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Dynamics and phrasing",
                "reading": "Lesson 7: Dynamics and phrasing. In playing piano, this stage focuses on dynamics and phrasing. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Sight-reading practice",
                "reading": "Lesson 8: Sight-reading practice. In playing piano, this stage focuses on sight-reading practice. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Interpretation and expression",
                "reading": "Lesson 9: Interpretation and expression. In playing piano, this stage focuses on interpretation and expression. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Perform a complete piece",
                "reading": "Lesson 10: Perform a complete piece. In playing piano, this stage focuses on perform a complete piece. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in playing piano.",
                "Practice posture and hand shape in a short session.",
                "Complete a first exercise on reading simple notes."
        ],
        "Intermediate": [
                "Practice scales and fingerings with attention to technique.",
                "Demonstrate progress with basic chords.",
                "Finish a small challenge involving two-hand coordination."
        ],
        "Expert": [
                "Analyze and refine dynamics and phrasing.",
                "Combine techniques while practicing interpretation and expression.",
                "Complete and reflect on perform a complete piece."
        ]
}
