print ("Number iteration")

arr = [10, 34, 45, 42, 34, 24]

for i in range (0, len(arr)):
    print (arr[i], end=" ")

arr.append(108)

arr[0] = 100

print ("\n array after modification:")

for i in range (0, len(arr)):
    print (arr[i], end=" ")