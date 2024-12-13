x = 40
y = 80
sum = x+y
if x > y:
    diff = x-y
    div = x/y
    modu = x%y
    print ("x is greater than y")
elif y > x:
    diff = y-x
    div = y/x
    modu  = y%x
    print ("y is greater than x")
else:
    diff = y-x
    div = y/x
    modu  = y%x
    print ("They're equals")

prod = x * y

print ("sum is ",x+y)
print ("diff is: ",diff)
print ("prod is: ",prod)
print ("div is: ",div)
print ("mod is: ",modu)