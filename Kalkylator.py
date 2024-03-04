tal1 = float(input("Skriv ditt första tal: "))
operation = input("Vilken operation vill du använda?: ")
tal2 = float(input("Skriv ditt andra tal: "))
def nummer(tal1, tal2, operation):
    elif operation == "*":
        result = tal1 * tal2
        return result
    elif operation == "/":
        result = tal1/tal2
        return result
    elif operation == "+":
        result = tal1+tal2
        return result
    elif operation == "-":
        result = tal1-tal2
        return result
    if operation == "/" and tal2 == "0":
    print("Man kan inte dividera med 0")
    beraknat_tal = nummer(tal1, tal2, operation)
    print(beraknat_tal)