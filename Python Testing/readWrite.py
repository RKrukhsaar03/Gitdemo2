file = open('test.txt')
# print(file.read(2)) # read all the content of file,read n number of character by passing parameter

# print(file.readline())  # 1st line readed
# print(file.readline())  # 2nd line readed


# print line by line using method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()