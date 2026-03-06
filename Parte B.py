"""
UNIVERSIDAD MILITAR NUEVA GRANADA
Laboratorio PDS — Parte B

Punto 1: Correlación cruzada
Punto 2: Representación gráfica de la secuencia

Señales:
x1[nTs] = cos(2π·100·nTs)
x2[nTs] = sin(2π·100·nTs)

Ts = 1.25 ms
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate


def stem_simple(ax, n, valores, color):
    """Dibuja una señal discreta"""
    for i, v in zip(n, valores):
        ax.plot([i, i], [0, v], color=color)
        ax.plot(i, v, "o", color=color)

    ax.axhline(0)


def main():

    # parámetros
    Ts = 1.25e-3
    fs = 1 / Ts
    f0 = 100

    n = np.arange(9)

    # señales
    x1 = np.cos(2 * np.pi * f0 * n * Ts)
    x2 = np.sin(2 * np.pi * f0 * n * Ts)

    print("\nPARTE B — Correlación cruzada\n")

    print("Ts =", Ts, "s")
    print("fs =", fs, "Hz")
    print("f0 =", f0, "Hz")

    print("\nx1[n] =")
    print(np.round(x1, 4))

    print("\nx2[n] =")
    print(np.round(x2, 4))

    # correlación
    Rxy = correlate(x1, x2, mode="full")

    lags = np.arange(-(len(n) - 1), len(n))

    pico = np.argmax(np.abs(Rxy))
    peak_lag = lags[pico]
    peak_val = Rxy[pico]

    print("\nResultados de correlación\n")

    print("lags =")
    print(lags)

    print("\nRxy =")
    print(np.round(Rxy, 4))

    print("\nPico máximo en lag =", peak_lag)
    print("Valor del pico =", peak_val)

    # gráfica
    fig, axes = plt.subplots(3, 1, figsize=(10, 8))

    fig.suptitle("Correlación cruzada entre x1 y x2")

    # x1
    stem_simple(axes[0], n, x1, "green")
    axes[0].set_title("x1[n] = cos(2π·100·nTs)")
    axes[0].set_xlabel("n")
    axes[0].set_ylabel("Amplitud")
    axes[0].grid(True)

    # x2
    stem_simple(axes[1], n, x2, "red")
    axes[1].set_title("x2[n] = sin(2π·100·nTs)")
    axes[1].set_xlabel("n")
    axes[1].set_ylabel("Amplitud")
    axes[1].grid(True)

    # correlación
    stem_simple(axes[2], lags, Rxy, "purple")
    axes[2].set_title("Rxy[lag]")
    axes[2].set_xlabel("lag")
    axes[2].set_ylabel("Amplitud")
    axes[2].grid(True)

    # marcar pico
    axes[2].axvline(peak_lag, linestyle="--")
    axes[2].text(peak_lag, peak_val, " pico")

    plt.tight_layout()

    plt.savefig("parteB_correlacion.png", dpi=150)

    plt.show()

    print("\nGráfica guardada como 'parteB_correlacion.png'")
    print("\nParte B terminada\n")


if __name__ == "__main__":
    main()