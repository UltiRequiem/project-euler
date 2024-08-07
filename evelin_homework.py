# silly code i had to do for my friend

def alcohol_concentration(bebida: int, concentracion: int, peso: int, sexo="male"):
    alcohol_ml = bebida * concentracion / 100
    alcohol_grams = 0.8 * alcohol_ml

    fw = 0.73 if sexo == "male" else 0.66

    user_concentration = alcohol_grams * 1.055 / peso * fw

    return round(user_concentration, 5)


def segunda_bebida(bebida: int, concentracion: int, peso: int):
    initial_concentration = alcohol_concentration(bebida, concentracion, peso)
    print(f"{initial_concentration} g/L de sangre al inicio.")

    final_concentration = alcohol_concentration(bebida * 2, concentracion, peso)
    print(f"{final_concentration} g/L de sangre al final.")

    varition_concentration = final_concentration - initial_concentration

    print(f"La variacion fue {varition_concentration}")

    if final_concentration < 0.5:
        print("Aun puede conducir.")
    else:
        print("Ya no puede conducir.")

print("Caso 1:")
segunda_bebida(100, 8, 60)
print("Caso 2:")
segunda_bebida(200, 10, 70)
print("Caso 3:")
segunda_bebida(330, 5, 75)
print("Caso 4:")
segunda_bebida(500, 12, 80)
print("Caso 5:")
segunda_bebida(750, 16, 80)
