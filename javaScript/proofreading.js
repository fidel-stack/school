function isPalindrome (word){
  const myWord = word.toLowerCase();
  const palindrome = myWord.split('').reverse().join('');

  return myWord === palindrome;
}

console.log(isPalindrome('racecar'));

function findPalindromeBreaks(words){
  const indices = [];
  for (let i = 0; i < words.length; i++){
    if(!isPalindrome(words[i])){
      indices.push((i))
    }
  }
  return indices;
}
console.log(findPalindromeBreaks([
  "abacus", "racecar", "crazy", "doctor", "escape", "madam", 
  "refer", "rotor","fragile", 
  "guitar", "horizon", "island", "jungle", "kitchen", "lemon", 
  "mystery", "stats", "tenet", "wow", "nebula", "ocean", 
  "level", "radar", "civic", "deed", "kayak",  "sagas", "solos"
]));

function findRepeatedPhrases(words, phraseLength){
  const startIndices = [];
  const seen = {};
  if(phraseLength >= words.length){
    return [];
  }
  for (let i = 0; i <= words.length - phraseLength; i++){
    const phrases = words.slice(i, i + phraseLength);
    const phrase = phrases.join(' ');

    if (seen[phrase] !== undefined){
      startIndices.push(i);
      if(!startIndices.includes(seen[phrase])){
        startIndices.push(seen[phrase]);
      }
    } else {
      seen[phrase] = i;
    }
    
  }
  return startIndices.sort((a, b) => a - b);

}
console.log(findRepeatedPhrases(["the", "cat", "sat", "the", "cat"], 2));

function analyzeTexts(texts, phraseLength){
  if (texts.length === 0){
    return [];
  }
  const results = [];
  for (let i = 0; i < texts.length; i++){
    const repeatedPhrases = findRepeatedPhrases(texts[i], phraseLength);
    const palindromeBreaks = findPalindromeBreaks(texts[i], phraseLength);
    results.push({
      repeatedPhrases: repeatedPhrases,
      palindromeBreaks: palindromeBreaks
    })
  }
  return results;
}
const texts = [
  ["the", "cat", "sat", "the", "cat"],

  ["racecar", "level", "hello", "madam"],

  ["one", "two", "one", "two", "three", "one", "two"]
];

const phraseLength = 2;

console.log(analyzeTexts(texts, phraseLength));