def adunare(nr1, nr2):
    i, j = len(nr1) - 1, len(nr2) - 1
    transport = 0
    rez = []
    
    while i >= 0 or j >= 0 or transport:
        d1 = int(nr1[i]) if i >= 0 else 0
        d2 = int(nr2[j]) if j >= 0 else 0
        suma = d1 + d2 + transport
        
        rez.append(str(suma % 10))
        transport = suma // 10
        
        i -= 1
        j -= 1
        
    return "".join(reversed(rez))

def inmultire(nr1, nr2):
    if nr1 == "0" or nr2 == "0":
        return "0"
        
    rez = [0] * (len(nr1) + len(nr2))
    
    for i in range(len(nr1) - 1, -1, -1):
        for j in range(len(nr2) - 1, -1, -1):
            prod = int(nr1[i]) * int(nr2[j]) + rez[i + j + 1]
            rez[i + j + 1] = prod % 10
            rez[i + j] += prod // 10
            
    start = 0
    while start < len(rez) - 1 and rez[start] == 0:
        start += 1
        
    return "".join(str(c) for c in rez[start:])

def main():
    try:
        with open("numere.txt", "r") as f:
            linii = [l.strip() for l in f if l.strip()]
        
        if len(linii) >= 2 and linii[0].isdigit() and linii[1].isdigit():
            print("Suma este:", adunare(linii[0], linii[1]))
            print("Produsul este:", inmultire(linii[0], linii[1]))
        else:
            print("Eroare: Fisierul trebuie sa contina minim 2 numere formate doar din cifre.")
    except FileNotFoundError:
        print("Eroare: Nu s-a gasit fisierul numere.txt.")

if __name__ == "__main__":
    main()