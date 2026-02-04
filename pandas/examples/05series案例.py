
import numpy as np
import pandas as pd

np.random.seed(42)
scores = pd.Series(
    np.random.randint(50,101,10),
    index=['学生' + str(i) for i in range(1,11)],
    name="学生成续单"
)


print("高于平均分的人数",scores[scores > scores.mean()].count())
