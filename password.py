import random


upper ="ABCDEFGHIJKLOPMQURES"
lower = "abcdefghifical"
numbers = "123456789"
symbols = ";,"
#These are varibles

all = lower + upper + numbers + symbols
length = 20
password = "".join(random.sample(all,length))
print(password)