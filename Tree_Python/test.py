#coing:utf-8

a = 1

try:
    a += 1
    print('try')
except:
    a += 1
    print("except")
else:
    a += 1
    print("else")
finally:
    a += 1
    print("finally")

print(a)