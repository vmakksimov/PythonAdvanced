text = input().split(', ')

for sym in text:
    if 3 <= len(sym) <= 16:
        if sym.isalpha() or '-' in sym or '_' in sym:
            print(sym)
        elif sym.isdigit() or '-' in sym or '_' in sym:
            print(sym)
        elif sym.isalnum() or '-' in sym or '_' in sym:
            print(sym)
