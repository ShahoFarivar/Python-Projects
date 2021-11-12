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


sentence=input("Enter your sentence:\n")
sentenceList=sentence.split(" ")
#print(sentenceList) #del

for word in sentenceList:
  if word[0].lower() in vowels:
    pigLatinList.append(word+vowelString)
  elif word[0] in numbers:
    pigLatinList.append(word)
  else:
    counter=0
    for item in word:
      if item not in vowels:
        counter+=1
      else:
        break
    for i in range(counter,len(word)):
      wordCons+=word[i]
    for k in range(counter):
      wordCons+=word[k]
    wordCons+=consString
    pigLatinList.append(wordCons)
    wordCons=""
       
pigLatin=" ".join(pigLatinList)
print(pigLatin)
