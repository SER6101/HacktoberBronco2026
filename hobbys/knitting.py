from hobby import Hobby


class Knitting(Hobby):
    """Knitting learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Knitting',
            description='Create scarves, clothing, and handmade accessories.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Yarn and needle selection",
                "reading": "Lesson 1: Yarn and needle selection. In knitting, this stage focuses on yarn and needle selection. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn.",
                "video_url": None
        },
        {
                "title": "Casting on",
                "reading": "Lesson 2: Casting on. In knitting, this stage focuses on casting on. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Knit stitch",
                "reading": "Lesson 3: Knit stitch. In knitting, this stage focuses on knit stitch. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Purl stitch",
                "reading": "Lesson 4: Purl stitch. In knitting, this stage focuses on purl stitch. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Reading patterns",
                "reading": "Lesson 5: Reading patterns. In knitting, this stage focuses on reading patterns. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Gauge swatches",
                "reading": "Lesson 6: Gauge swatches. In knitting, this stage focuses on gauge swatches. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Increases and decreases",
                "reading": "Lesson 7: Increases and decreases. In knitting, this stage focuses on increases and decreases. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Joining and finishing",
                "reading": "Lesson 8: Joining and finishing. In knitting, this stage focuses on joining and finishing. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Pattern customization",
                "reading": "Lesson 9: Pattern customization. In knitting, this stage focuses on pattern customization. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Complete a knitted project",
                "reading": "Lesson 10: Complete a knitted project. In knitting, this stage focuses on complete a knitted project. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in knitting.",
                "Practice casting on in a short session.",
                "Complete a first exercise on knit stitch."
        ],
        "Intermediate": [
                "Practice purl stitch with attention to technique.",
                "Demonstrate progress with reading patterns.",
                "Finish a small challenge involving gauge swatches."
        ],
        "Expert": [
                "Analyze and refine increases and decreases.",
                "Combine techniques while practicing pattern customization.",
                "Complete and reflect on complete a knitted project."
        ]
}
