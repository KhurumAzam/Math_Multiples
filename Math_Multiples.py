class Math_Multiples:
    def multiples(self, num1):
        output = f"The multiples of {num1} are: "
        for i in range(100):
            if i == 0:
                continue
            elif i == 99:
                output += f"{str(num1*i)}"
            else:
                output += f"{str(num1 * i)}, "
        print(output)

if __name__ == "__main__":
    obj = Math_Multiples()
    obj.multiples(int(input("What number do you want multiples from: ")))
