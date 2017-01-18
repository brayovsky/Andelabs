"""
Sort the code first. (I am using bubble sort)
Once the code is sorted make a new list with the first and last element and return it
If max and min are equal returna list with the list length
"""

def find_max_min(some_list):
  """
  a bubble sort will ideally go through the unsorted list comparing each element with the next element
  and swapping if the previous element is greater than the next element. In this way, after the first 
  iteration, the largest element will be at the last index of the list. After the second iteration, the 
  second-largest item will precede the largest item and so on and so forth until the whole list is sorted
  """
  max_and_min = []
  list_length = len(some_list)
  for list_index in range(list_length):
    #compare value of list index and swap until the whole list is done
    for compare_index in range(list_length-1-list_index): #subtract the list_index because after each iteration the last, second-last,third-last etc will be sorted
      if some_list[compare_index]>some_list[compare_index+1] :
        some_list[compare_index],some_list[compare_index+1] = some_list[compare_index+1],some_list[compare_index] #swap
  
  
  if some_list[0]==some_list[list_length-1]:
    list_list_length = [list_length]
    return list_list_length
  else:
    max_and_min.append(some_list[0])
    max_and_min.append(some_list[len(some_list)-1])
    return max_and_min