//hambuger menu
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("open");
  hamburger.setAttribute("aria-expanded", isOpen);
});

// Close menu when link is clicked
document.querySelectorAll(".nav-links a").forEach(link => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    hamburger.setAttribute("aria-expanded", "false");
  });
});

//Form for data input
      const form = document.getElementById("contact-form");
      const popup = document.getElementById("popup");
      const closeBtn = document.getElementById("close-btn");
      const submitBtn = document.getElementById("sendBtn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  submitBtn.disabled = true;
  submitBtn.textContent = "Sending...";

  try {
    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" }
    });

    if (response.ok) {
      form.reset();
      popup.style.display = "flex";
    } else {
      alert("Something went wrong. Please try again.");
    }
  } catch {
    alert("Network error. Try again later.");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Send";
  }
});
  closeBtn.addEventListener("click", () => {
    popup.style.display = "none";
  });