import math

while True:
    userinp = float(input("Enter Which Operation would you like to perform: \n 1. 2 Number Addition \n 2. 2 Number Subtraction \n 3. 2 Number Multiplication \n 4. 2 Number Division \n 5. Exponent \n 6. Square Root a number \n 7. Find the Remainder of 2 numbers \n 8. Find the Percentage \n 9. Average (mean) \n 10. Find the Hypotenuse \n 11. Find the Missing Leg \n 12. Check For A Right Triangle \n 13. Find the Area of a circle \n 14. Find the Area of a Triangle \n 15. Find the Distance Between 2 pofloats \n 16. Quit \n Choice - "))


    if userinp == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = (num1 + num2)
        print("The sum of the numbers is: ", op)

    elif userinp == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = (num1 - num2)
        print("The difference of the numbers is: ", op)

    elif userinp == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = (num1 * num2)
        print("The product of the numbers is: ", op)

    elif userinp == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            op = (num1 / num2)
            print("The quotient of the numbers is: ", op)
        else:
            print("The quotient of the numbers is: 0")

    elif userinp == 5:
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter the power: "))
        op = (num1) ** (num2)
        print("The exponent of the numbers is: ", op)

    elif userinp == 6:
        num1 = float(input("Enter the number to find the Square Root of: "))
        if num1 >= 1:
            op = math.sqrt(num1)
            print("The Square Root of the number is : ", op)
        else:
            print("The Value Can't be Negative!")

    elif userinp == 7:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num1 or num2 != 0:
            op = (num1) % (num2)
            print("The Remainder of the numbers is: ", op)
        else:
            print("Syntax Error")

    elif userinp == 8:
        n = float(input("Enter n value: "))
        p = float(input("Enter p value: "))
        op = (n) * (p / 100)
        print("The Percentage of the numbers is (Rounded 2 Decimal Places) : {:.2f} " .format(op))
    elif userinp == 9:
        nums = []
        i = float(input("Enter how many numbers to Calculate the mean: "))
        for x in range(int(i)):
            number =  float(input("Enter numbers: "))
            nums.append(number)
        op = sum(nums) / len(nums)
        print("The mean of the numbers is (rounded 2 decimals places) : {:.2f} " .format(op))

    elif userinp == 10:
        a = float(input("Enter first leg: "))
        b = float(input("Enter second leg: "))
        op = math.sqrt((a ** 2) + (b ** 2))
        print("The Hypotenuse is (rounded 2 decimals places) : {:.2f} ".format(op))

    elif userinp == 11:
        b = float(input("Enter b value: "))
        c = float(input("Enter c value: "))
        if c > b:
            op = math.sqrt((c ** 2) - (b ** 2))
            print("The Value of the Leg is (rounded 2 decimal places: {:.2f} ".format(op))
        else:
            print("Invalid Inputs")

    elif userinp == 12:
        a = float(input("Enter a value: "))
        b = float(input("Enter b value: "))
        c = float(input("Enter c value: "))
        if (a ** 2 + b ** 2) == (c ** 2):
            print("It is a Right Triangle")
        else:
            print("It is not a Right Triangle")
    elif userinp == 13:
        r = float(input("Enter the radius of the circle:"))
        op = (r ** 2) * (math.pi)
        print("The area of the circle is (rounded 2 decimal places): {:.2f}".format(op))

    elif userinp == 14:
        b = float(input("Enter base value: "))
        h = float(input("Enter height value: "))
        op = (0.5) * (b) * (h)
        print("The Area of the triangle is (rounded 2 decimal places) : {:.2f}".format(op))

    elif userinp == 15:
        x1 = float(input("Enter first x value: "))
        x2 = float(input("Enter second x value: "))
        y1 = float(input("Enter first y value: "))
        y2 = float(input("Enter second y value: "))
        op = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("The Distance between the 2 pofloats is (rounded 2 decimal places) : {:.2f}".format(op))
    elif userinp == 16:
        break



