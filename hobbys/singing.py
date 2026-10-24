from .hobby import Hobby


class Singing(Hobby):
    """Singing learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Singing',
            description='Improve your voice and explore musical expression.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Vocal health and posture",
                "reading": "Lesson 1: Vocal health and posture. In singing, this stage focuses on vocal health and posture. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Breath support",
                "reading": "Lesson 2: Breath support. In singing, this stage focuses on breath support. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Pitch matching",
                "reading": "Lesson 3: Pitch matching. In singing, this stage focuses on pitch matching. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Warm-up routines",
                "reading": "Lesson 4: Warm-up routines. In singing, this stage focuses on warm-up routines. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Vowels and resonance",
                "reading": "Lesson 5: Vowels and resonance. In singing, this stage focuses on vowels and resonance. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Rhythm and phrasing",
                "reading": "Lesson 6: Rhythm and phrasing. In singing, this stage focuses on rhythm and phrasing. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Vocal range awareness",
                "reading": "Lesson 7: Vocal range awareness. In singing, this stage focuses on vocal range awareness. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Interpretation",
                "reading": "Lesson 8: Interpretation. In singing, this stage focuses on interpretation. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Recording and self-review",
                "reading": "Lesson 9: Recording and self-review. In singing, this stage focuses on recording and self-review. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Prepare a performance",
                "reading": "Lesson 10: Prepare a performance. In singing, this stage focuses on prepare a performance. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in singing.",
                "Practice breath support in a short session.",
                "Complete a first exercise on pitch matching."
        ],
        "Intermediate": [
                "Practice warm-up routines with attention to technique.",
                "Demonstrate progress with vowels and resonance.",
                "Finish a small challenge involving rhythm and phrasing."
        ],
        "Expert": [
                "Analyze and refine vocal range awareness.",
                "Combine techniques while practicing recording and self-review.",
                "Complete and reflect on prepare a performance."
        ]
}
