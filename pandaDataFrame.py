#!/usr/bin/env python

import pandas as pd
import numpy as np

data = {'year':[2010,2011,2012,2013],
        "team":['Bears', 'Lions',
            'Cat','Dog'],
        "win":[11,12,10,1],
        "losses":[1,2,3,1]
        }
football = pd.DataFrame(data)
print (football)
print ()

print(football.dtypes)
print()
print(football.describe)
