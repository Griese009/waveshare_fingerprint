def wert_tauschen(wert, art="g"):
    try:
        try:
            wert += 1
            wert -= 1
            ergebnis = None
            print(hex(wert))
            erste_haelfte = wert // 16 // 16
            zweite_haelfte = wert - (erste_haelfte * 16 * 16)
            print(hex(erste_haelfte), hex(zweite_haelfte))
            ergebnis = [erste_haelfte, zweite_haelfte]
            return ergebnis  # return the values
        except TypeError:
            print(wert)
            ergebnis = 0b0000
            b = wert
            for d in b:
                if d == "0":
                    bit = 0b0000
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "1":
                    bit = 0b0001
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "2":
                    bit = 0b0010
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "3":
                    bit = 0b0011
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "4":
                    bit = 0b0100
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "5":
                    bit = 0b0101
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "6":
                    bit = 0b0110
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "7":
                    bit = 0b0111
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "8":
                    bit = 0b1000
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "9":
                    bit = 0b1001
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "A" or d == "a":
                    bit = 0b1010
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "B" or d == "b":
                    bit = 0b1011
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "C" or d == "c":
                    bit = 0b1100
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "D" or d == "d":
                    bit = 0b1101
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "E" or d == "e":
                    bit = 0b1110
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                elif d == "F" or d == "f":
                    bit = 0b1111
                    ergebnis = ergebnis ^ bit
                    ergebnis = ergebnis << 4
                else:
                    print("Error")
                    break
            ergebnis = ergebnis >> 4
            return ergebnis
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(wert_tauschen(0xFF38, art="z"))
    print(wert_tauschen("3ef"))
