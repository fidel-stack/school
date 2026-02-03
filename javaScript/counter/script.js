const textarea = document.querySelector("#text-input");
const countEl = document.querySelector("#char-count");

function updateCharCount(){
    if (textarea.value.length > 100){
        textarea.value = textarea.value.slice(0, 100);
    }

    const count = textarea.value.length;
    countEl.textContent = `Character Count: ${count}/100`;

    if (count === 100){
        countEl.classList.add("limit");
    } else {
        countEl.classList.remove("limit");
    }
}
textarea.addEventListener("input", updateCharCount);