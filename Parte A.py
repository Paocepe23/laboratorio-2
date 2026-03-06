"""
UNIVERSIDAD MILITAR NUEVA GRANADA
Laboratorio PDS — Parte A

Punto 3: Convolución usando Python
Punto 4: Representación gráfica de las señales
"""

import numpy as np
import matplotlib.pyplot as plt


# colores para las gráficas
STEM_COLOR = "#b06aba"
LINE_COLOR = "#5bc8f5"


def leer_digitos(prompt):
    """Lee un número y devuelve sus dígitos como arreglo"""
    while True:
        valor = input(prompt).strip()

        if valor.isdigit():
            digitos = [int(d) for d in valor]
            return np.array(digitos, dtype=float), valor

        print("Entrada inválida. Solo escribe números sin espacios.")


def stem_custom(ax, n, valores):
    """Dibuja una señal discreta tipo stem"""
    for i, v in zip(n, valores):
        ax.plot([i, i], [0, v], color=STEM_COLOR)
        ax.plot(i, v, "o", color=STEM_COLOR)

    ax.axhline(0, color=LINE_COLOR)


def graficar(h, x, y, codigo, cedula):

    fig, axes = plt.subplots(3, 1, figsize=(10, 8))

    fig.suptitle(
        f"Convolución en Python\nCódigo: {codigo}  -  Cédula: {cedula}",
        fontsize=12
    )

    datos = [
        (np.arange(len(h)), h, "Sistema h[n]"),
        (np.arange(len(x)), x, "Señal x[n]"),
        (np.arange(len(y)), y, "Resultado y[n] = x[n] * h[n]")
    ]

    for ax, (n, valores, titulo) in zip(axes, datos):

        stem_custom(ax, n, valores)

        ax.set_title(titulo)
        ax.set_xlabel("n")
        ax.set_ylabel("Amplitud")

        ax.set_xticks(n)
        ax.set_xlim(-0.5, len(n) - 0.5)

        ax.grid(True)

        ymax = max(valores) * 1.2 if max(valores) > 0 else 1
        ymin = min(valores) * 1.2 if min(valores) < 0 else -1

        ax.set_ylim(ymin, ymax)

    plt.tight_layout()

    plt.savefig("parteA_convolucion.png", dpi=150)

    plt.show()

    print("Gráfica guardada como 'parteA_convolucion.png'")


def main():

    print("\nLABORATORIO PDS — PARTE A\n")

    # ingresar datos
    h, codigo = leer_digitos("Código estudiantil: ")
    x, cedula = leer_digitos("Número de cédula: ")

    # Punto 3: convolución
    y = np.convolve(x, h)

    print("\nResultados\n")

    print("h[n] =", h.astype(int).tolist())
    print("x[n] =", x.astype(int).tolist())

    print("\nLongitud de y[n] =", len(x), "+", len(h), "- 1 =", len(y))

    print("y[n] =", y.astype(int).tolist())

    # Punto 4: gráfica
    graficar(h, x, y, codigo, cedula)

    print("\nProceso terminado\n")


if __name__ == "__main__":
    main()