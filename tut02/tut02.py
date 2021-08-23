#AJAY NAIK 1901me14
def get_memory_score(input_list):
  l_2=[]
  count=0
  for x in input_list:
     if x in l_2:
      count+=1
     else:
      l_2.append(x)
      if len(l_2)==6:
         l_2.remove(l_2[0])
  return count

def is_digit(input_list2):
  invalid_l2=[]
  ok=True
  for x in input_list2:
    if type(x)==int and x<10 and x>=0:
      continue
    else:
      invalid_l2.append(x)
      ok=False
  
  if ok:
   return True
  else:
   print ("Please enter a valid input list")
   print ("Invalid inputs detected:", invalid_l2)
   return False

input_list=[3,4,5,3,2,1,6,6,6,9,5]
s=is_digit(input_list)
if s:
  print ("Score:",get_memory_score(input_list))


   