import datetime

li = range(1, 1000000)


start = datetime.datetime.now()


for i in li:
    i = i*10

end=datetime.datetime.now()

print(end,start)
