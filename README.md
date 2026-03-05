# laboratorio-2
# Convolución, correlación y transformada de Fourier.
# Objetivos general. 
Reconocer la importancia de la aplicación de herramientas matemáticas como la convolución y correlación en el área de procesamiento de señales, validando su comportamiento mediante cálculos manuales y simulaciones en Python.
# Objetivos especificos.
Comprender la convolución como una operación fundamental para obtener la respuesta de un sistema discreto ante una entrada determinada, validando los resultados mediante cálculos manuales (sumatorias) y herramientas de programación en Python.
Analizar la correlación cruzada como una medida de similitud entre secuencias discretas (seno y coseno), identificando su utilidad para caracterizar dependencias estadísticas en el procesamiento de señales.
Implementar la Transformada de Fourier para realizar un análisis espectral de señales biológicas, permitiendo la transición del dominio del tiempo al dominio de la frecuencia para su caracterización.
# Metodología del experimento.
## Fase de Análisis Matemático y Simulación (Convolución).
En esta etapa se busca contrastar el cálculo manual con el computacional.
Definición de secuencias: Se establecen las señales discretas  utilizando los dígitos del código estudiantil y la cédula de ciudadanía respectivamente.
Cálculo Analítico: Se aplica la sumatoria de convolución de forma manual para obtener la secuencia resultante y su representación gráfica.
Implementación en Python: Se desarrolla un script para ejecutar la misma operación y generar las gráficas secuenciales, permitiendo la validación de los resultados obtenidos a mano.
## Fase de Caracterización de Similitud (Correlación)
Esta fase se enfoca en el análisis de señales trigonométricas:Generación de señales: Se definen las funciones con un periodo de muestreo.
Operación de Correlación: Se calcula la correlación cruzada entre ambas señales para medir su grado de similitud y se analiza la secuencia resultante de forma gráfica.
## Fase de Procesamiento de Señales Biológicas y Frecuencia.
Es la etapa de aplicación práctica con hardware y señales reales:
Adquisición: Se genera una señal biológica mediante el generador de señales.
Digitalización: Se determina la frecuencia de Nyquist de la señal y se procede a su digitalización utilizando una frecuencia de muestreo de 4.
Análisis Estadístico: Se caracteriza la señal en el dominio del tiempo obteniendo medidas de tendencia central (media, mediana) y de dispersión (desviación estándar).
Análisis Espectral: Se aplica la Transformada de Fourier para trasladar la señal al dominio de la frecuencia, graficando su espectro y densidad espectral de potencia.
# Marco conceptual.
## Electrooculografía (EOG).
Es la técnica que mide la diferencia de potencial existente entre la córnea y la retina (potencial córneo-retiniano).
El ojo actúa como un dipolo donde la córnea es positiva y la retina es negativa. Se usa para registrar movimientos oculares. En procesamiento de señales, estas señales suelen estar contaminadas por ruido de 60 Hz o artefactos musculares (EMG), lo que justifica el uso de filtros (convolución).
## Convolución Discreta.
Es una operación matemática que combina dos señales  para producir una tercera señal. Se utiliza para determinar la respuesta de un sistema lineal e invariante en el tiempo (LTI) ante una entrada determinada.Aplicación Biomédica: Es la base del filtrado lineal; por ejemplo, para suavizar una señal de EOG y eliminar picos de ruido.
## Correlación Cruzada
Es una medida de la similitud entre dos señales en función del desplazamiento de una respecto a la otra. A diferencia de la  Convolución en la correlación no se invierte la señal en el tiempo.Sirve para caracterizar dependencias estadísticas entre dos secuencias.Es fundamental para detectar patrones o latencias, como comparar una señal de EOG actual con un patrón de parpadeo conocido.
## Transformada de Fourier (DFT/FFT)
Herramienta matemática que traslada una señal del dominio del tiempo al dominio de la frecuencia.
Permite analizar qué frecuencias componen la señal biológica. Densidad Espectral de Potencia (PSD), indica cómo se distribuye la potencia de la señal sobre las diferentes frecuencias, crucial para identificar ritmos biológicos.
## Teorema de Muestreo de Nyquist
Establece que para reconstruir una señal analógica a partir de sus muestras, la frecuencia de muestreo debe ser al menos el doble de la frecuencia máxima de la señal .
En la práctica: La guía sugiere digitalizar a 4 veces la frecuencia de Nyquist para evitar el aliasing y garantizar una caracterización precisa en el dominio de la frecuencia.
## Estadísticos en Frecuencia
Para señales biológicas, no basta con la media temporal; se requieren medidas espectrales:Frecuencia Media: El promedio de las frecuencias ponderado por su potencia.Frecuencia Mediana: La frecuencia que divide el espectro de potencia en dos partes iguales.

# procedimiento

## Parte A
### Manual
### python
### Diagrama de flujo

## Parte B
### Manual
### python
### Diagrama de flujo

## Parte C
### python
### Diagrama de flujo
# Adquisición de la señal.

# Análisis de resultados.
# Conclusiones.

