def wert_tauschen(wert):
    a = str(hex(wert))
    print(a)
    b = a[2:]
    print(b)
    ergebnisA = 0b0000
    ergebnisB = 0b0000
    ergebnis = []
    for d in b:
        if len(bin(ergebnisA)) < 8:
            if d == "0":
                bit = 0b0000
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "1":
                bit = 0b0001
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "2":
                bit = 0b0010
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "3":
                bit = 0b0011
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "4":
                bit = 0b0100
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "5":
                bit = 0b0101
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "6":
                bit = 0b0110
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "7":
                bit = 0b0111
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "8":
                bit = 0b1000
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "9":
                bit = 0b1001
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "A" or d == "a":
                bit = 0b1010
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "B" or d == "b":
                bit = 0b1011
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "C" or d == "c":
                bit = 0b1100
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "D" or d == "d":
                bit = 0b1101
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "E" or d == "e":
                bit = 0b1110
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            elif d == "F" or d == "f":
                bit = 0b1111
                ergebnisA = ergebnisA ^ bit
                ergebnisA = ergebnisA << 4
            else:
                print("Error")
                break
        else:
            if d == "0":
                bit = 0b0000
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "1":
                bit = 0b0001
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "2":
                bit = 0b0010
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "3":
                bit = 0b0011
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "4":
                bit = 0b0100
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "5":
                bit = 0b0101
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "6":
                bit = 0b0110
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "7":
                bit = 0b0111
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "8":
                bit = 0b1000
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "9":
                bit = 0b1001
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "A" or d == "a":
                bit = 0b1010
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "B" or d == "b":
                bit = 0b1011
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "C" or d == "c":
                bit = 0b1100
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "D" or d == "d":
                bit = 0b1101
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "E" or d == "e":
                bit = 0b1110
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            elif d == "F" or d == "f":
                bit = 0b1111
                ergebnisB = ergebnisB ^ bit
                ergebnisB = ergebnisB << 4
            else:
                print("Error")
                break
        ergebnisA = ergebnisA >> 4
        ergebnisB = ergebnisB >> 4
        ergebnis.append(ergebnisA)
        ergebnis.append(ergebnisB)
        return ergebnis