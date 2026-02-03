/*
console.log("Hi there!");
console.log("I am excited to talk to you.");
let bot;
bot = "teacherBot";

let botLocation = "the universe";

console.log("Allow me to introduce myself.");

const botIntroduction = "My name is " + bot + ".";
console.log(botIntroduction);

const botLocationSentence = "I live in " + botLocation + ".";
console.log(botLocationSentence);

bot = "professorBot";

const nicknameIntroduction = "My nickname is " + bot + ".";
console.log(nicknameIntroduction);

bot = "awesomeTeacherBot";

const newNicknameGreeting = "I love my nickname but I wish people would call me " + bot + ".";
console.log(newNicknameGreeting);

const favoriteSubject = "Computer Science";

const favoriteSubjectSentence = "My favorite subject is " + favoriteSubject + ".";
console.log(favoriteSubjectSentence);

console.log("Well, it was nice to talk to you. Have a nice day!");

//version 2

console.log("Hello! I'm your coding fun fact guide!");
let botName = "Fidel";
let botlocation = "Space";
let favoriteLanguage = "JavaScript";
console.log("My name is" + " " + botName + " " + "and I live on" + " " + botlocation + ".");
console.log("My favorite programming language is" + " "+ favoriteLanguage + ".")
let codingFact = favoriteLanguage + " was created in just 10 days by Brendan Eich in 1975 and it was originary called Mocha!";
console.log(codingFact);
codingFact = favoriteLanguage + " is the most popular programming language.";
console.log(codingFact);
codingFact = favoriteLanguage + " is my favorite coding language at the moment.";
console.log(codingFact);

console.log(`It was fun sharing these facts with you. Goodbye! - ${botName} from ${botLocation}.`)

//
let adjective = "Proud";
let noun = "Soldier";
let verb = "raining";
let place = "Barrack";
let adjective2 = "big";
let noun2 = "Lasagna";
let firstStory = "Once upon a time, there was a(n) " + adjective + " " + noun + " who loved to eat " + noun2 + ". The " + noun +" lived in a "+ place + " and had " + adjective2 + " nostrils that blew fire when it was "+ verb + ".";
console.log("First story: "+firstStory);
//Second story

adjective = "Pretty";
noun = "Girl";
verb = "bored";
place = "home";
adjective2 = "small";
noun2 = "Pancakes";

let secondStory = "Once upon a time, there was a(n) " + adjective + " " + noun + " who loved to eat " + noun2 + ". The " + noun +" lived in a "+ place + " and had " + adjective2 + " nostrils that blew fire when it was "+ verb + ".";
console.log("Second story: " + secondStory)

//Teacher Bot
console.log("Hi there!");
const botName2 = "teacherBot";

const greeting = `My name is ${botName2}.`;
console.log(greeting);

const subject = "JavaScript";
const topic = "strings";

const sentence = `Today, you will learn about ${topic} in ${subject}.`;
console.log(sentence);

const strLengthIntro = `Here is an example of using the length property on the word ${subject}.`;
console.log(strLengthIntro);

console.log(subject.length);

console.log(`Here is an example of using the length property on the word ${topic}.`);
console.log(topic.length);

console.log(`Here is an example of accessing the first letter in the word ${subject}.`);

console.log(subject[0]);

console.log(`Here is an example of accessing the second letter in the word ${subject}.`);
console.log(subject[1]);

console.log(`Here is an example of accessing the last letter in the word ${subject}.`);

const lastCharacter = subject[subject.length - 1];
console.log(lastCharacter);

const learningIsFunSentence = "Learning is fun.";

console.log("Here are examples of finding the positions of substrings in the sentence.");

console.log(learningIsFunSentence.indexOf("Learning"));

console.log(learningIsFunSentence.indexOf("fun"));
console.log(learningIsFunSentence.indexOf("learning"));

console.log("I hope you enjoyed learning today.")
*/
//Includes() and Slices()
const fccSentence = "freeCodeCamp is a great place to learn web development.";

console.log("Here are some examples of the includes() method:");

const hasFreeCodeCamp = fccSentence.includes("freeCodeCamp");
console.log(`fccSentence.includes("freeCodeCamp") returns ${hasFreeCodeCamp} because the word "freeCodeCamp" is in the sentence.`);

const hasJavaScript = fccSentence.includes("JavaScript");
console.log(`fccSentence.includes("JavaScript") returns ${hasJavaScript} because the word "JavaScript" is not in the sentence.`);

const hasLowercaseFCC = fccSentence.includes("freecodecamp");
console.log(`fccSentence.includes("freecodecamp") returns ${hasLowercaseFCC} because includes is case-sensitive.`);

const message = "Welcome to freeCodeCamp!";

console.log("Here are some examples of the slice() method:");

const platform = message.slice(11, 23);
console.log(`The word "${platform}" was sliced from the message.`);

const greetingWord = message.slice(0, 7);
console.log(`The first word is "${greetingWord}".`);

const endPunctuation = message.slice(-1);
console.log(`The ending punctuation mark is a "${endPunctuation}"`);

console.log("Workshop complete! You now know how to use includes() and slice().")

//String Formatting
const userInput = "   Hello World!   ";
console.log("Original input:");
console.log(userInput);

const cleanedInput = userInput.trim();
console.log("Result of trimming whitespace from both ends:");
console.log(cleanedInput);

const trimmedStart = userInput.trimStart();
console.log("After using the trimStart() method, leading spaces removed:");
console.log(trimmedStart);

const trimmedEnd = userInput.trimEnd();
console.log("After using the trimEnd() method, trailing spaces removed:");
console.log(trimmedEnd);

const upperCaseInput = cleanedInput.toUpperCase();
console.log("Result of using the toUpperCase() method:");
console.log(upperCaseInput);

const lowerCaseInput = cleanedInput.toLowerCase();
console.log("Result of using the toLowerCase() method:");
console.log(lowerCaseInput);

const lowercaseWord = "camelcase";
const camelCasedVersion = lowercaseWord.slice(0, 5) + lowercaseWord[5].toUpperCase()
console.log("Camel cased version:");
console.log(camelCasedVersion);

//STRING TRANSFORMER
const originalString = "I love cats.";
console.log("Original string:");
console.log(originalString);

const replacedString = originalString.replace("cats", "dogs");
console.log("After using the replace() method:");
console.log(replacedString);

const exampleSentence = "I love cats and cats are so much fun!";
console.log("Original sentence:");
console.log(exampleSentence);

const dogsOnlySentence = exampleSentence.replaceAll("cats", "dogs");
console.log("Replacing all occurrences of cats with dogs:");
console.log(dogsOnlySentence);

const learningSentence = "I love learning!";
console.log("Original learning sentence:");
console.log(learningSentence);

const repeatedLove = "love ".repeat(3).trimEnd();
console.log(repeatedLove);

const newSentence = `I ${repeatedLove} learning.`;
console.log(newSentence);

//MATHBOT
const $botName = "MathBot";
const greetings = `Hi there! My name is ${$botName} and I am here to teach you about the Math object!`;

console.log(greetings);

console.log("The Math.random() method returns a pseudo random number greater than or equal to 0 and less than 1.");

const randomNum = Math.random();
console.log(randomNum);

console.log("Now, generate a random number between two values.");

const min = 1;
const max = 100;

const randomNum2 = Math.random() * (max - min) + min;
console.log(randomNum2);

console.log("The Math.floor() method rounds the value down to the nearest whole integer.");

const numRoundedDown = Math.floor(6.7);
console.log(numRoundedDown);

console.log("Now, generate a random integer between two values.");

const randomInt = Math.floor(Math.random() * (max - min) + min);
console.log(randomInt);

console.log("The Math.ceil() method rounds the value up to the nearest whole integer.");

const numRoundedUp = Math.ceil(3.2);
console.log(numRoundedUp);

console.log(
  "The Math.round() method rounds the value to the nearest whole integer."
);

const numRounded = Math.round(2.7);
console.log(numRounded);
const numRounded2 = Math.round(11.2);
console.log(numRounded2);

console.log("The Math.max() and Math.min() methods are used to get the maximum and minimum number from a range.");

const maxNum = Math.max(3, 125, 55, 24);
console.log(maxNum);
const minNum = Math.min(6, 90, 14, 90, 2);
console.log(minNum);

console.log("It was fun learning about the different Math methods with you!")

//FORTUNE TELLER
const fortune1 = "Your cat will look very cuddly today.";

const fortune2 = "The weather will be nice tomorrow.";
const fortune3 = "Be cautious of your new neighbors.";
const fortune4 = "You will find new hobby soon.";
const fortune5 = "It would be nice to avoid the color red today.";

const randomNumber = Math.round(Math.random() * 5) + 1;
//console.log(randomNum);
let selectedFortune = "";
if (randomNumber === 1)
{
  selectedFortune = fortune1;
} else if (randomNumber === 2)
{
 selectedFortune = fortune2;
} else if (randomNumber === 3)
{
  selectedFortune = fortune3;
} else if (randomNumber === 4)
{
  selectedFortune = fortune4; 
} else if(randomNumber === 5)
{
  selectedFortune = fortune5;
}
console.log(selectedFortune);

//function || A calculator

function calculateSum(num1, num2) {
  return num1 + num2;
}

console.log(calculateSum(2, 5));
console.log(calculateSum(10, 10));
console.log(calculateSum(5, 5));

function calculateDifference(num1, num2) {
  return num1 - num2;
}

console.log(calculateDifference(22, 5));
console.log(calculateDifference(12, 1));
console.log(calculateDifference(17, 9));

function calculateProduct(num1, num2) {
  return num1 * num2;
}

console.log(calculateProduct(13, 5));


function calculateQuotient(num1, num2) {
  return num2 === 0 ? "Error: Division by zero" : num1 / num2;
}

console.log(calculateQuotient(7, 11));
console.log(calculateQuotient(3, 0));

function calculateSquare(num) {
  return num ** 2;
}

console.log(calculateSquare(2));
console.log(calculateSquare(9));

function calculateSquareRoot(num) {
  return Math.sqrt(num);
}

console.log(calculateSquareRoot(25));
console.log(calculateSquareRoot(100));

//Boolean checker
function booWho(value){
  return typeof value === "boolean";
}
console.log(booWho(true))

//An email masker
function maskEmail(email){
  const atIndex = email.indexOf("@");
  const username = email.slice(0, atIndex);
  const domain = email.slice(atIndex);
  const firstChar = username[0];
  const lastChar = username[username.length - 1];
  const maskedMiddle = "*".repeat(username.length - 2);
  return firstChar+ maskedMiddle + lastChar + domain;
}
const email = "freecodecamp@gmail.com";
console.log(maskEmail(email))

//Loan Qualification Checker
const minIncomeForDuplex = 60000;
const minCreditScoreForDuplex = 700;

const minIncomeForCondo = 45000;
const minCreditScoreForCondo = 680;

const minIncomeForCar = 30000;
const minCreditScoreForCar = 650;

function getLoanMessage(annualIncome, creditScore) {
  if(creditScore >= minCreditScoreForDuplex && annualIncome >= minIncomeForDuplex) {
    return "You qualify for a duplex, condo, and car loan."
  } else if (annualIncome >= minIncomeForCondo && creditScore >= minCreditScoreForCondo) {
    return "You qualify for a condo and car loan."
  } else if (annualIncome >= minIncomeForCar && creditScore >= minCreditScoreForCar) {
    return "You qualify for a car loan."
  } else {
    return "You don't qualify for any loans."
  }
}

const duplexLoanMsg = getLoanMessage(85000, 850);
const condoLoanMsg = getLoanMessage(65000, 690);
const carLoanMsg = getLoanMessage(45000, 660);
const noLoanMsg = getLoanMessage(25000, 550);

console.log(duplexLoanMsg);
console.log(condoLoanMsg);
console.log(carLoanMsg);
console.log(noLoanMsg);

//Celcius to fahrenheit converter
function convertCtoF(celcius){
  const fahrenheit = celcius * (9/5) + 32;
  return fahrenheit
}
console.log(convertCtoF(30))

//card counter assistance
let count = 0;

function cardCounter(card){
  if (card >= 2 && card <= 6)
  {
    count +=1;
  } else if(card === 10 || card === "J" || card === "K" || card === "Q" || card === "A") {
    count -= 1;
  }
  if (count > 0){
    return count + " Bet";
  } else{
    return count + " Hold";
  }
}
(cardCounter(3));
(cardCounter(2));
(cardCounter("A"));
(cardCounter(10));
console.log(cardCounter("K"))


//leap year calculator
function isLeapYear(year){
  if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0))
  {
    return `${year} is a leap year.`;
  } else{
    return `${year} is not a leap year.`
  }
}
let year = 2028;
let result = isLeapYear(year);
console.log(result);

//truncate string algorithm
function truncateString(string, length){
  if (string.length > length)
  {
    return string.slice(0, length ) + "...";
  } else {
    return string ;
  }
}
console.log(truncateString("A white boy under the mat.", 5));

//confrim the ending tool

function confirmEnding(str, end){
  if (str.slice(-end.length) === end)
  {
    return true;
  } else
  {
    return false;
  }
}
console.log(confirmEnding("open saseme", "seme"))

//Arrays
console.log("Grocery shopping list");

const shoppingList = [];

console.log("It will be nice to have some fruit to eat.");

shoppingList.push("Apples");

function getShoppingListMsg(arr) {
  return `Current Shopping List: ${arr}`;
}

console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Grapes");
console.log(getShoppingListMsg(shoppingList));

console.log("It looks like we need to get some cooking oil.");

shoppingList.unshift("Vegetable Oil");
console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Popcorn", "Beef Jerky", "Potato Chips");
console.log(getShoppingListMsg(shoppingList));

console.log("This looks like too much junk food.");

shoppingList.pop();
console.log(getShoppingListMsg(shoppingList));

console.log("It might be nice to get a dessert.");

shoppingList.unshift("Chocolate Cake");
console.log(getShoppingListMsg(shoppingList));

console.log("On second thought, maybe we should be more health conscious.");

shoppingList.shift();
shoppingList[0] = "Canola Oil";

console.log(getShoppingListMsg(shoppingList));

//lunch picker
let lunches = [];
function addLunchToEnd(arr, str){
  arr.push(str);
  console.log(`${str} added to the end of the lunch menu.`);
  return arr;
}

function addLunchToStart (arr, str){
  arr.unshift(str);
  console.log(`${str} added to the start of the lunch menu.`);
  return arr;
}

function removeLastLunch (arr){
  if (arr.length > 0){
    const removed = arr.pop()
  console.log(`${removed} removed from the end of the lunch menu.`);
  return arr;
  } else
  console.log("No lunches to remove.");
  return arr;
}

function removeFirstLunch (arr){
  if (arr.length > 0)
  {
    const removed = arr.shift()
    console.log(`${removed} removed from the start of the lunch menu.`)
  return arr;
  } else
  {
    console.log("No lunches to remove.")
    return arr;
  }
}
function getRandomLunch (arr){
  if (arr.length > 0)
  {
    const randomIndex = Math.floor(Math.random() * arr.length);
  console.log(`Randomly selected lunch: ${arr[randomIndex]}`)
} else 
{
  console.log("No lunches available.")
  return arr;
}
}

function showLunchMenu(arr){
  if (arr.length > 0)
  {
    console.log(`Menu items: ${arr.join(", ")}`);
    return arr;
  } else (arr.length === 0)
  {
    console.log("The menu is empty.");
    return arr;
  }
}

console.log(addLunchToEnd(lunches, "Tacos"));
console.log(addLunchToEnd(["Pizza", "Tacos"], "Burgers"));
console.log(addLunchToStart(lunches, "Sushi"));
console.log(addLunchToEnd(["Burger", "Sushi"], "Pizza"));
console.log(removeLastLunch(["Stew", "Soup", "Toast"]));
console.log(removeLastLunch(["Sushi", "Pizza", "Noodles"]));
console.log(removeFirstLunch(["Salad", "Eggs", "Cheese"]));
console.log(getRandomLunch(["pizza", "burger", "salad"]));
console.log(showLunchMenu(["pizza", "apples"]))

//Golf score translator
const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore (par, strokes){
  if (strokes === 1)
  {
    return "Hole-in-one!";
  } else if (strokes <= (par - 2))
  {
    return "Eagle";
  } else if (strokes === (par - 1))
  {
    return "Birdie";
  } else if (strokes === (par))
  {
    return "Par";
  } else if (strokes === (par + 1))
  {
    return "Bogey";
  } else if (strokes === (par + 2))
  {
    return "Double Bogey";
  } else if (strokes >= (par + 3))
  {
    return "Go Home!";
  }
}
console.log(golfScore(3, 1))