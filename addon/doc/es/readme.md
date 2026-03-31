<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>gestureDuplicate NVDA Add-on</title>
<style>
body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #f4f4f4; }
.container { max-width: 800px; margin: auto; background: #fff; padding: 20px 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
h1, h2, h3 { text-align: center; }
b { font-weight: bold; }
.section { margin-bottom: 30px; }
.nvda-logo { display: block; margin: 0 auto 20px; width: 120px; height: auto; }
.hotkey { background: #f8f9fa; border-left: 4px solid #3498db; padding: 15px; margin: 15px 0; border-radius: 0 4px 4px 0; }
.feature-item { margin: 15px 0; padding-left: 10px; }
.note { background: #fff3cd; border-left: 4px solid #ffc107; padding: 12px; margin: 15px 0; border-radius: 0 4px 4px 0; }
a { color: #3498db; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="container">
    <div class="section">
        <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="Logo NVDA" class="nvda-logo">
        <h1>gestureDuplicate</h1>
        <br>
        <p style="text-align: center;">Identifica y gestiona atajos de teclado en conflicto y limpia tu configuración de NVDA.</p>
    </div>
    <br>
    <div class="section">
        <p style="text-align: center;"><b>Autor:</b> Chai Chaimee</p>
        <p style="text-align: center;"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>
    </div>
    <hr>
    <div class="section">
        <h2>Descripción</h2>
        <p><b>gestureDuplicate</b> es un complemento profesional para NVDA diseñado para mantener la salud y eficiencia de la configuración de tu lector de pantalla. Te ayuda a identificar gestos de entrada en conflicto (atajos duplicados), gestionar asignaciones personalizadas y realizar una limpieza profunda de restos de configuración de complementos desinstalados.</p>
        <p>El complemento proporciona tres herramientas esenciales de mantenimiento:</p>
        <ul>
            <li><strong>Verificar gestos duplicados</strong> — Detecta y enumera todos los gestos duplicados en todos los contextos (global, módulos de aplicación, etc.).</li>
            <li><strong>Gestión de mis gestos</strong> — Te permite ver y eliminar de forma segura gestos personalizados asignados a complementos que ya no están instalados.</li>
            <li><strong>Limpiar configuración (nvda.ini)</strong> — Identifica y elimina secciones obsoletas de complementos desinstalados que aún residen en tu archivo <em>nvda.ini</em> principal.</li>
        </ul>
        <div class="note">
            <strong>Importante:</strong> Con el tiempo, al desinstalar complementos suelen quedar ajustes "fantasma" en <em>nvda.ini</em> y <em>gestures.ini</em>. Esto puede causar conflictos o un comportamiento inesperado. Esta herramienta mantiene tu NVDA ligero y estable.
        </div>
    </div>
    <br>
    <div class="section">
        <h2>Teclas de acceso rápido</h2>
        <div class="hotkey">
            <strong>Windows + Shift + G</strong><br>
            • <b>Un toque:</b> Abrir el diálogo <strong>Verificar gestos duplicados</strong><br>
            • <b>Dos toques:</b> Abrir el diálogo <strong>Gestión de mis gestos</strong><br>
            • <b>Tres toques:</b> Abrir el diálogo <strong>Limpiar configuración</strong>
        </div>
        <br>
        <p style="padding-left: 20px;">
            <strong>Acceso al menú: Menú NVDA → Herramientas → gestureDuplicate →</strong><br>
                • Verificar gestos duplicados...<br>
                • Gestionar gestos personalizados...<br>
                • Limpiar configuración...
        </p>
    </div>
    <br>
    <div class="section">
        <h2>Características</h2>
        <ul>
            <li class="feature-item"><strong>Detección de gestos duplicados:</strong> Escanea todas las asignaciones cargadas (Núcleo + Complementos) para encontrar conflictos.</li>
            <li class="feature-item"><strong>Navegación inteligente:</strong> Salto con un clic al diálogo estándar de "Gestos de entrada" de NVDA con el script relevante preseleccionado.</li>
            <li class="feature-item"><strong>Limpieza de gestos fantasma:</strong> Localiza entradas en <em>gestures.ini</em> vinculadas a complementos faltantes (mostradas en gris).</li>
            <li class="feature-item"><strong>Limpieza avanzada de configuración:</strong> Escanea <em>nvda.ini</em> en busca de restos de complementos desinstalados para eliminarlos de forma segura.</li>
            <li class="feature-item"><strong>Acciones por lotes:</strong> Permite eliminar elementos individuales, todos los gestos de un complemento específico o todas las asignaciones a la vez.</li>
            <li class="feature-item"><strong>Accesibilidad total:</strong> Todos los diálogos son accesibles mediante teclado (Enter, Espacio, Suprimir, Escape).</li>
        </ul>
    </div>
    <br>
    <div class="section">
        <h2>Cómo limpiar tu configuración</h2>
        <ol>
            <li>Abre la herramienta <strong>Limpiar configuración</strong> (Tres toques <b>Windows+Shift+G</b>).</li>
            <li>Revisa la lista de secciones encontradas en tu <em>nvda.ini</em>.</li>
            <li>Marca las casillas de los complementos que ya has desinstalado.</li>
            <li>Presiona <strong>Eliminar seleccionados</strong> para borrarlos de forma segura.</li>
        </ol>
    </div>

<br><br>
<h2 style="text-align: center;">Apoya el proyecto</h2>
    <p style="text-align: center;">Si <b>gestureDuplicate</b> ha facilitado la gestión de tu NVDA, considera apoyar su desarrollo continuo.</p>
    <p style="text-align: center;">
        <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Visita el repositorio en GitHub</a></strong>
    </p>
    <br>
    <p style="text-align: center; font-size: 0.8em; color: #7f8c8d;">&copy; 2026 Chai Chaimee • Lanzado bajo GNU GPL v2+</p>
</div>
</body>
</html>