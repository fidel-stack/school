
const detectBtn = document.getElementById("detectBtn");
const moodResult = document.getElementById("moodResult");
const musicPlayer = document.getElementById("musicPlayer");

// Simulated moods & corresponding music
const moods = {
  happy: "music/happy.mp3",
  sad: "music/sad.mp3",
  energetic: "music/energetic.mp3",
  calm: "music/calm.mp3"
};

// Randomly simulate mood detection
function detectMood() {
  const moodKeys = Object.keys(moods);
  const randomMood = moodKeys[Math.floor(Math.random() * moodKeys.length)];
  
  moodResult.innerText = `Detected mood: ${randomMood.toUpperCase()}`;
  musicPlayer.src = moods[randomMood];
  musicPlayer.play();
}

detectBtn.addEventListener("click", detectMood);

