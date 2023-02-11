# The below code checks if a word has a vowel in letter in it..
word = "brandon"
def check_vowel(a):
    found_vowels = []
    for vowel in word:
        if vowel in 'aeiou':
            found_vowels.append(vowel)
    print("Vowel found:", found_vowels)
       
check_vowel(word)
