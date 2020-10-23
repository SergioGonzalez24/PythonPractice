largest = None
smallest = None
nums=[]
while True:
    

    try:
        num=int(input("numero: "))
        val= input("Enter a number: ")
        if not(num==int):
            nums.append(num)
            nums.sort()
    except ValueError:
        print("Invalid Input")
        continue
    if val == "done" : 
        smallest=nums[0]
        largest= nums[3]
        break

print("Maximum is", largest)
print("Minimum is ",smallest)