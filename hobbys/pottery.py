from hobby import Hobby


class Pottery(Hobby):
    """Pottery learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Pottery',
            description='Create decorative or functional objects using clay.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Clay and studio safety",
                "reading": "Lesson 1: Clay and studio safety. In pottery, this stage focuses on clay and studio safety. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Follow studio ventilation, dust, and kiln safety guidance.",
                "video_url": None
        },
        {
                "title": "Wedging clay",
                "reading": "Lesson 2: Wedging clay. In pottery, this stage focuses on wedging clay. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Pinch pots",
                "reading": "Lesson 3: Pinch pots. In pottery, this stage focuses on pinch pots. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Coil building",
                "reading": "Lesson 4: Coil building. In pottery, this stage focuses on coil building. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Slab construction",
                "reading": "Lesson 5: Slab construction. In pottery, this stage focuses on slab construction. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Surface texture",
                "reading": "Lesson 6: Surface texture. In pottery, this stage focuses on surface texture. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Trimming and finishing",
                "reading": "Lesson 7: Trimming and finishing. In pottery, this stage focuses on trimming and finishing. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Glaze fundamentals",
                "reading": "Lesson 8: Glaze fundamentals. In pottery, this stage focuses on glaze fundamentals. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Form and function",
                "reading": "Lesson 9: Form and function. In pottery, this stage focuses on form and function. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Complete a pottery collection",
                "reading": "Lesson 10: Complete a pottery collection. In pottery, this stage focuses on complete a pottery collection. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in pottery.",
                "Practice wedging clay in a short session.",
                "Complete a first exercise on pinch pots."
        ],
        "Intermediate": [
                "Practice coil building with attention to technique.",
                "Demonstrate progress with slab construction.",
                "Finish a small challenge involving surface texture."
        ],
        "Expert": [
                "Analyze and refine trimming and finishing.",
                "Combine techniques while practicing form and function.",
                "Complete and reflect on complete a pottery collection."
        ]
}
