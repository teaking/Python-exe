#!/usr/bin/env python 
import numpy
import pandas as pd

d = {
        'one':pd.Series(list(range(4)),
            index =["A", "B","C","D"]), 
        'two':pd.Series(list(range(4,7)),
            index = ["A", "B", "C"])
        }

df = pd.DataFrame(d)
print (df)
print()
print(df.apply(numpy.mean))
print()
print(df['one'].map(lambda x: x >= 2))
print()
print(df.applymap(lambda x: x >= 2))
