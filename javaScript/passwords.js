//Password generator

function generatePassword (passwordLength){

    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    let result = "";

    for (let i = 0; i < passwordLength; i++)
    {
        const randomIndex = Math.floor(Math.random() * letters.length);
        result += letters[randomIndex];
    }

    return result;
}

const password = generatePassword(10);
console.log(`Generated password: ${password}`);