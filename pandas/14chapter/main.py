# import pandas as pd
# import numpy as np
#
#
# s1 = pd.Series([1,2,3,4,5])
# s2 = pd.Series([6,7,8,9,10])
#
# df = pd.DataFrame({"第1列":s1,"第2列":s2})
# print(df)

import  pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":["tom","jack","alice","bob",'allen'],
        "age":[15,17,20,26,30],
        "score":[60.5,80,30.6,70,83.5]
    }
)

print(df)


