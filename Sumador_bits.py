
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

# Núcleo evaluado (dos variantes):

def half_adder_cond(a: int, b: int) -> Tuple[int, int]:
    if (a == 0 and b == 1) or (a == 1 and b == 0):
        s = 1
    else:
        s = 0
    if a == 1 and b == 1:
        c = 1
    else:
        c = 0
    return s, c

def half_adder(a: int, b: int) -> Tuple[int, int]:
    return a ^ b, a & b

# Extensión: full-adder + tablas (sin demo de n bits)

def full_adder(a: int, b: int, cin: int = 0) -> Tuple[int, int]:
    if a not in (0, 1) or b not in (0, 1) or cin not in (0, 1):
        raise ValueError("a, b y cin deben ser bits (0/1).")
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, cin)
    return s2, (c1 | c2)

def tabla_verdad_half() -> None:
    print("\nTabla de Verdad — HALF ADDER (A, B -> S, C)")
    print(" A  B | S  C")
    print("-----------")
    for a in (0, 1):
        for b in (0, 1):
            s, c = half_adder_cond(a, b)  # versión con condicionales
            print(f" {a}  {b} | {s}  {c}")

def tabla_verdad_full() -> None:
    print("\nTabla de Verdad — FULL ADDER (A, B, Cin -> S, Cout)")
    print(" A  B  Cin | S  Cout | A+B+Cin")
    print("-------------------------------")
    for a in (0, 1):
        for b in (0, 1):
            for cin in (0, 1):
                s, cout = full_adder(a, b, cin)
                print(f" {a}  {b}   {cin}  | {s}   {cout}    |   {a+b+cin}")

def simulador_interactivo() -> None:
    print("\n🧮 Simulador de 1 bit (full-adder opcional)")
    a = leer_bit("Bit A (0/1): ")
    b = leer_bit("Bit B (0/1): ")
    usar_cin = input("¿Usar carry de entrada? (s/n): ").strip().lower() == "s"
    cin = leer_bit("Carry de entrada (0/1): ") if usar_cin else 0

    s, cout = full_adder(a, b, cin)
    print("\nResultado:")
    print(f"  A={a}, B={b}, Cin={cin}")
    print(f"  Suma={s}, Cout={cout}")
    dec = a + b + cin
    print(f"  Verificación decimal: {a}+{b}+{cin} = {dec}")
    print(f"  En binario: {cout}{s} = {cout*2 + s} (decimal)")

def main() -> None:
    print("=== Sumadores de 1 bit: Half & Full ===")
    while True:
        print("\nOpciones:")
        print(" 1) Tabla HALF")
        print(" 2) Tabla FULL")
        print(" 3) Simulador 1 bit")
        print(" 4) Salir")
        try:
            op = input("Elegí (1-4): ").strip()
        except KeyboardInterrupt:
            print("\nAdiós.")
            return
        if op == "1":
            tabla_verdad_half()
        elif op == "2":
            tabla_verdad_full()
        elif op == "3":
            simulador_interactivo()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()