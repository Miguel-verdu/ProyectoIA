# Análisis de Videojuegos Personales
**P04 - Proyecto de análisis de datos | Opción B**

---

## 1. Introducción

Este proyecto analiza 20 videojuegos de mi biblioteca personal para descubrir patrones en mis preferencias: géneros favoritos, plataformas más usadas, relación entre horas jugadas y puntuación, y hábitos de completar juegos.

Los datos son reales y han sido recopilados manualmente a partir de mi experiencia personal con cada juego.

---

## 2. Dataset

- **Archivo:** `dataset_videojuegos.csv`
- **Registros:** 20 juegos
- **Columnas:**

| Columna | Tipo | Descripción |
|---|---|---|
| `nombre` | str | Título del juego |
| `plataforma` | str | Plataforma principal jugada |
| `genero` | str | Género del juego |
| `año` | int | Año de lanzamiento |
| `horas_jugadas` | float | Horas invertidas |
| `puntuacion` | float | Mi nota personal (0-10) |
| `desarrolladora` | str | Estudio que lo desarrolló |
| `completado` | bool | Si he completado el juego |

---

## 3. Metodología

Los datos se recopilaron revisando mi biblioteca personal de juegos y el historial de plataformas (Steam, etc.). Las puntuaciones son subjetivas y reflejan mi experiencia personal.

---

## 4. Hallazgos principales

- **Género favorito:** RPG y Acción (5 juegos cada uno)
- **Plataforma más usada:** PC (14 de 20 juegos)
- **Juego con más horas:** League of Legends (250 h)
- **Puntuación media:** 8.2 / 10
- **Juegos completados:** solo el 40% (8 de 20)
- **Correlación horas ↔ puntuación:** 0.16 (prácticamente nula — juego muchas horas a juegos que no puntúo muy alto, como el LoL)

---

## 5. Conclusiones

Soy un jugador orientado a los RPGs de historia (Fire Emblem, Persona, NieR), pero también invierto muchas horas en juegos multijugador que no puntúo tan alto, principalmente por que me dedico a jugarlos con amigos, lo que mejora la experiencia en juegos que objetivamente en solitario no disfruto tanto. Tiendo a no completar los juegos: solo termino 4 de cada 10, esto es en parte debido a que los juegos multijugador que he mencionado no tienen final definido y/o no se pueden completar.

---

## 6. Estructura del repositorio

```
ProyectoIA/
│
├── dataset_videojuegos.csv       # Dataset con los 20 juegos
├── analisis_videojuegos.py       # Código principal del análisis
├── requirements.txt              # Librerías necesarias
├── README.md                     # Este archivo
│
├── grafico1_generos.png          # Juegos por género (barras)
├── grafico2_histograma_horas.png # Distribución de horas (histograma)
└── grafico3_completados.png      # % completados (circular)
```

---

## 7. Cómo ejecutar

```bash
# 1. Instalar dependencias
pip install -r requirements.txt
# En caso de que no funcione, prueba con la ruta completa de Python (Sustituye la ubicación por la tuya)
C:\Users\migue\AppData\Local\Programs\Python\Python312\python.exe -m pip install -r requirements.txt

# 2. Ejecutar el análisis
python analisis_videojuegos.py
```
