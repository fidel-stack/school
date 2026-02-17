const regexPattern = document.getElementById("pattern");
const stringToTest = document.getElementById("test-string");
const testButton = document.getElementById("test-btn");
const testResult = document.getElementById("result");
const caseInsensitiveFlag = document.getElementById("i");
const globalFlag = document.getElementById("g");

function getFlags() {
  let flags = '';
  if (caseInsensitiveFlag.checked) flags += 'i';
  if (globalFlag.checked) flags += 'g';
  return flags;
}
testButton.addEventListener("click", () => {

  const pattern = regexPattern.value;
  const testString = stringToTest.textContent; // always grab clean text
  const flags = getFlags();

  const regex = new RegExp(pattern, flags);

  const matches = flags.includes('g')
    ? [...testString.matchAll(regex)]
    : (testString.match(regex) ? [testString.match(regex)] : []);

  if (matches.length > 0) {

    const highlighted = testString.replace(regex, (match) => {
      return `<span class="highlight">${match}</span>`;
    });

    stringToTest.innerHTML = highlighted;
    testResult.textContent = matches.map(m => m[0]).join(", ");

  } else {
    stringToTest.innerHTML = testString; // reset highlight
    testResult.textContent = "no match";
  }

});
