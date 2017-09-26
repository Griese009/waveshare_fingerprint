def wert_tauschen(wert, art="g"):
    ergebnis = None
    print(hex(wert))
    erste_haelfte = wert // 16 // 16
    zweite_haelfte = wert - (erste_haelfte * 16 * 16)
    print(hex(erste_haelfte), hex(zweite_haelfte))
    ergebnis = [erste_haelfte, zweite_haelfte]
    return ergebnis  # return the values


if __name__ == "__main__":
    print(wert_tauschen(0xFF38, art="z"))