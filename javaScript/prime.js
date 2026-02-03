function isPrime(num){
    if(num < 2) return false;
    if(num === 2) return true;
    if(num % 2 === 0) return false;

    const limit = Math.floor(Math.sqrt(num));

    for(let i = 3; i <= limit; i += 2)
    {
        if(num % i === 0)
        {
            return false
        }
    }

    return true;
}

function sumPrimes(number){
    let sum = 0;

    for(let i = 0; i <= number; i++)
    {
        if(isPrime(i))
        {
            sum += i;
        }
    }

    return sum;
}

console.log(isPrime(2)); //true
console.log(sumPrimes(22)); //sums up all prime numbers less or equal to 20

//Range based calculator
function gcd(a, b){
    if(b === 0)
    {
        return a;
    }

    return (gcd(b, a % b));
}

function lcm(a, b){
    return Math.abs(a * b) / gcd(a, b);
}

function smallestCommons(arr){
    const min = Math.min(...arr);
    const max = Math.max(...arr);
    let currentLCM = min;

    for(let i = min + 1; i <= max; i++)
    {
        currentLCM = lcm(currentLCM, i);
    }

    return currentLCM;
};

//deep flattening tool
function steamrollArray(arr){
  let result = [];
  arr.forEach(item =>{
    if( Array.isArray(item)){
      result = result.concat(steamrollArray(item));
    } else {
      result.push(item);
    }
  });
  return result;
}
console.log(steamrollArray([[["a"]], [["b"]]])) //[a, b]