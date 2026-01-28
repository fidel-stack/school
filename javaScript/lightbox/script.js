const modal = document.querySelector(".lightbox");
const images = document.querySelectorAll(".gallery-item");
const modalImg = document.querySelector("#lightbox-image");
const closeBtn = document.querySelector("#close-btn");

images.forEach(img => {
    img.addEventListener("click", () => {
        modal.style.display = "flex";
        modalImg.src = img.src.replace("-thumbnail", "");
    });
});

closeBtn.onclick = () => {
    modal.style.display = "none";
}

window.onclick = (event) => {
    if (event.target === modal){
        modal.style.display = "none";
    }
}