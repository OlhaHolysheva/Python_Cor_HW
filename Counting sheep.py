array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(sheep):
   return sheep.count(True) and sheep.count(False)
   
              
print((count_sheeps(array1), "There are 17 sheeps in total, not %s" % count_sheeps(array1)))