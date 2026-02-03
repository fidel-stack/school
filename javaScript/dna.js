//Implement a DNA pair generator

function pairElement (mySty){
    const basePair = {
        A: "T",
        T: "A",
        C: "G",
        G: "C"
    }

    return mySty.split("").map((letter => [letter, basePair[letter]]));
}

//console.log(pairElement("ATCGA"));

//Implement a HTML entity converter

function convertHTML (myStr){
    const characters = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
  }

  return myStr.split('').map(character => characters[character]).join('');
}

console.log(convertHTML('Stuff in "quotation marks"'))

//Odd Fibonacci calculator

function sumFibs(number){

  if (number < 1) return 0;
  let a = 1;
  let b = 1;

  let sum = 2;

  while (true)
  {
    let next = a + b;

    if (next > number) break;

    if (next % 2 !== 0)
    {
      sum += next;
    }

    a = b;
    b = next;
  }
  return sum;
}

console.log(sumFibs(1000));

//Implement an element skipper

function dropElements (arr, func){

  for (let i = 0; i < arr.length; i++)
  {
    if(func(arr[i]))
    {
      return arr.slice(i);
    }
  }
  return [];
}

//implement a sorted index finder
//the function returns lowest index at which a value should be inserted

function getIndexToIns (arr, number){
  const sorted = [...arr].sort((a, ) => a - b);

  for(let i = 0; i < sorted.length; i++)
  {
    if(number <= sorted[i])
      return i;
  }

  return sorted.length;
}

//symetric diffrence function

function diffArray(arr1, arr2){

  //creating sets of elements in both arrays
  const setA = new Set(arr1);
  const setB = new Set(arr2);

  //filter elements in arr1 not in arr2
  const diffA = arr1.filter(item => !setB.has(item));
  const diffB = arr2.filter(item => !setA.has(item));
  
  return [new Set([...diffA, ...diffB])];
}

console.log(diffArray(["diamond", "stick", "apple"], ["stick", "emerald", "bread"]));
//returns [ 'diamond', 'apple', 'emerald', 'bread' ]

//value remover function
function destroyer(arr, ...others){
  return arr.filter(value => !others.includes(value));
}
console.log(destroyer([1, 2, 3, 1], 2, 3));
//returns [1, 1]

//matching object filter
function whatIsInAName(arr, source){
  const sourceKeys = Object.keys(source);

  return arr.filter(item =>{
    return sourceKeys.every(key =>{
      return item[key] === source[key];
    })
  })
}