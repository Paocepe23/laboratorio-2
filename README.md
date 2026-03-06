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
Esta fase se enfoca en el análisis de señales trigonométricas:Generación de señales, se definen las funciones con un periodo de muestreo.
Operación de Correlación se calcula la correlación cruzada entre ambas señales para medir su grado de similitud y se analiza la secuencia resultante de forma gráfica.
## Fase de Procesamiento de Señales Biológicas y Frecuencia.
Es la etapa de aplicación práctica con hardware y señales reales:

Adquisición: Se geenera una señal biológica mediante el generador de señales.

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
<img width="768" height="554" alt="image" src="https://github.com/user-attachments/assets/52060e3c-f381-4d19-8979-551c41697321" />
<img width="748" height="632" alt="image" src="https://github.com/user-attachments/assets/a36e713a-c086-432c-a98b-2f3f9d35ca04" />
<img width="647" height="474" alt="image" src="https://github.com/user-attachments/assets/6a3fd364-eac6-4464-8091-b97c9ae20ca4" />
<img width="713" height="410" alt="image" src="https://github.com/user-attachments/assets/0f6f2e8b-8a82-4bc0-a507-f2a4fb3ae356" />



### python
### Diagrama de flujo

## Parte B
### Manual
<img width="482" height="647" alt="image" src="https://github.com/user-attachments/assets/fb9b16fd-2f67-466c-8cf4-d50857f093bf" />
<img width="468" height="645" alt="image" src="https://github.com/user-attachments/assets/e3fffd46-5f0a-48a7-b509-760d371ce3b1" />
<img width="480" height="670" alt="image" src="https://github.com/user-attachments/assets/9e02acc4-e17b-499b-a2b6-963010cc42b7" />
<img width="485" height="658" alt="image" src="https://github.com/user-attachments/assets/6f42e256-7a04-4918-b68c-52714bd32250" />
<img width="471" height="668" alt="image" src="https://github.com/user-attachments/assets/38716780-a2fb-496f-b6a1-9a42ff8f645e" />
<img width="483" height="651" alt="image" src="https://github.com/user-attachments/assets/2eeb5a74-579c-40e1-9077-4830ba51d6a8" />
<img width="450" height="641" alt="image" src="https://github.com/user-attachments/assets/fa009f60-0498-4b8f-b0f5-a06d0191b95c" />
<img width="471" height="673" alt="image" src="https://github.com/user-attachments/assets/df5748a0-890b-412b-aa86-52b9ae8ae071" />
<img width="468" height="648" alt="image" src="https://github.com/user-attachments/assets/394f6c49-a6b8-4e45-bf22-71cc2d5ba899" />
<img width="473" height="651" alt="image" src="https://github.com/user-attachments/assets/aaccf875-f763-4dcf-a7b6-ee8627eda6a5" />
<img width="462" height="641" alt="image" src="https://github.com/user-attachments/assets/2f2a3644-7efd-48f4-a528-52eb49d91d1e" />
### ¿En qué situaciones resulta útil aplicar la correlación cruzada en el procesamiento digital de señales? 

En procesamiento de señales biomédicas, sirve para reconocer una forma de onda específica (como un latido cardíaco) dentro de una señal ruidosa al compararla con un patrón de referencia.

### python
### Diagrama de flujo

## Parte C
### python
### Diagrama de flujo
# Adquisición de la señal.

# Análisis de resultados.
# Conclusiones.
# PREGUNTAS PARA LA DISCUSIÓN
## ¿Qué utilidad poseen herramientas como la convolución y la correlación en áreas como procesamiento de imágenes?
Convolución: Se utiliza principalmente para el filtrado digital. Al aplicar una matriz pequeña (llamada núcleo o kernel) sobre la imagen, se pueden lograr efectos como el suavizado (reducción de ruido), el realce de bordes (detección de contornos) o el desenfoque. Es la base de las Redes Neuronales Convolucionales (CNN) para visión artificial.

Correlación: Su principal uso es el reconocimiento de patrones (Template Matching). Permite buscar una imagen pequeña (patrón) dentro de una más grande. El punto donde la correlación es máxima indica la ubicación exacta donde se encuentra el objeto buscado.

## ¿En cuáles contextos de aplicación la transformada de Fourier ofrece un conjunto de características con mayor poder discriminativo que las quesuelen considerarse desde el dominio temporal?
Identificación de ritmos biológicos: En señales como el EEG o el ECG, es más fácil identificar patologías observando picos en frecuencias específicas (como el ritmo alfa o arritmias) que analizando la señal cruda en el tiempo.

Eliminación de ruido periódico: Si una señal tiene interferencia de la red eléctrica (60 Hz), en el dominio del tiempo el ruido se mezcla con la señal, pero en el dominio de la frecuencia aparece como un pico aislado muy fácil de identificar y filtrar.

Compresión de datos: Permite identificar qué componentes de frecuencia tienen poca energía y pueden eliminarse sin perder información vital, algo imposible de determinar solo viendo la señal temporal.

## ¿En qué se diferencia la correlación cruzada de la convolución? 
Inversión de la señal: En la convolución, una de las señales se debe invertir en el tiempo (reflejar) antes de deslizarla y sumar. En la correlación cruzada, las señales se comparan directamente sin invertir ninguna.
Propiedad de conmutatividad: La convolución es conmutativa, pero la correlación cruzada no lo es; el orden de las señales cambia el resultado del desplazamiento.

