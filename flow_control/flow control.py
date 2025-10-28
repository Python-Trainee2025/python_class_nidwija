a=[1,2,3,4,5]

for i in a:
    if i%2==0:
        print("inside the loop: ",i)

'''
range(start,stop,step)
range(5) 0-> n-1
range(0,5)
'''

# for i in range(1,50):
#     if i%2==0:
#         print("inside the range loop: ",i)
for i in range(0,5,2):
    print("inside the range loop with step 2: ",i)

c=["apple","banana","mango"]
while c[0]!="mango":
    print("inside while loop: ",c)
    c+=1