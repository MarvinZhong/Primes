def Finding(Prime): #statement for finding primes
    x = 2 #x start value
    while x <= Prime/2 : #term for Prime
        if Prime % x == 0 : #checking it's prime or not
            return False #false
        x += 1 #x + 1
    return True #true
n = int(input()) #input n's value
Prime = 2 #start Prime Value
result = 0 #Start result value
while Prime <= n : #term for get prime
    if Finding(Prime) : #get in to statement
        result += 1 #result + 1
    Prime += 1 #Prime + 1
print(result) #print out the result
