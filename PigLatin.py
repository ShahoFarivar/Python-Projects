# Pig Latin
'''If a word begins with a vowel, the word yay is added to the end of it. 
If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay. '''

vowels = "aeiou"
vowelString="yay"
consString="ay"
numbers="0123456789"
pigLatinList=[]
pigLatin=""
wordCons=""
wordSign=""

sentence=input("Enter your sentence:\n")
sentenceList=sentence.split(" ")

for word in sentenceList:
  #check not alphabetics:
  if not word[-1].isalpha():
    wordSign=word[-1]
    word=word[:-1]
    print(wordSign,"--",word)
  #check if start with vowel
  if word[0].lower() in vowels:
    pigLatinList.append(word+vowelString+wordSign)
  #check if start with numbers
  elif word[0] in numbers:
    word+=wordSign
    pigLatinList.append(word)
  #check if start with consonant cluster
  else:
    counter=0
    for item in word:
      if item not in vowels:
        counter+=1
      else:
        break
    #finding first vowel and words after it
    for i in range(counter,len(word)): 
      wordCons+=word[i]
    #finding consonant cluster
    for k in range(counter):
      wordCons+=word[k]
    wordCons+=consString
    wordCons+=wordSign
    pigLatinList.append(wordCons)
    wordCons=""
  wordSign=""
  
       
pigLatin=" ".join(pigLatinList)
print(pigLatin)
