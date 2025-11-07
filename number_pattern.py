def number_pattern(n):
    if not isinstance(n, int):
        return("Argument must be an integer value.")
    if n < 1:
        return("Argument must be an integer greater than 0.")
    number_list = [] 
    for i in range(1, n + 1):
        number_list.append(str(i))  
    return " ".join(number_list)                 
print(number_pattern(4)) #Expected output: "1 2 3 4" 