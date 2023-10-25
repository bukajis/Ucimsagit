import os

x = 123
d=os.listdir("")
print(d)
y = "abc"
z = 123.4567
print(f"{x:05d}")               #00123
print(f"{x:<05d}")              #12300
print(f"{x:^5d}")               # 123
print(f"{y:5s}")                #abc
print(f"{z:2f}")                #123.456700
print(f"{z:.2f}")
print(f"{z:8.2f}")
print(100*"-")
