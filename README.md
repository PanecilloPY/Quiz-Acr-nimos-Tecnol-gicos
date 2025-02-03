# Quiz Acrónimos Tecnológicos 🚀

¡Bienvenido al **Quiz Acrónimos Tecnológicos**! Este es un proyecto interactivo que pone a prueba tus conocimientos sobre acrónimos y siglas relacionadas con la tecnología. El quiz se ejecuta en un servidor local y cuenta con un diseño moderno, retroalimentación visual y la posibilidad de reiniciar el juego.

---

## Características ✨

- **Preguntas y respuestas**: Más de 30 preguntas sobre acrónimos y siglas tecnológicas.
- **Retroalimentación visual**: Las respuestas se marcan en **azul** (seleccionada), **verde** (correcta) o **rojo** (incorrecta).
- **Fondo animado**: Un gradiente dinámico que cambia de color.
- **Créditos**: Muestra "PanecilloPY" en la esquina inferior derecha.
- **Reinicio**: Un botón de "Volver a jugar" permite reiniciar el quiz con preguntas y opciones mezcladas.

---

## Requisitos 📋

Para ejecutar este proyecto, necesitas tener instalado:

- **Python 3.8 o superior**.
- **Flask**: Un framework web ligero para Python.
- **Colorama**: Librería que nos permitirá mostrar texto en distintos colores en la consola

---

## Instalación 🛠️

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/quiz-tecnologico.git
   cd quiz-tecnologico
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso 🚀

1. **Inicia el servidor**:
   - Ejecuta el menú principal:
     
     ```bash
     python menu.py
     ```
   - Selecciona la opción **1** para iniciar el servidor en `http://127.0.0.1:5000/`.

2. **Juega al quiz**:
   - Abre tu navegador y busca `http://127.0.0.1:5000/`.
   - Responde las preguntas seleccionando una opción.
   - Usa el botón **Siguiente** para avanzar.
   - Al finalizar, puedes reiniciar el quiz con el botón **Volver a jugar**.

---

## Estructura del proyecto 📂

```
quiz-tecnologico/
├── app.py                # Backend con Flask
├── menu.py               # Menú para ejecutar el servidor
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo
├── static/
│   ├── style.css         # Estilos CSS
│   └── script.js         # Lógica del frontend
└── templates/
    └── index.html        # Plantilla HTML del quiz
```

---

## Librerías utilizadas 📚

- **Flask**: Framework web para Python.
- **Random**: Módulo de Python para mezclar preguntas y opciones.

---

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un **Pull Request**.

---

## Licencia 📄

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

