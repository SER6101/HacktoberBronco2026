from hobby import Hobby


class Camping(Hobby):
    """Camping learning roadmap for HobBob."""

    def __init__(self):
        super().__init__(
            name='Camping',
            description='Spend time outdoors and learn basic camping skills.'
        )

        # One shared 10-node roadmap; skill level chooses the starting node.
        self.lessons = [
        {
                "title": "Campsite safety",
                "reading": "Lesson 1: Campsite safety. In camping, this stage focuses on campsite safety. Identify the key tools, safety considerations, and vocabulary involved. Write down two things you already know and one thing you want to learn. Follow local fire rules and check weather and emergency plans.",
                "video_url": None
        },
        {
                "title": "Essential gear",
                "reading": "Lesson 2: Essential gear. In camping, this stage focuses on essential gear. Work through a simple example slowly. Pay attention to the details and repeat the basic movement or idea until it feels familiar.",
                "video_url": None
        },
        {
                "title": "Choosing a campsite",
                "reading": "Lesson 3: Choosing a campsite. In camping, this stage focuses on choosing a campsite. Try a short low-pressure practice session. Note what worked, what was confusing, and one question to revisit.",
                "video_url": None
        },
        {
                "title": "Tent setup",
                "reading": "Lesson 4: Tent setup. In camping, this stage focuses on tent setup. Break the technique into smaller parts. Practice each part separately before combining them into a short exercise.",
                "video_url": None
        },
        {
                "title": "Food and water safety",
                "reading": "Lesson 5: Food and water safety. In camping, this stage focuses on food and water safety. Use a repeatable routine to build control. Compare two attempts and notice which small adjustment helped.",
                "video_url": None
        },
        {
                "title": "Weather preparedness",
                "reading": "Lesson 6: Weather preparedness. In camping, this stage focuses on weather preparedness. Apply the technique to a small, achievable challenge. Record the result and choose one improvement for next time.",
                "video_url": None
        },
        {
                "title": "Navigation and emergency plan",
                "reading": "Lesson 7: Navigation and emergency plan. In camping, this stage focuses on navigation and emergency plan. Analyze an example carefully. Explain why the approach works and identify a variation you could safely try.",
                "video_url": None
        },
        {
                "title": "Low-impact camping",
                "reading": "Lesson 8: Low-impact camping. In camping, this stage focuses on low-impact camping. Plan a more demanding practice task. Set a measurable goal, review your results, and adjust your method.",
                "video_url": None
        },
        {
                "title": "Trip logistics",
                "reading": "Lesson 9: Trip logistics. In camping, this stage focuses on trip logistics. Combine several skills into a coherent project or session. Ask for feedback when appropriate and refine one detail.",
                "video_url": None
        },
        {
                "title": "Plan an overnight trip",
                "reading": "Lesson 10: Plan an overnight trip. In camping, this stage focuses on plan an overnight trip. Review the full journey, document your strongest work, and set a realistic next goal to continue developing your skills.",
                "video_url": None
        }
]

        # Skill-specific challenges for the right sidebar.
        self.quests = {
        "Beginner": [
                "Identify the basic tools or ideas used in camping.",
                "Practice essential gear in a short session.",
                "Complete a first exercise on choosing a campsite."
        ],
        "Intermediate": [
                "Practice tent setup with attention to technique.",
                "Demonstrate progress with food and water safety.",
                "Finish a small challenge involving weather preparedness."
        ],
        "Expert": [
                "Analyze and refine navigation and emergency plan.",
                "Combine techniques while practicing trip logistics.",
                "Complete and reflect on plan an overnight trip."
        ]
}
