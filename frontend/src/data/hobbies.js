export const questions = [
  { question: "What do you hope to gain from a hobby?", options: ["Relaxation", "Learning", "Fitness", "Creativity"] },
  { question: "What activities do you enjoy?", options: ["Creating", "Exploring", "Problem solving", "Physical activities"] },
  { question: "How do you prefer spending free time?", options: ["Alone", "Small group", "Meeting people", "Either"] },
  { question: "What is your starting budget?", options: ["Free", "Under $25", "$25-$100", "Over $100"] },
  { question: "How much time do you have each week?", options: ["Under 2 hours", "2-5 hours", "5-10 hours", "Over 10 hours"] },
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
