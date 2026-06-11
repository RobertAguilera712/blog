Title: Sistema de Monitoreo Térmico en Tiempo Real
Summary: Desarrollo de una aplicación de escritorio de alta precisión que centraliza, procesa y visualiza datos térmicos provenientes de hardware embebido en tiempo real.

![Interfaz del Monitor de Temperatura]({static}/images/Monitor de temperatura.png)

Este proyecto demuestra la viabilidad de integrar software empresarial con hardware de bajo costo para el control de entornos. Desarrollé una solución robusta capaz de capturar variables físicas del entorno, procesarlas mediante comunicación serial y desplegarlas en una interfaz gráfica intuitiva, un flujo de trabajo crítico en sectores como la automatización industrial, domótica y soporte de TI.

## Valor Técnico y Arquitectura del Proyecto

El desarrollo se enfocó en optimizar la fluidez de los datos y garantizar una experiencia de usuario profesional mediante los siguientes pilares:

* **Arquitectura de Software Decoplada:** Separación estricta de la lógica de negocio y la interfaz de usuario mediante el patrón FXML y Scene Builder, facilitando el mantenimiento futuro del sistema.
* **Procesamiento Concurrente:** Gestión eficiente de hilos en Java para evitar el congelamiento de la interfaz gráfica mientras se reciben flujos continuos de datos a través del puerto serial.
* **Comunicación de Bajo Nivel Confiable:** Implementación de protocolos estables de lectura de datos utilizando la librería `jSerial-COM` para garantizar cero pérdida de paquetes desde el microcontrolador.

## Stack Tecnológico

* **Lenguaje y Framework:** Java 8 / JavaFX (Construcción de interfaces ricas y reactivas)
* **Entorno y Diseño:** NetBeans / Scene Builder (Diseño modular de componentes visuales)
* **Hardware y Firmware:** Arduino UNO / Arduino IDE / C++ (Programación de sensores y control de puertos E/S)
* **Conectividad:** jSerial-COM (Abstracción del puerto serie para sistemas operativos cruzados)

## Habilidades Aplicadas Clave para tu Negocio

* Integración integral de soluciones de Software y Hardware (IoT).
* Diseño de interfaces limpias, adaptables y enfocadas en la usabilidad del cliente.
* Escritura de código limpio, documentado y optimizado para entornos con recursos limitados.

<a href="https://github.com/RobertAguilera712/Temp-Monitor" class="btn btn-danger d-block mb-3" target="_blank" rel="noopener"><i class="bi bi-github"></i> Explorar Código en GitHub</a>
<a href="./contact.html" class="btn btn-danger d-block mb-3" rel="noopener"><i class="bi bi-envelope-fill"></i> ¿Tienes un proyecto en mente? Contrátame</a>
