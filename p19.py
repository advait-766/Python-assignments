def overlapping(list1, list2):
  for item1 in list1:
    if item1 in list2:
      return True  
  return False 
