//Recipe tracker using JS Objects and more
const recipes = [];

const recipe1 = {
  name: "Spaghetti Carbonara",
  ingredients: ["spaghetti", "Parmesan cheese", "pancetta", "black pepper"],
  cookingTime: 22,
  totalIngredients: null,
  difficultyLevel: ""
};

const recipe2 = {
  name: "Chicken Curry",
  ingredients: ["chicken breast", "coconut milk", "curry powder", "onion", "garlic"],
  cookingTime: 42,
  totalIngredients: null,
  difficultyLevel: ""
};

const recipe3 = {
  name: "Vegetable Stir Fry",
  ingredients: ["broccoli", "carrot", "bell pepper"],
  cookingTime: 15,
  totalIngredients: null,
  difficultyLevel: ""
};

recipes.push(recipe1, recipe2, recipe3);

function getTotalIngredients(ingredients) {
  return ingredients.length;
}

function getDifficultyLevel(cookingTime) {
  if (cookingTime <= 30) {
    return "easy";
  } else if (cookingTime <= 60) {
    return "medium";
  } else {
    return "hard";
  }
}

const recipe1TotalIngredients = getTotalIngredients(recipe1.ingredients);
console.log(recipe1TotalIngredients);

const recipe1DifficultyLevel = getDifficultyLevel(recipe1.cookingTime);
console.log(recipe1DifficultyLevel);

recipe1.totalIngredients = getTotalIngredients(recipe1.ingredients);
recipe1.difficultyLevel = getDifficultyLevel(recipe1.cookingTime);

recipe2.totalIngredients = getTotalIngredients(recipe2.ingredients);
recipe2.difficultyLevel = getDifficultyLevel(recipe2.cookingTime);

recipe3.totalIngredients = getTotalIngredients(recipe3.ingredients);
recipe3.difficultyLevel = getDifficultyLevel(recipe3.cookingTime);

console.log(recipes)

//Quiz game

const questions = [];

const laptop = {
    category: "Workstation",
    question: "What would you prefer?",
    choices: ["MacBook", "Windows", "Linux"],
    answer: "MacBook"
  }

const book = {
    category: "Fiction",
    question: "What would you prefer?",
    choices: ["Fantancy", "Mystery", "Romance"],
    answer: "Fantancy"
}

const phone = {
    category: "Gaming",
    question: "What would you prefer?",
    choices: ["Fodable", "Budget", "Premium"],
    answer: "Fodable"
}

const pen = { 
    category: "School",
    question: "What would you prefer?",
    choices: ["Ballpoint", "Fountain", "Rollerball"],
    answer: "Rollerball"
}

const notebook = {
    category: "Office",
    question: "What would you prefer?",
    choices: ["Spiral", "Tear-off", "Sewn"],
    answer: "Spiral"
}

questions.push(laptop, book, phone, pen, notebook);

function getRandomQuestion(question){
  const randomIndex2 = Math.floor(Math.random() * question.length);
  return question[randomIndex2];
}

function getRandomComputerChoice(choices){
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function getResults (question, getRandomComputerChoice){
  if (question.answer === getRandomComputerChoice)
  {
    return "The computer\'s choice is correct!";
  } else
  {
    return `The computer's choice is wrong. The correct answer is: ${question.answer}`;
  }
}

//Record collection
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

function updateRecords (records, id, prop, value){
  if (value === "")
  {
    delete records [id] [prop];
  } else if (prop === "tracks")
   
  {
    if (!records[id].hasOwnProperty("tracks"))
    {
      records[id][prop] = [];
    }
    records[id][prop].push(value);
  }
   else
   { 
     records[id][prop] = value;
}
return records;
   }

console.log(updateRecords(recordCollection, 1245, "albumTitle", "Riptide"));
console.log(updateRecords(recordCollection, 2548, "tracks", ""), tracks )

