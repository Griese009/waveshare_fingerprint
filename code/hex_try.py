def wert_tauschen(wert, art="g"):
    try:
        a = str(hex(wert))
    except Exception:
        a = wert  # i just trust everyone the he/she types values isnated of characters
    b = a[2:]
    while len(b) != 4:
        b = "0" + b
    ergebnisA = 0b0000
    ergebnisB = 0b0000
    ergebnis = []
    length = 0
    if art == "g":  # controll of value should be put together or not (from command together if for a command seperate)
        # g = seperating them into 2 8-bit values
        length = 8
    elif art == "z":
        # z = put them into 1 16-bit values
        length = 16 + 2  # +2 because the last hex number would not be count if only 16 (maybe because the b' indicates)
    for d in b:
        if len(bin(ergebnisA)) <= length:
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
    if length == 8:
        ergebnisA = ergebnisA >> 4
        ergebnisB = ergebnisB >> 4  # at ergebnisB the value is 4 bits bigger as it should so bit manipulation
        ergebnis.append(ergebnisA)
        ergebnis.append(ergebnisB)
    elif length == 18:
        ergebnis = (ergebnisA >> 4)  # see comment above
    return ergebnis  # return the values

if __name__ == "__main__":
    print(wert_tauschen(61483, art="z"))