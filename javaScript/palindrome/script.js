const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const result = document.getElementById("result");

function isPalindrome (str){
  const cleaned = str.replace(/([^a-z0-9])/gi, '').toLowerCase();
  const reversed = cleaned.split('').reverse().join('');

  return cleaned === reversed;
}

checkBtn.addEventListener("click", () => {
  if (textInput.value === ""){
    alert("Please input a value");
    return;
  }
 result.textContent = isPalindrome(textInput.value)
 ? `${textInput.value} is a palindrome.`
 : `${textInput.value} is not a palindrome.`;
  textInput.value = "";
});