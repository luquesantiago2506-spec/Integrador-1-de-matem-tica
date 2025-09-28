
# Sumador de bits #

from typing import Tuple

def leer_bit(mensaje: str) -> int:
    """Lee un bit (0/1) con reintento y salida limpia."""
    while True:
        try:
            x = input(mensaje).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            raise SystemExit(1)
        if x in ("0", "1"):
            return int(x)
        print("Entrada inválida. Escribí 0 o 1.")

# Núcleo evaluado (dos variantes: condicionales y bitwise)
def half_adder_cond(a: int, b: int) -> Tuple[int, int]:
    
    # SUMA (S): 1 si son distintos; 0 si son iguales
    if (a == 0 and b == 1) or (a == 1 and b == 0):
        s = 1
    else:
        s = 0
    # CARRY (C): 1 solo si a==1 y b==1
    if a == 1 and b == 1:
        c = 1
    else:
        c = 0
    return s, c

def half_adder(a: int, b: int) -> Tuple[int, int]:
    """Half-Adder con operadores bit a bit (XOR y AND)."""
    return a ^ b, a & b

def tabla_verdad_half() -> None:
    """Imprime la tabla de verdad del Half-Adder (A, B -> S, C)."""
    print("\nTabla de Verdad — HALF ADDER (A, B -> S, C)")
    print(" A  B | S  C")
    print("-----------")
    for a in (0, 1):
        for b in (0, 1):
            s, c = half_adder_cond(a, b)  # usar la versión con condicionales
            print(f" {a}  {b} | {s}  {c}")

def simulador_interactivo() -> None:
    """Simulador simple de Half-Adder (sin carry de entrada)."""
    print("\n🧮 Simulador de Sumador de 1 Bit (Half-Adder)")
    a = leer_bit("Bit A (0/1): ")
    b = leer_bit("Bit B (0/1): ")
    s, c = half_adder_cond(a, b)  # núcleo evaluado: condicionales
    print("\nResultado:")
    print(f"  A={a}, B={b}")
    print(f"  Suma (S) = {s}")
    print(f"  Carry (C) = {c}")

def main() -> None:
    print("=== Sumador de 1 bit (Half-Adder) ===")
    while True:
        print("\nOpciones:")
        print(" 1) Mostrar tabla de verdad (Half-Adder)")
        print(" 2) Simulador 1 bit")
        print(" 3) Salir")
        try:
            op = input("Elegí (1-3): ").strip()
        except KeyboardInterrupt:
            print("\nAdiós.")
            return
        if op == "1":
            tabla_verdad_half()
        elif op == "2":
            simulador_interactivo()
        elif op == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
