

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98],
       "Developed" : ["No","No","No","No","No"]
       }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

rcs = pd.read_csv("E:/test10rows.csv")
print(rcs)
#print(rcs[[['id','name','rank']]])
print(rcs[4:-2])
