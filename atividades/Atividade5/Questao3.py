# TURNO DE ESTUDO

turno = input("Digite o turno (M, V ou N): ").lower()

match turno:
    case "m":
        print("Bom Dia!")
    case "v":
        print("Boa Tarde!")
    case "n":
        print("Boa Noite!")
    case _:
        print("Turno inválido!")
