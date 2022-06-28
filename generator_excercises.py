#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def primes_gen():
    x=1
    while True:
        n+=1
        for num in range(2,n+1):
            #base case of generator
            if n == num :
                yield n 
            #break case to get out of loop
            if n % num == 0:
                break
gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(word):
    while True:
        for x in range(len(word)):
            if word[x] != word[x-1] and word[x+1]:
                x+=1
                yield word[x]
            if word[x] == word[x-1] or word[x+1]:
                break 
for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o