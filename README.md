# Python Notes

## Tuples
Tuples - can store multiple items in a single variable. There are immutable. Good to use when the data is fixed. They have no way to append data to it, but you can combine a tuple into a new tuple with new data 

EX:
```
tuple_items - ("item1","item2","item3")
print(tuple_items)

mixed_tuple = ("A", 1, ("A",1))
print(mixed_tuple)
```

## Lists

using ```list1=list2``` just creates a shallow copy 
can use copy to make a deep copy such as 
```list6 = list4.copy() ```


## Disctionaries 

 ```
 dict1 = {"a":1,"b":2,"c":3}
 print(dict1)
 print(type(dict1))
 print(len(dict1))
 print(dict1["a"])
```

## Loops 
Allow you to continuously go through values or keep executing until a condition is met 

ex:
```
a = 1
while a < 5:
    a +=1
    print(a)

for i in [0, 1, 2, 3, 4, 5]:
   print(i+6)

for i range(5):
   print(i+6)
```
## Files

### Opening a file 
```
f = open('top-100.txt')
print(f) #will print out file meta data and opening mode
```

### Reading a file
```
print(f.read()) #will actually display the contents of the file 

f.seek(0)
for line in f:
   print(line.strip())
f.close()
```

### Writing to a file
```
f = open("text.txt", "w")
f.write("test line")
f.close()
```
 ## User Input
 ```
 test = input("What is your name?: )
 print("Hi, ", test)
 ```

 ## Exceptions and Error Handling
 ```
try:
    f = open("ajdhdhsh")
except Exception as e:
   print(f"The file does not exist! the error is {e}")
```

## Comprehensions 
```
list1 = ['a','b','c']
print(list1)
list2 = [x for x in list1]
print(list2)
list3 = [x for x in list1 if x == 'a']
print(list3)

list11 = [c for c in "string"]
print(list11)

print("".join(list11))
print("-".join(list11))
``` 

## Functions
Block of code meant to only be run when it is called and meant to be rerun

```
def function1():
   print("Hello from function!")

function1()

def funtion3(s):
   print("\t{}".format(s))

funtion3("parameter")
```

## Lambda
Function without a name, can only have one expression

```
add_4 = lambda x : x + 4
print(add_4(5))
```