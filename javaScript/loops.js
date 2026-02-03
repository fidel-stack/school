//sentence analyser

function getVowelCount(sentence) {
  const vowels = "aeiou";
  let count = 0;

  for (const char of sentence.toLowerCase()) {
    if (vowels.includes(char)) {
      count++;
    }
  }
  return count;
}

const vowelCount = getVowelCount("Apples are tasty fruits");
console.log(`Vowel Count: ${vowelCount}`);

function getConsonantCount(sentence) {
  const consonants = "bcdfghjklmnpqrstvwxyz";
  let count = 0;

  for (const char of sentence.toLowerCase()) {
    if (consonants.includes(char)) {
      count++;
    }
  }
  return count;
}

const consonantCount = getConsonantCount("Coding is fun");
console.log(`Consonant Count: ${consonantCount}`);

function getPunctuationCount(sentence) {
  const punctuations = ".,!?;:-()[]{}\"'–";
  let count = 0;

  for (const char of sentence) {
    if (punctuations.includes(char)) {
      count++;
    }
  }
  return count;
}

const punctuationCount = getPunctuationCount("WHAT?!?!?!?!?");
console.log(`Punctuation Count: ${punctuationCount}`);

function getWordCount(sentence) {
  if (sentence.trim() === '') {
    return 0;
  }
  
  const words = sentence.trim().split(/\s+/);
  return words.length;
}

const wordCount = getWordCount("I love freeCodeCamp");
console.log(`Word Count: ${wordCount}`);

//Longest word finder
function findLongestWordLength(sentence){
  const eachWord = sentence.split(" ");
  let longestWord = "";

  for(let word of eachWord)
  {
    if (word.length > longestWord.length)
    {
      longestWord = word;
    }
  }
  return longestWord.length;
}

console.log(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology"));

//Factorial Calculator
let num = 3;

function factorialCalculator (num){
  let result = 1;
  
  for (let i = 1; i <= num; i++)
  {
    result *= i;
  }
  return result;
}
const factorial = factorialCalculator(num);
const resultMsg = (`Factorial of ${num} is ${factorial}`);
console.log(resultMsg);

//Mutation Algorithm

function mutation (arr){
  let first = arr[0].toLowerCase();
  let second = arr[1].toLowerCase();

  for(let char of second)
  {
    if (!first.includes(char)){
   return false
    }
  }
  return true;
  }
console.log(mutation(["hello", "Hello"]));

//Chuncky monkey algorithm
function chunkArrayInGroups(arr, num){
  const chunkedArray = [];
  for(let i = 0; i < arr.length; i += num)
  {
    const chunk = arr.slice(i, i + num);
    chunkedArray.push(chunk);
  }
  return chunkedArray;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2));

//profile lookup

let contacts = [
  {
    firstName: "Akira",
    lastName: "Laine",
    number: "0543236543",
    likes: ["Pizza", "Coding", "Brownie Points"],
  },
  {
    firstName: "Harry",
    lastName: "Potter",
    number: "0994372684",
    likes: ["Hogwarts", "Magic", "Hagrid"],
  },
  {
    firstName: "Sherlock",
    lastName: "Holmes",
    number: "0487345643",
    likes: ["Intriguing Cases", "Violin"],
  },
  {
    firstName: "Kristian",
    lastName: "Vos",
    number: "unknown",
    likes: ["JavaScript", "Gaming", "Foxes"],
  },
];

function lookUpProfile (name, prop){
  for ( let i = 0; i < contacts.length; i++)
  {
    if (contacts[i].firstName === name)
    {
      if (contacts[i].hasOwnProperty(prop))
      {
        return contacts[i][prop];
      } else
      {
        return "No such property";
      }
    }
  }
  return "No such contact";
}

console.log(lookUpProfile("Kristian", "lastName"));
console.log(lookUpProfile("Kristian", "lastName"));
console.log(lookUpProfile("Sherlock", "likes"));
console.log(lookUpProfile("Akira", "address"))

//str repeat function

function repeatStringNumTimes(str, num){
  let result = "";
  if (num <= 0)
  {
    return result;
  }
  for (let i = 0; i < num; i++)
  {
    result += str;
  }
  return result;
}

console.log(repeatStringNumTimes("*", 3));
console.log(repeatStringNumTimes("abc", -2));

//Missing letter detector

function fearNotLetter(str){
  for (let i = 0; i < str.length -1; i++)
  {
    if(str.charCodeAt(i + 1) - str.charCodeAt(i) > 1)
    {
      return String.fromCharCode(str.charCodeAt(i) + 1);
    }
  }
  return undefined;
}

console.log(fearNotLetter("abcdefj"))