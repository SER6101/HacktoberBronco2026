from .hobby import Hobby


class Hiking(Hobby):
    """Hiking learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Hiking',
            description='Explore nature and stay physically active.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Trail safety and gear",
                "reading": "Lesson 1: Trail safety and gear. In hiking, this stage focuses on trail safety and gear. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Check conditions and tell someone your route; stay on designated trails.",
                "video_url": None
        },
        {
                "title": "Reading trail signs",
                "reading": "Lesson 2: Reading trail signs. In hiking, this stage focuses on reading trail signs. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Planning a short walk",
                "reading": "Lesson 3: Planning a short walk. In hiking, this stage focuses on planning a short walk. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Pacing and hydration",
                "reading": "Lesson 4: Pacing and hydration. In hiking, this stage focuses on pacing and hydration. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Navigating intersections",
                "reading": "Lesson 5: Navigating intersections. In hiking, this stage focuses on navigating intersections. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Weather and terrain",
                "reading": "Lesson 6: Weather and terrain. In hiking, this stage focuses on weather and terrain. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Longer route planning",
                "reading": "Lesson 7: Longer route planning. In hiking, this stage focuses on longer route planning. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Elevation strategy",
                "reading": "Lesson 8: Elevation strategy. In hiking, this stage focuses on elevation strategy. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Leave No Trace leadership",
                "reading": "Lesson 9: Leave No Trace leadership. In hiking, this stage focuses on leave no trace leadership. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Design a hiking itinerary",
                "reading": "Lesson 10: Design a hiking itinerary. In hiking, this stage focuses on design a hiking itinerary. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in hiking.",
                "Practice reading trail signs in a short session.",
                "Complete a first exercise on planning a short walk."
        ],
        "Intermediate": [
                "Practice pacing and hydration with attention to technique.",
                "Demonstrate progress with navigating intersections.",
                "Finish a small challenge involving weather and terrain."
        ],
        "Expert": [
                "Analyze and refine longer route planning.",
                "Combine techniques while practicing leave no trace leadership.",
                "Complete and reflect on design a hiking itinerary."
        ]
}
