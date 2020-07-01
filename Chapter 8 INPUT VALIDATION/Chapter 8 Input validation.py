import pyinputplus as pyip

# response = pyip.inputNum(prompt="Enter a number: ")

def addsUpToTen(numbers):
    numberList = list(numbers)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != 10:
        raise Exception("The digits must add up to 10, not %s" % sum(numberList))

    return int(numbers)

response = pyip.inputCustom(addsUpToTen)
