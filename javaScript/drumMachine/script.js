const drumPads = document.querySelectorAll(".drum-pad");
const display = document.getElementById("display");
const powerBtn = document.getElementById("power-btn");
const volumeSlider = document.getElementById("volume");
const volumeLevel = document.getElementById("volume-level");

let isPoweredOn = true;

function triggerPad(pad) {
  if (!isPoweredOn) {
    return;
  }

  const audio = pad.querySelector(".clip");
  audio.currentTime = 0;
  audio.play();
  display.textContent = pad.id;
}

function animatePad(pad) {
  pad.classList.add("active");
  setTimeout(() => {
    pad.classList.remove("active");
  }, 120);
}

drumPads.forEach(pad => {
  pad.addEventListener("click", () => {
    triggerPad(pad);
    animatePad(pad);
  });
});

document.addEventListener("keydown", (event) => {
  const key = event.key.toUpperCase();

  const allowedKeys = ["Q", "W", "E", "A", "S", "D", "Z", "X", "C"];

  if (allowedKeys.includes(key)) {
    const audio = document.getElementById(key);
    const pad = audio.parentElement;

    triggerPad(pad);
    animatePad(pad);
  }
});

volumeSlider.addEventListener("input", () => {
  const volume = Number(volumeSlider.value);
  volumeLevel.textContent = `${Math.round(volume * 100)}%`;
  document.querySelectorAll(".clip").forEach(audio => {
    audio.volume = volume;
  });
});

powerBtn.addEventListener("click", () => {
  isPoweredOn = !isPoweredOn;

  powerBtn.textContent = isPoweredOn ? "POWER: ON" : "POWER: OFF";
  powerBtn.setAttribute("aria-pressed", String(isPoweredOn));
});