print("Gray Code to Binary Converter")
print("-----------------------------")

gray = input("Enter a Gray Code: ")

# Validate Gray Code
if all(bit in "01" for bit in gray):

    binary = gray[0]

    for i in range(1, len(gray)):
        binary += str(int(binary[i - 1]) ^ int(gray[i]))

    print("\nResult:")
    print("Gray Code :", gray)
    print("Binary    :", binary)

else:
    print("Invalid input! Please enter only 0 and 1.")
