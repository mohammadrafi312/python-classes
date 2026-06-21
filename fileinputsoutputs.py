f=open("/Users/shaik.mohammadrafi/Desktop/python class/python-classes/example.txt", "r")
data=f.read()

for x in data.split(","):
    print(x)