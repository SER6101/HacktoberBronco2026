
from hobby import Hobby


class Skateboarding(Hobby):

    def __init__(self):

        # Initialize the parent Hobby class
        super().__init__(
            name="Skateboarding",
            description=(
                "Learn skateboard tricks, improve balance, "
                "and explore skateparks."
            )
        )

        # 10-Lesson Roadmap

        # Lessons 1-3: Beginner foundation
        # Lessons 4-6: Intermediate
        # Lessons 7-10: Expert

        self.lessons = [
            {
                "title": "Understanding Your Skateboard",
                "reading": (
                    "A skateboard consists of a deck, trucks, "
                    "wheels, bearings, and grip tape. "
                    "The deck is where you stand. "
                    "Trucks connect the wheels to the deck "
                    "and allow turning. "
                    "Grip tape helps your shoes maintain traction. "
                    "Before riding, inspect your skateboard "
                    "and wear a properly fitted helmet."
                ),
                "video_url": None
            },
            {
                "title": "Finding Your Stance",
                "reading": (
                    "There are two common skateboarding stances. "
                    "Regular stance means your left foot is forward. "
                    "Goofy stance means your right foot is forward. "
                    "Try both positions to find what feels comfortable. "
                    "Practice standing on the skateboard "
                    "while it is stable before attempting to roll."
                ),
                "video_url": None
            },
            {
                "title": "Learning to Push",
                "reading": (
                    "Place your front foot near the front bolts. "
                    "Keep your knees slightly bent. "
                    "Use your back foot to push gently against "
                    "the ground. Start slowly on flat ground "
                    "and practice maintaining your balance."
                ),
                "video_url": None
            },
            {
                "title": "Turning and Stopping",
                "reading": (
                    "Practice gentle turns by shifting your weight "
                    "toward your toes or heels. "
                    "To stop at low speeds, carefully lower "
                    "your back foot to the ground and apply "
                    "gradual pressure. "
                    "Master stopping before increasing your speed."
                ),
                "video_url": None
            },
            {
                "title": "Improving Board Control",
                "reading": (
                    "Practice riding at different comfortable speeds. "
                    "Improve your balance during turns and transitions. "
                    "Focus on smooth movements and maintaining control."
                ),
                "video_url": None
            },
            {
                "title": "Introduction to Ollies",
                "reading": (
                    "An ollie is a foundational skateboarding trick. "
                    "It involves popping the tail, lifting the board, "
                    "and leveling it while airborne. "
                    "Practice the mechanics in a suitable area "
                    "with protective equipment."
                ),
                "video_url": None
            },
            {
                "title": "Kickturns",
                "reading": (
                    "A kickturn allows you to change direction "
                    "by briefly lifting the front wheels. "
                    "Start with small movements on flat ground. "
                    "Gradually improve your balance and control."
                ),
                "video_url": None
            },
            {
                "title": "Advanced Trick Consistency",
                "reading": (
                    "Focus on improving the consistency "
                    "of tricks you already know. "
                    "Analyze foot placement, timing, "
                    "board control, and landing technique."
                ),
                "video_url": None
            },
            {
                "title": "Technical Trick Combinations",
                "reading": (
                    "Learn to connect multiple tricks "
                    "into smooth combinations. "
                    "Practice transitions and consistency "
                    "before increasing technical difficulty."
                ),
                "video_url": None
            },
            {
                "title": "Developing Personal Style",
                "reading": (
                    "Develop a personal skateboarding style "
                    "by experimenting with movements, "
                    "transitions, and combinations "
                    "that match your experience. "
                    "Review your progress and set new goals."
                ),
                "video_url": None
            }
        ]

 
        # Skill Related Quest

        self.quests = {
            "Beginner": [
                "Identify the main parts of your skateboard.",
                "Find your preferred riding stance.",
                "Practice balancing on your skateboard.",
                "Push and roll for 10 meters.",
                "Demonstrate a controlled stop."
            ],

            "Intermediate": [
                "Complete five controlled kickturns.",
                "Practice consistent ollies.",
                "Perform smooth turns while riding.",
                "Complete a basic trick sequence."
            ],

            "Expert": [
                "Refine an advanced trick.",
                "Complete a technical trick combination.",
                "Develop a consistent skatepark line.",
                "Record and review your technique."
            ]
        }
