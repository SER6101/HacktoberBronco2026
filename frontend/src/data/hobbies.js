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

// Questions, recommendations and 10-node lesson roadmaps come from FastAPI.
// This file only provides optional visual metadata for hobby cards.
export const skillDescriptions = {
  Beginner: "I'm new to this and want to learn the basics.",
  Intermediate: "I know the basics and want to build my skills.",
  Expert: "I'm experienced and ready for advanced lessons.",
};
