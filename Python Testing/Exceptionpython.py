

ItemInCart = 0
# 2 items will be added to cart

# if ItemInCart != 2:
#     raise Exception("Products cart count not matching")

# if ItemInCart != 2:
    #pass
#assert(ItemInCart == 2)  # assertion always should be true this one is false due to 2 there should be 0

# try,except

try:
    with open('filelog.txt','r')as reader:
        reader.read()

except:
    print("some how i reached this block because there is failure in try block")


try:
    with open('filelog.txt','r')as reader:  # if try block is wrong it will go to except
        reader.read()

except Exception as e:  # run when try block is wrong
    print(e)  # python error message

finally:   # does not matter try and except is wrong or right it will run
    print("cleaning up resources")

