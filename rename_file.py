"list and change file names in a dictory"
import os

path = 'E:\\Data\\test'

for file in os.listdir(path):
    print(file)
    if os.path.isfile(os.path.join(path, file)):
        if file[0:4] == "2016":
            newname = file[0:10] + '.csv'
            os.rename(os.path.join(path, file), os.path.join(path, newname))
            print(file,'ok')
