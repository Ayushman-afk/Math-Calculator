import math

userinp = int(input("Enter Which Operation would you like to perform: \n 1. 2 Number Addition \n 2. 2 Number Subtraction \n 3. 2 Number Multiplication \n 4.2 Number Division \n 5. Exponent \n 6. Square Root a number \n 7. Find the Remainder of 2 numbers \n 8. Find the Percentage \n 9. Average (mean) \n 10. Find the Hypotenuse \n 11. Find the Missing Leg \n 12. Check For A Right Triangle \n 13. Find the Area of a circle \n 14. Find the Area of a Triangle \n 15. Find the Distance Between 2 points \n 16. Quit \n Choice - "))

if userinp == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = (num1 + num2)
    print("The sum of the numbers is: ", op)

elif userinp == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = (num1 - num2)
    print("The sum of the numbers is: ", op)

elif userinp == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = (num1 * num2)
    print("The sum of the numbers is: ", op)

elif userinp == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = (num1 / num2)
    print("The sum of the numbers is: ", op)

elif userinp == 5:
    num1 = int(input("Enter base number: "))
    num2 = int(input("Enter the power: "))
    op = (num1) ** (num2)
    print("The exponent of the numbers is: ", op)

elif userinp == 6:
    num1 = int(input("Enter the number to find the Square Root of: "))
    op = math.sqrt(num1)
    print("The Square Root of the number is : ", op)

elif userinp == 7:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = (num1) % (num2)
    print("The Remainder of the numbers is: ", op)

elif userinp == 8:
    n = int(input("Enter p value: "))
    p = int(input("Enter n value: "))
    op = (n) * (p / 100)
    print("The Percentage of the numbers is (Rounded 2 Decimal Places) : {:.2f} " .format(op))
elif userinp == 9:
    nums = []
    userinp = int(input("Enter how many numbers to Calculate the mean: "))
    for x in range(userinp):
        int(input("Enter numbers: "))
        nums.append(x)
    op = sum(nums) / len(nums)
    print("The mean of the numbers is (rounded 2 decimals places) : {:.2f} " .format(op))

elif userinp == 10:
    a = int(input("Enter first leg: "))
    b = int(input("Enter second second: "))
    op = (a ** 2) + (b ** 2)
    print("The Hypotenuse is (rounded 2 decimals places) : {:.2f} ".format(op))

elif userinp == 11:
    b = int(input("Enter b value: "))
    c = int(input("Enter c value: "))
    op = math.sqrt((c ** 2) - (b ** 2))
    print("The Value of the Leg is (rounded 2 decimal places: {:.2f} ".format(op))

elif userinp == 12:
    a = float(input("Enter a value: "))
    b = float(input("Enter b value: "))
    c = float(input("Enter c value: "))
    if (a ** 2 + b ** 2) == (c ** 2):
        print("It is a Right Triangle")
    else:
        print("It is not a Right Triangle")
elif userinp == 13:
    r = int(input("Enter the radius of the circle:"))
    op = (r ** 2) * (math.pi)
    print("The area of the circle is (rounded 2 decimal places): {:.2f}".format(op))

elif userinp == 14:
    b = int(input("Enter base value: "))
    h = int(input("Enter height value: "))
    op = (0.5) * (b) * (h)
    print("The Area of the triangle is (rounded 2 decimal places) : {:.2f}".format(op))

elif userinp == 15:
    x1 = int(input("Enter first x value: "))
    x2 = int(input("Enter second x value: "))
    y1 = int(input("Enter first y value: "))
    y2 = int(input("Enter second y value: "))
    op = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The Distance between the 2 points is (rounded 2 decimal places) : {:.2f}".format(op))
elif userinp == 16:
    quit()



