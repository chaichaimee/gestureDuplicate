<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

# <p align="center">gestureDuplicate</p>

<br>

<p align="center">Identifica y gestiona atajos de teclado en conflicto y limpia tu configuración de NVDA.</p>

<br>

<p align="center"><b>Autor:</b> Chai Chaimee</p>
<p align="center"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>

---

## Descripción
**gestureDuplicate** es un complemento de NVDA de grado profesional diseñado para mantener la salud y eficiencia de la configuración de tu lector de pantalla. Te ayuda a identificar gestos de entrada en conflicto (atajos duplicados), gestionar asignaciones personalizadas y realizar una limpieza profunda de los datos de configuración restantes de complementos desinstalados.

El complemento proporciona tres herramientas de mantenimiento esenciales:
* **Comprobar gestos duplicados** — Detecta y enumera todos los gestos duplicados en todos los contextos (global, módulos de aplicación, etc.).
* **Gestión de mis gestos** — Te permite ver y eliminar de forma segura los gestos personalizados asignados a complementos que ya no están instalados.
* **Limpiar configuración (nvda.ini)** — Identifica y elimina secciones de configuración obsoletas pertenecientes a complementos desinstalados que aún residen en tu archivo *nvda.ini* principal.

> **Importante:** Con el tiempo, la desinstalación de complementos a menudo deja ajustes "fantasma" en *nvda.ini* y *gestures.ini*. Esto puede provocar un aumento del uso de memoria, conflictos de configuración o comportamientos inesperados. Esta herramienta garantiza que tu NVDA se mantenga ligero y estable.

<br>

## Teclas rápidas
> **Windows + Mayús + G**
> <br>
> • **Un toque:** Abrir el diálogo **Comprobar gestos duplicados**
> <br>
> • **Dos toques:** Abrir el diálogo **Gestión de mis gestos**
> <br>
> • **Tres toques:** Abrir el diálogo **Limpiar configuración**

<br>

**Acceso al menú: Menú NVDA → Herramientas → gestureDuplicate →**
* Comprobar gestos duplicados...
* Gestionar gestos personalizados...
* Limpiar configuración...

<br>

## Características
* **Detección de gestos duplicados:** Escanea todas las asignaciones cargadas (Núcleo + Complementos) para encontrar conflictos funcionales.
* **Navegación inteligente:** Salto con un solo clic al diálogo estándar de NVDA "Gestos de entrada" con el script relevante preseleccionado para una corrección inmediata.
* **Limpieza de gestos fantasma:** Se dirige específicamente a *gestures.ini* para encontrar entradas vinculadas a complementos faltantes, mostrándolas en gris para una fácil identificación.
* **Limpieza de configuración avanzada:** Escanea el *nvda.ini* principal en busca de secciones sobrantes de complementos desinstalados, permitiéndote "purgar" ajustes obsoletos de forma segura.
* **Acciones por lote:** Admite la eliminación de elementos individuales, todos los gestos de un complemento específico o la limpieza de todas las asignaciones de complementos personalizados a la vez.
* **Flujo de trabajo multi-toque:** Cambia rápidamente entre las herramientas de detección, gestión y limpieza usando una sola tecla rápida.
* **Enfocado en la accesibilidad:** Todos los diálogos son totalmente accesibles por teclado con soporte para Intro (ejecutar), Espacio (alternar), Suprimir (eliminar) y Escape (cerrar).

<br>

## Cómo limpiar tu configuración
Para que NVDA siga funcionando de la mejor manera, sigue estos pasos:
1. Abre la herramienta **Limpiar configuración** (Tres toques **Windows+Mayús+G**).
2. Revisa la lista de secciones encontradas en tu *nvda.ini*.
3. Marca las casillas de los complementos que ya hayas desinstalado.
4. Presiona **Eliminar seleccionados** para borrar de forma segura esas secciones de tu archivo de configuración.

> **Recomendación:** Ejecuta "Gestión de mis gestos" y "Limpiar configuración" después de cada limpieza importante de complementos para evitar posibles conflictos y mantener tus ajustes organizados.

<br><br>

## Apóyame
Si esta herramienta ha facilitado tu vida, considera impulsar la próxima actualización con una pequeña donación.

<br>

[![Apóyame](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Tu apoyo significa el mundo. Construyamos algo grande juntos.

<br>

© 2026 Chai Chaimee Complemento de NVDA Lanzado bajo GNU