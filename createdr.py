import os
# from pathlib import Path
# d = os.mkdir("data")
# my_file = Path(d)
# if my_file.is_file():
#     print("exists")
# else:
#     print("does not exists")
from os import listdir
from os.path import isfile, join
print("-"*80)
onlyfiles = [f for f in listdir('data') if isfile(join('data/', f))]
for f in onlyfiles:
    if f.startswith('tanvi') and f.endswith("ndx"):
            
        os.remove("data/" + f)
        print("index file deleted")