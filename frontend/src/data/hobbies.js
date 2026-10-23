export const questions = [
  { prompt: "What would you like a hobby to bring to your life?", choices: ["A chance to relax", "A new skill", "More movement", "A creative outlet"] },
  { prompt: "How do you like to spend your free time?", choices: ["Making things", "Exploring", "Solving problems", "Being active"] },
  { prompt: "What kind of setting sounds good?", choices: ["On my own", "With a small group", "Meeting new people", "A bit of everything"] },
];

export const hobbies = [
  { name: "Drawing", category: "Creative", icon: "✎", description: "Practice sketching and bring your ideas to life." },
  { name: "Hiking", category: "Outdoors", icon: "⌁", description: "Find new trails and enjoy time outside." },
  { name: "Cooking", category: "Creative", icon: "◒", description: "Build kitchen confidence one recipe at a time." },
  { name: "Photography", category: "Creative", icon: "◉", description: "Learn to notice and capture the little details." },
  { name: "Gardening", category: "Outdoors", icon: "❋", description: "Grow something green, from herbs to flowers." },
  { name: "Playing Guitar", category: "Music", icon: "♫", description: "Learn chords and play songs you love." },
  { name: "Chess", category: "Strategy", icon: "♞", description: "Explore patterns, tactics, and thoughtful play." },
  { name: "Pottery", category: "Creative", icon: "◡", description: "Shape clay into useful and beautiful objects." },
  { name: "Cycling", category: "Movement", icon: "⟲", description: "Build confidence and explore on two wheels." },
];

const beginnerRoadmap = [
  ["Take your first step", "10 min", "Set up a small, welcoming space to begin.", "Start simple: gather what you already have, pick one tiny goal, and give yourself permission to learn as you go."],
  ["Learn the foundations", "20 min", "Get to know the core tools, terms, and techniques.", "Choose one beginner-friendly technique and practice it slowly. Repetition builds confidence more than getting it perfect."],
  ["Practice a little", "30 min", "Try a short practice session and notice what you enjoy.", "Set a timer for a short session. Focus on the process, and jot down one thing you learned afterward."],
  ["Make your first project", "45 min", "Bring the pieces together in a small project you can finish.", "Pick a project that fits in one session. Keep the goal achievable and make it your own as you work."],
  ["Find your own style", "Ongoing", "Keep exploring, try a new challenge, and choose what to learn next.", "Look back at what you enjoyed most. Use that as a guide for choosing your next skill, project, or community."],
];

export const skillDescriptions = {
  Beginner: "I’m new to this and want to learn the basics.",
  Intermediate: "I know a little already and want to build my skills.",
  Expert: "I’m experienced and ready to refine or challenge myself.",
};

export const skillRoadmaps = {
  Beginner: beginnerRoadmap,
  Intermediate: [
    ["Refresh your foundations", "15 min", "Review the core techniques and identify what you want to improve.", "Choose one familiar technique. Notice what already feels comfortable and where a small adjustment could make it stronger."],
    ["Build a stronger technique", "25 min", "Practice a technique that adds control and consistency.", "Work slowly through a more challenging variation. Focus on precision, and repeat it a few times to find a rhythm."],
    ["Explore a new approach", "30 min", "Try a different method and compare it with what you already know.", "Pick an approach you have not tried before. Keep notes about what feels different and what you would use again."],
    ["Create a personal project", "45 min", "Plan and complete a project that combines the skills you have practiced.", "Set a clear goal for your project, then make a quick plan. Leave room to experiment as you work."],
    ["Set your next challenge", "Ongoing", "Choose a direction for continued practice and growth.", "Reflect on the project you just completed. Pick one skill to deepen and make a simple plan for practicing it."],
  ],
  Expert: [
    ["Choose a stretch goal", "15 min", "Set a specific challenge that pushes your current practice.", "Pick a goal just beyond your comfort zone. Define what success looks like, and break the challenge into manageable parts."],
    ["Refine your technique", "30 min", "Analyze your process and focus on one detail to improve.", "Choose a specific detail to refine. Practice deliberately, review the results, and adjust your approach as you go."],
    ["Experiment with a new approach", "30 min", "Test an unfamiliar method, tool, or style.", "Set up a small experiment: change one variable in your usual approach and observe what it makes possible."],
    ["Complete an ambitious project", "60 min", "Bring your skills together in a project with a meaningful challenge.", "Break the project into milestones. Review your progress at each stage and adapt your plan when you learn something new."],
    ["Share what you have learned", "Ongoing", "Reflect on your progress and choose how you want to contribute or grow.", "Document your process, share a tip with someone else, or choose a new long-term challenge to keep your practice evolving."],
  ],
};
