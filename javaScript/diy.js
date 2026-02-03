//Build a string inverter (reverse)
function stringReverse (str){
    return str.split("").reverse().join("");
}
console.log(stringReverse("Greetings From Earth"));

//build a Largest Number Finder

function largestOfAll(arr){
    const largestNumber = [];

    for (let i = 0; i < arr.length; i++)
    {
        let largestNumInSubArray = -Infinity;
        const subArray = arr[i];

        for (let j = 0; j < subArray.length; j++)
        {
            if (subArray[j] > largestNumInSubArray)
            {
                largestNumInSubArray = subArray[j];
            }
        }
        largestNumber.push(largestNumInSubArray)
    }
    return largestNumber;
}
console.log(largestOfAll([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));

//First word finder
function findElement (arr, func){
    return arr.find(func);
}

//Implimenting slice and splice algorithm

function frankenSplice (arr1, arr2, index){
    let result = arr2.slice();

    for (let i = 0; i < arr1.length; i++)
    {
        result.splice(index + i, 0, arr1[i]);
    }

    return result;
}

console.log(frankenSplice([1, 2, 3], [4, 5], 1));

//Pyramid generator

function Pyramid (character, rowCount, isCentered){

    let result = "\n";

    if (isCentered === false)
    {
        for (let i = 1; i <= rowCount; i++)
        {
            const spaces = " ".repeat(rowCount - i);
            const chars = character.repeat(2 * i - 1)

            result += spaces + chars + "\n";
        }
    } else
    {
        for (let i = rowCount; i >= 1; i--)
        {
            const spaces = " ".repeat(rowCount - i);
            const chars = character.repeat(2 * i - 1);

            result += spaces + chars + "\n";
        }
    }
}

console.log(Pyramid("*", 4, false));

//Build a grade book app
function getAverage (arr){
  let sum = 0;
  for (const number of arr)
  {
    sum += number;
  }
  return sum / arr.length;
}

console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));

function getGrade (score){
  if (score === 100) return "A+";
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

console.log(getGrade(40));

function hasPassingGrade (score){
  return getGrade(score) !== "F";
}

console.log(hasPassingGrade(80));

function studentMsg (arr, score){
  const hasPassed = getAverage(arr);
  const studentGrade = getGrade(score)
  const passed = hasPassingGrade(score);
  if (passed)
  {
  return `Class average: ${hasPassed}. Your grade: ${studentGrade}. You passed the course.`;
  } else
  {
    return `Class average: ${hasPassed}. Your grade: ${studentGrade}. You failed the course.`
  }
}

console.log(studentMsg([15, 25, 35, 45, 55, 60, 70, 60], 60));

//Title converter

function titleCase (sentence){
    const words = sentence.split(" ");

    for (let i = 0; i < words.length; i++)
    {
        if (words.length > 0)
        {
            words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
        }
    }
    return words.join(" ");
}

console.log(titleCase("This is my code.")) //This Is My Code.

//Falsy remover

function bouncer (originalArr){
    const truthyArr = originalArr.filter(Boolean);

    return truthyArr;
}

//Inventory management program

const inventory = [];


function findProductIndex (name){
const productName = name.toLowerCase();
return inventory.findIndex(item => item.name === productName)
}

function addProduct (product){
  const name = product.name.toLowerCase();
  const index = findProductIndex(name);

  if (index !== -1)
  {
    inventory[index].quantity += product.quantity;
    console.log(`${name} quantity updated`)
  } else
  {
    inventory.push({name, quantity: product.quantity });
    console.log(`${name} added to inventory`)
  }
}

function removeProduct (productName, quantity){
  const name = productName.toLowerCase();
  const index = findProductIndex(name);

  

  if (index === -1)
  {
    console.log(`${name} not found`)
    return;
  }  

    const product = inventory[index];
    
    if (product.quantity < quantity)
    {
      console.log(`Not enough ${name} available, remaining pieces: ${product.quantity}`)
      return;
    }


      product.quantity -= quantity;
      if (product.quantity === 0)
      {
        inventory.splice(index, 1)
      } else
      {
  console.log(`Remaining ${name} pieces: ${product.quantity}`);
  }
}


console.log(findProductIndex("flour"));
console.log(removeProduct("FLOUR", 10));

//Implimenting a unique sorted union

function uniteUnique (...arrays){
  const results = [];

  for(const arr of arrays)
  {
    for (const value of arr)
    {
      if (!results.includes(value))
      {
        results.push(value);
      }
    }
  }

}

//Design a Sum all Numbers
//adds numbers the range of a given array

function sumAll (arr){

  const minNum = Math.min(...arr);
  const maxNum = Math.max(...arr);

  let sum = 0;

  const rangeArr = [];
  for (let i = minNum; i <= maxNum; i++)
  {
    sum =+ i;
    rangeArr.push(i);
  }
  return sum;
}

//Implement a DNA pair generator

function pairElement(myStr){
  const basepair = {
    A: "T",
    T: "A",
    C: "G",
    G: "T"
  }

  return myStr.split("").map((letter => [letter, basepair[letter]]));
}