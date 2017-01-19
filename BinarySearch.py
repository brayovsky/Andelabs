
class BinarySearch(list):

  # def __new__(cls, list_length,step):
  #   self.list_to_search = range(1,list_length*step,step)
  #   obj = super(BinarySearch, cls).__new__(cls, )
  #   return obj

  def __init__(self,list_length,step):
    self.length = list_length
    super(BinarySearch,self).__init__(self)
    #add the necessary list to the list returned from the superclass
    self+=range(step,(list_length*step)+1,step)
    

  def search(self,val):
    """
    The binary search involves looking for a midpoint in the list and compares if the 
    midpoint is larger than smaller than or equal to and searches another half accordingly.
    Consequently the list MUST be sorted.
    """
    count=0
    start_index = 0
    finish_index = self.length-1
    item_found = False
    #compensate for extra iteration not recorded
    result={"count":0,"index":-1} 

    #if value is out of range, to hell with it
    if val<self[start_index] or val>self[finish_index]:
      return result
    #recursive binary search
    while finish_index>=start_index and not item_found:
      #get midpoint
      mid_index = (start_index+finish_index)//2
      #if its the midpoint,finishing or starting found is true
      if self[mid_index] == val:
        result["index"]=mid_index
        item_found = True
        break
      elif self[finish_index]==val:
        result["index"]=finish_index
        item_found = True
        break
      elif self[start_index]==val:
        result["index"]=start_index
        item_found = True
        break
      elif start_index==finish_index-1:
        break
      else:
        #compare on which half it should lie
        if val>self[mid_index]:
          start_index = mid_index+1
        elif val<self[mid_index]:
          finish_index = mid_index-1
      #add count
      result["count"]+=1
          
    return result
        
if __name__ == "__main__":
  r=BinarySearch(100,10)
  p=r.search(10000)
  print(r)
  print(p)
  # print(r[0])
  # print(r[99])
  # print(r.length)