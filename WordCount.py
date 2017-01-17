
def words(sentence):
  all_words = sentence.split()
  number_of_occurrence = {}
  
  for word in all_words:
    try:
      int(word)
      word=int(word)
    except ValueError:
      pass
    #if word in dict add value, else add word to dict with value 1
    if(word in number_of_occurrence):
      number_of_occurrence[word]+=1
    else:
      number_of_occurrence[word]=1
      
  return number_of_occurrence