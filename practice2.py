import pandas as pd
import re


d = [["ab12", 'albert', 'blake', 79],
     ["def45",  "dana", "feng", 87],
     ["ghi789", "grace", "ichiwa", 92]]

cols = ["netid", "first", "last", "score"]

c = pd.DataFrame(d, columns=cols)
print(c.set_index('netid'))
print(c['netid'])