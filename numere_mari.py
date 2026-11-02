def adunare(nr1, nr2):
    while len(nr1) < len(nr2):
        nr1 = "0" + nr1
    while len(nr2) < len(nr1):
        nr2 = "0" + nr2

    rezultat = ""
    transport = 0
    for i in range(len(nr1) - 1, -1, -1):
        suma = int(nr1[i]) + int(nr2[i]) + transport
        rezultat = str(suma % 10) + rezultat
        transport = suma // 10

    if transport > 0:
        rezultat = str(transport) + rezultat

    return rezultat

def inmultire(nr1, nr2):
    if nr1 == "0" or nr2 == "0":
        return "0"

    rez = [0] * (len(nr1) + len(nr2))
    for i in range(len(nr1) - 1, -1, -1):
        for j in range(len(nr2) - 1, -1, -1):
            prod = int(nr1[i]) * int(nr2[j])
            poz = i + j + 1
            suma = prod + rez[poz]
            rez[poz] = suma % 10
            rez[poz - 1] += suma // 10

    text_rez = ""
    for c in rez:
        text_rez += str(c)

    while len(text_rez) > 1 and text_rez[0] == '0':
        text_rez = text_rez[1:]

    return text_rez

def main():
    try:
        f = open("numere.txt", "r")
        linii = f.readlines()
        f.close()

        if len(linii) >= 2:
            nr1 = linii[0].strip()
            nr2 = linii[1].strip()

            if nr1.isdigit() and nr2.isdigit():
                print("Suma este:", adunare(nr1, nr2))
                print("Produsul este:", inmultire(nr1, nr2))
            else:
                print("Eroare: Fisierul contine alte caractere decat cifre.")
        else:
            print("Eroare: Fisierul trebuie sa aiba cel putin doua linii.")
    except FileNotFoundError:
        print("Eroare: Nu s-a gasit fisierul numere.txt.")

if __name__ == "__main__":
    main()