function fearNotLetter (str){
    let missing = "";

    for(let i = 0; i < str.length - 1; i++){
        const currentCode = str[i].charCodeAt(0);
        const nextCode = str[i + 1].charCodeAt(0);

        if((nextCode - currentCode) !== 1){
            missing = String.fromCharCode(currentCode + 1);
            return missing
        }
    }
    return undefined;
}

console.log(fearNotLetter("abce"));