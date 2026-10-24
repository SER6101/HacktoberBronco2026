from hobby import Hobby


class PlayingGuitar(Hobby):
    """Playing Guitar learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Playing Guitar',
            description='Learn chords, songs, and music composition.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Guitar parts and tuning",
                "reading": "Lesson 1: Guitar parts and tuning. In playing guitar, this stage focuses on guitar parts and tuning. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Holding the instrument",
                "reading": "Lesson 2: Holding the instrument. In playing guitar, this stage focuses on holding the instrument. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "First chords",
                "reading": "Lesson 3: First chords. In playing guitar, this stage focuses on first chords. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Strumming patterns",
                "reading": "Lesson 4: Strumming patterns. In playing guitar, this stage focuses on strumming patterns. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Chord transitions",
                "reading": "Lesson 5: Chord transitions. In playing guitar, this stage focuses on chord transitions. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Reading tablature",
                "reading": "Lesson 6: Reading tablature. In playing guitar, this stage focuses on reading tablature. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Fingerpicking",
                "reading": "Lesson 7: Fingerpicking. In playing guitar, this stage focuses on fingerpicking. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Rhythm precision",
                "reading": "Lesson 8: Rhythm precision. In playing guitar, this stage focuses on rhythm precision. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Song arrangement",
                "reading": "Lesson 9: Song arrangement. In playing guitar, this stage focuses on song arrangement. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Record a full song",
                "reading": "Lesson 10: Record a full song. In playing guitar, this stage focuses on record a full song. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in playing guitar.",
                "Practice holding the instrument in a short session.",
                "Complete a first exercise on first chords."
        ],
        "Intermediate": [
                "Practice strumming patterns with attention to technique.",
                "Demonstrate progress with chord transitions.",
                "Finish a small challenge involving reading tablature."
        ],
        "Expert": [
                "Analyze and refine fingerpicking.",
                "Combine techniques while practicing song arrangement.",
                "Complete and reflect on record a full song."
        ]
}
