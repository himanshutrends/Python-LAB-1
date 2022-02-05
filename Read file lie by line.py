f=open(r"C:\Users\Atharva\Desktop//test.txt","r")

counter=0
for data in f.readlines():
    print(data)
    counter+=1

f.close()

print(f"\nNumber of lines are {counter}")