#!/usr/bin/env python
import pandas as pd

series = pd.Series(["Dave","Chris","Mike","Andy"])
series2 = pd.Series(["Dave","Chris","Mike","Andy"], index = ["C","Java","Networking","Android"])
print(series)
print (series2)
print(series2['C'])
