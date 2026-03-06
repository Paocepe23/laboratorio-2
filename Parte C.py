"""
UNIVERSIDAD MILITAR NUEVA GRANADA
Laboratorio PDS — Parte C

Análisis de señal biológica (EOG)

Puntos:
3a. Estadísticos en el tiempo
4a. Transformada de Fourier
4b. Densidad espectral de potencia
4c. Estadísticos en frecuencia
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# frecuencia de muestreo
FS = 1000


def main():

    # cargar señal
    senal = np.loadtxt("senalralf.txt")

    N = len(senal)
    t = np.arange(N) / FS

    print("\nPARTE C — Señal EOG\n")
    print("Muestras:", N)
    print("Frecuencia de muestreo:", FS, "Hz")
    print("Duración:", N / FS, "s")

    # ==================================================
    # PUNTO 3a — estadísticos en tiempo
    # ==================================================

    media   = np.mean(senal)
    mediana = np.median(senal)
    std     = np.std(senal)
    maximo  = np.max(senal)
    minimo  = np.min(senal)

    print("\nEstadísticos de la señal\n")
    print(f"  Media:              {media:.4f}")
    print(f"  Mediana:            {mediana:.4f}")
    print(f"  Desviación estándar:{std:.4f}")
    print(f"  Máximo:             {maximo:.4f}")
    print(f"  Mínimo:             {minimo:.4f}")

    # ==================================================
    # PUNTO 4a — FFT
    # ==================================================

    Y     = np.fft.rfft(senal)
    freqs = np.fft.rfftfreq(N, 1 / FS)
    mag   = np.abs(Y) / N

    print("\nFFT calculada")
    print(f"  Resolución: {FS / N:.4f} Hz")

    # ==================================================
    # PUNTO 4b — PSD (Welch)
    # ==================================================

    f_welch, psd = welch(senal, fs=FS)

    print("\nPSD calculada usando método Welch")

    # ==================================================
    # PUNTO 4c — estadísticos en frecuencia
    # ==================================================

    power       = mag ** 2
    total_power = np.sum(power)

    f_media   = np.sum(freqs * power) / total_power

    acumulado = np.cumsum(power)
    f_mediana = freqs[np.searchsorted(acumulado, total_power / 2)]

    f_std     = np.sqrt(np.sum(((freqs - f_media) ** 2) * power) / total_power)

    print("\nEstadísticos espectrales\n")
    print(f"  Frecuencia media:      {f_media:.4f} Hz")
    print(f"  Frecuencia mediana:    {f_mediana:.4f} Hz")
    print(f"  Desviación estándar:   {f_std:.4f} Hz")

    # ==================================================
    # GRAFICAS
    # ==================================================

    # señal en el tiempo
    plt.figure(figsize=(10, 4))
    plt.plot(t, senal)
    plt.axhline(media, linestyle="--", label=f"media = {media:.4f}")
    plt.legend()
    plt.title("[Punto 3a] Señal EOG en el tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid()
    plt.tight_layout()
    plt.savefig("parteC_senal_tiempo.png")
    plt.show()

    # histograma de amplitudes
    plt.figure(figsize=(6, 4))
    plt.hist(senal, bins=50)
    plt.axvline(media,   linestyle="--", label=f"media = {media:.4f}")
    plt.axvline(mediana, linestyle=":",  label=f"mediana = {mediana:.4f}")
    plt.legend()
    plt.title("[Punto 3a] Histograma de amplitudes")
    plt.xlabel("Amplitud")
    plt.ylabel("Conteo")
    plt.grid()
    plt.tight_layout()
    plt.savefig("parteC_histograma.png")
    plt.show()

    # FFT — con frecuencia media y mediana marcadas (punto 4c)
    plt.figure(figsize=(10, 4))
    plt.plot(freqs, mag)
    plt.axvline(f_media,   linestyle="--", label=f"f media = {f_media:.2f} Hz")
    plt.axvline(f_mediana, linestyle=":",  label=f"f mediana = {f_mediana:.2f} Hz")
    plt.xlim(0, FS / 2)
    plt.legend()
    plt.title("[Punto 4a] Espectro de magnitud")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X(f)|")
    plt.grid()
    plt.tight_layout()
    plt.savefig("parteC_fft.png")
    plt.show()

    # PSD
    plt.figure(figsize=(10, 4))
    plt.semilogy(f_welch, psd)
    plt.xlim(0, FS / 2)
    plt.title("[Punto 4b] Densidad espectral de potencia")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("PSD")
    plt.grid()
    plt.tight_layout()
    plt.savefig("parteC_psd.png")
    plt.show()

    # histograma de frecuencias ponderado por potencia (punto 4c)
    plt.figure(figsize=(8, 4))
    plt.hist(freqs, bins=50, weights=power / total_power)
    plt.axvline(f_media,   linestyle="--", label=f"f media = {f_media:.2f} Hz")
    plt.axvline(f_mediana, linestyle=":",  label=f"f mediana = {f_mediana:.2f} Hz")
    plt.legend()
    plt.title("[Punto 4c] Histograma de frecuencias")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Densidad de probabilidad")
    plt.grid()
    plt.tight_layout()
    plt.savefig("parteC_histograma_freq.png")
    plt.show()

    print("\nGráficas guardadas.")
    print("\nParte C finalizada\n")


if __name__ == "__main__":
    main()