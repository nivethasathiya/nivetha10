N1 = 11
N2 = 25
  
for value in range(N1, N2 + 1): 
	if value > 1: 
     for n in range(2, value): 
           if (value % n) == 0: 
               break
       else: 
           print(value) 
