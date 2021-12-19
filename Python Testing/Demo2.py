values = [1, 2, "rahul", 4, 5]
# list is data type that allows multiple values and can be different data types

print(values[0])

print(values[3])

print(values[-1])

print(values[1:4])

values.insert(3,"shetty")
print(values)

values.append("end")
print(values)

values[2] = "RAHUL"
print(values) # updating

del values[0]
print(values)

# Tuple = same as list data type but immutable

val = (1, 2, "rahul", 4.5)
print(val[1])

# dictionary

dict = {"a": 2, 4 : "bcd", "c" : "Hello world" }
print(dict["c"])

#
dict = {}

dict["Firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "male"

print(dict["gender"])

