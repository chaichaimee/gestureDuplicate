# gestureDuplicate

<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

<p align="center">
  Identifica y gestiona atajos de teclado en conflicto en tu configuración de NVDA
</p>

<p align="center">
  <strong>autor:</strong> chai chaimee<br>
  <strong>url:</strong> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a>
</p>

---

## Descripción

gestureDuplicate es un complemento de NVDA que te ayuda a identificar y gestionar gestos de entrada en conflicto (atajos duplicados) así como limpiar gestos personalizados sobrantes de complementos desinstalados en tu configuración de NVDA.

El complemento incluye dos herramientas potentes:

- **Comprobar gestos duplicados** — detecta y lista todos los gestos duplicados en todos los contextos (global, módulos de aplicaciones, etc.)
- **Gestión de mis gestos** — te permite ver y eliminar de forma segura gestos personalizados asignados a complementos que ya no están instalados

> **Importante:**  
> Después de desinstalar complementos, muchas asignaciones de atajos personalizados suelen permanecer en *gestures.ini* causando confusión o conflictos. Este complemento te ayuda a limpiarlos fácilmente y de forma segura.

## Atajos de teclado

**Windows+Shift+G**

- Toque simple → Abre el diálogo **Comprobar gestos duplicados**
- Toque doble → Abre el diálogo **Gestión de mis gestos**

O a través del menú:

**NVDA → Herramientas → gestureDuplicate →**

- Comprobar gestos duplicados
- Gestión de mis gestos

## Características

- **Detección de gestos duplicados** — escanea todos los mapeos de gestos cargados en NVDA (núcleo + complementos)
- Lista limpia y legible que muestra el gesto, nombre de función y contexto/categoría
- Salto con un clic al diálogo estándar de Gestos de entrada de NVDA con nombre de script prefiltrado
- **Gestión de gestos sobrantes** de complementos instalados anteriormente (ahora desinstalados)
- Solo muestra gestos que pertenecen a complementos (ignora gestos integrados de NVDA)
- Texto gris para gestos de complementos que ya no están instalados
- Eliminar gestos individuales o eliminar todos los gestos de un complemento específico de una vez
- **Función Limpiar todo** — elimina gestos personalizados de todos los complementos en una sola operación
- Soporte para doble toque en atajos para cambiar rápidamente entre ambas herramientas
- Diálogos completamente accesibles por teclado (soporte para Enter, Supr, Escape)

> **Recomendación:**  
> Después de desinstalar cualquier complemento, usa "Gestión de mis gestos" para limpiar las asignaciones restantes y prevenir conflictos potenciales.