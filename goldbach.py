def este_prim(numar):
    if numar < 2:
        return False
    for i in range(2, numar):
        if numar % i == 0:
            return False
    return True

def gaseste_perechi(n):
    for p in range(2, n):
        q = n - p
        if p <= q and este_prim(p) and este_prim(q):
            print(f"{n} = {p} + {q}")

def main():
    n = 0
    while n <= 2 or n % 2 != 0:
        text = input("Introdu un numar par mai mare ca 2: ")
        if text.isdigit():
            n = int(text)
            if n <= 2 or n % 2 != 0:
                print("Eroare: Numarul trebuie sa fie par si mai mare ca 2!")
        else:
            print("Eroare: Te rog introdu un numar valid!")

    print("Perechile Goldbach sunt:")
    gaseste_perechi(n)

if __name__ == "__main__":
    main()