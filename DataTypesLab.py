def data_type(data):
  if(type(data)==str):
    return len(data)
  elif(type(data)==type(None)):
    return 'no value'
  elif(type(data)==bool):
    if(data):
      return True
    else:
      return False
  elif(type(data)==int):
    if(data<100):
      return 'less than 100'
    elif(data==100):
      return 'equal to 100'
    elif(data>100):
      return 'more than 100'
  elif(type(data)==list):
    try:
	    data[2]
	    return data[2]
    except Exception, e:
	    return None