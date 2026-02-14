from logic_gates import AND, OR, NOT, NAND

def main():
    print("Digital Logic Simulator")
    print("Available Gates: AND, OR, NOT, NAND")
    
    gate = input("Enter gate name: ").upper()

    if gate == "NOT":
        a = int(input("Enter input (0 or 1): "))
        print("Output:", NOT(a))
    else:
        a = int(input("Enter first input (0 or 1): "))
        b = int(input("Enter second input (0 or 1): "))
        
        if gate == "AND":
            print("Output:", AND(a, b))
        elif gate == "OR":
            print("Output:", OR(a, b))
        elif gate == "NAND":
            print("Output:", NAND(a, b))
        else:
            print("Invalid gate!")

if __name__ == "__main__":
    main()
