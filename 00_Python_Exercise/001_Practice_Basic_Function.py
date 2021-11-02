
from random import *

address = "http://naver.com"
print(address)

# r규칙 1
address = address.replace("http://", "")
print(address)

# r규칙 2
PointIndex = address.find(".")
address = address[0:PointIndex]
print(address)

address = str(address[0:3]) + str(len(address)) + str(address.count("e")) + "!"
# r규칙 3
print(address)
