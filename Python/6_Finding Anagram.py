# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word1)==sorted(word2):
       return True
    
    return False
    
word1 = input("Enter First Word: ")
word2 = input("Enter Second Word: ")
print("Are both words anagrams of each other?",find_anagram(word1,word2))