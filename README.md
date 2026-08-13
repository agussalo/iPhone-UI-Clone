# iOS 18 Pro Max — Simulador de Interfaz

Recreación interactiva de la interfaz de **iOS 18**, corriendo en una ventana de escritorio nativa mediante **pywebview** (Python) con todo el frontend construido en **HTML, CSS y JavaScript**. Incluye pantalla de bloqueo, Face ID simulado, centro de notificaciones, centro de control y más de 10 apps navegables con distintos niveles de funcionalidad real.

## 📱 Funcionalidades

- **Pantalla de bloqueo** con reloj en vivo, widgets y desbloqueo por Face ID (usa la cámara real para el efecto visual de escaneo)
- **Dynamic Island** interactiva con animación de ecualizador
- **Centro de notificaciones** y **Centro de control** (brillo, volumen, conectividad) deslizables
- **Home screen** con widgets (clima, calendario), grid de apps y dock

### Apps incluidas
| App | Funcionalidad |
|---|---|
| WhatsApp | Lista de chats y vista de conversación (solo lectura, no permite escribir) |
| Apple Music | Reproductor con interfaz completa (play/pausa, progreso) — sin audio real |
| Calculadora | Totalmente funcional |
| Reloj | Cronómetro y temporizador funcionales |
| Mapas | Mapa real con Leaflet + OpenStreetMap |
| Cámara | Usa la cámara del dispositivo real |
| Fotos | Galería con imágenes de muestra |
| Notas | Editor de texto simple |
| Mail | Buzón (vacío, de demostración) |
| Ajustes | Lista de opciones con switches estilo iOS |
| Block Beast | Mini-juego simple en canvas |

## 🛠️ Tecnologías

- Python 3 + [pywebview](https://pywebview.flowrl.com/) (ventana nativa de escritorio)
- HTML5, CSS3, JavaScript (vanilla)
- [Leaflet.js](https://leafletjs.com/) para el mapa real
- [Font Awesome](https://fontawesome.com/) para los íconos

## ▶️ Cómo correrlo

```bash
pip install pywebview
python iphone_ios18.py
```

Se abre una ventana de escritorio con el iPhone simulado. Para Face ID y la Cámara, el navegador/sistema pedirá permiso de acceso a la cámara.

## ✨ Detalles técnicos

- Todo el HTML/CSS/JS vive embebido en un único archivo Python, renderizado dentro de la ventana con pywebview
- Estados de UI (apps abiertas, overlays, pantalla bloqueada/desbloqueada) manejados con clases CSS y transiciones
- Integración con `getUserMedia` para el acceso real a cámara (Face ID y app Cámara)
- Mapa interactivo real embebido con Leaflet + tiles de OpenStreetMap

---

Proyecto de práctica personal, hecho para explorar diseño de interfaces complejas, microinteracciones y estados de UI en HTML/CSS/JS, empaquetado como app de escritorio con Python.
