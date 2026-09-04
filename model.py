import torch
import torchvision
import numpy
with open("train.csv","rt") as f:
    records = []
    stop = False
    while not stop:
        x = f.readline().split(",")
        if x == [""]:
            stop = True
            break
        if x[-2] == "":
            x[-2] = "0"
        if x[6] == "": #convert male to 0 and female to 1
            x[6] = "29.7"
        if x[5] == "male": #convert male to 0 and female to 1
            x[5] = 0
        else:
            x[5] = 1
        x.pop(3) #remove names
        x.pop(3) 
        x.pop(-2) #remove cabin
        embark = x.pop(-1)
        x.pop(-2) #remove ticket
        if embark== "S\n":
            x.append("0")
            x.append("0")
            x.append("1")
        elif embark == "C\n":
            x.append("0")
            x.append("1")
            x.append("0")
        elif embark == "Q\n":
            x.append("1")
            x.append("0")
            x.append("0")
        else:
            x.append("0")
            x.append("0")
            x.append("0")

        records.append(x)
        
        print(x)
records2 = []
for x in records:

    x = list(map(float,x))#
    if len(x) == 11:
        records2.append(x)
records_np = torch.tensor(records2,dtype= float)
print(records_np.size())
#'print(records)

