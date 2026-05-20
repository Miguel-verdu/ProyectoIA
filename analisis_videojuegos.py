import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo visual de los gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)


# ─────────────────────────────────────────────
# 1. CARGA Y EXPLORACIÓN INICIAL DE DATOS
# ─────────────────────────────────────────────
print("=" * 50)
print("1. CARGA Y EXPLORACIÓN INICIAL")
print("=" * 50)

# Cargar el CSV en un DataFrame
df = pd.read_csv("dataset_videojuegos.csv")

# Ver las primeras filas para comprobar que cargó bien
print("\nPrimeras 5 filas:")
print(df.head())

# Dimensiones del dataset (filas x columnas)
print(f"\nEl dataset tiene {df.shape[0]} juegos y {df.shape[1]} columnas.")

# Nombre y tipo de cada columna
print("\nColumnas y tipos de datos:")
print(df.dtypes)


# ─────────────────────────────────────────────
# 2. LIMPIEZA DE DATOS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("2. LIMPIEZA DE DATOS")
print("=" * 50)

# --- 2.1 Verificar valores nulos ---
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Eliminamos filas con valores nulos
df.dropna(inplace=True)

# --- 2.2 Verificar duplicados ---
duplicados = df.duplicated().sum()
print(f"\nFilas duplicadas: {duplicados}")

# Eliminamos filas duplicadas
df.drop_duplicates(inplace=True)

# --- 2.3 Verificar tipos de datos y corregirlos si hace falta ---
# La columna 'año' debería ser entero
df["año"] = df["año"].astype(int)

# La columna 'completado' debería ser booleana
# (ya lo es, pero lo confirmamos)
df["completado"] = df["completado"].astype(bool)

print("\nTipos de datos tras la limpieza:")
print(df.dtypes)

# --- 2.4 Resumen rápido del dataset limpio ---
print("\nResumen del dataset:")
print(df.info())


# ─────────────────────────────────────────────
# 3. ANÁLISIS ESTADÍSTICO
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("3. ANÁLISIS ESTADÍSTICO")
print("=" * 50)

# --- 3.1 Estadísticas descriptivas generales ---
print("\nEstadísticas descriptivas (columnas numéricas):")
print(df[["año", "horas_jugadas", "puntuacion"]].describe())

# --- 3.2 Media de horas jugadas y puntuación ---
media_horas = df["horas_jugadas"].mean()
media_puntuacion = df["puntuacion"].mean()
print(f"\nHoras promedio por juego: {media_horas:.1f} h")
print(f"Puntuación media:         {media_puntuacion:.2f} / 10")

# --- 3.3 Conteo de juegos por género ---
print("\nJuegos por género:")
print(df["genero"].value_counts())

# --- 3.4 Conteo de juegos por plataforma ---
print("\nJuegos por plataforma:")
print(df["plataforma"].value_counts())

# --- 3.5 ¿Cuántos juegos has completado? ---
completados = df["completado"].value_counts()
print(f"\nJuegos completados:     {completados.get(True, 0)}")
print(f"Juegos no completados:  {completados.get(False, 0)}")

# --- 3.6 Top 5 juegos con más horas jugadas ---
print("\nTop 5 juegos con más horas:")
top_horas = df[["nombre", "horas_jugadas"]].sort_values("horas_jugadas", ascending=False).head(5)
print(top_horas.to_string(index=False))

# --- 3.7 Puntuación media por género ---
print("\nPuntuación media por género:")
puntuacion_genero = df.groupby("genero")["puntuacion"].mean().sort_values(ascending=False)
print(puntuacion_genero.round(2))

# --- 3.8 Correlación entre horas jugadas y puntuación ---
correlacion = df["horas_jugadas"].corr(df["puntuacion"])
print(f"\nCorrelación horas jugadas ↔ puntuación: {correlacion:.2f}")
print("(1 = muy positiva, 0 = ninguna, -1 = muy negativa)")


# ─────────────────────────────────────────────
# 4. VISUALIZACIONES
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("4. GENERANDO GRÁFICOS...")
print("=" * 50)

# ── Gráfico 1: Juegos por género (barras horizontales) ──
fig, ax = plt.subplots()
df["genero"].value_counts().plot(kind="barh", ax=ax, color="steelblue", edgecolor="black")
ax.set_title("Número de juegos por género", fontsize=14, fontweight="bold")
ax.set_xlabel("Número de juegos")
ax.set_ylabel("Género")
ax.invert_yaxis()  # El más frecuente arriba
plt.tight_layout()
plt.savefig("grafico1_generos.png", dpi=150)
plt.close()
print("✓ Gráfico 1 guardado: grafico1_generos.png")

# ── Gráfico 2: Histograma de horas jugadas ──
fig, ax = plt.subplots()
df["horas_jugadas"].plot(kind="hist", bins=8, ax=ax, color="darkorange", edgecolor="black")
ax.set_title("Distribución de horas jugadas por juego", fontsize=14, fontweight="bold")
ax.set_xlabel("Horas jugadas")
ax.set_ylabel("Número de juegos")
plt.tight_layout()
plt.savefig("grafico2_histograma_horas.png", dpi=150)
plt.close()
print("✓ Gráfico 2 guardado: grafico2_histograma_horas.png")

# ── Gráfico 3: Gráfico circular - juegos completados vs no completados ──
fig, ax = plt.subplots()
completados_count = df["completado"].value_counts()
etiquetas = ["No completado", "Completado"]
colores_pie = ["#FF6B6B", "#51CF66"]
ax.pie(completados_count, labels=etiquetas, colors=colores_pie,
       autopct="%1.0f%%", startangle=90, wedgeprops={"edgecolor": "white"})
ax.set_title("Porcentaje de juegos completados", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("grafico3_completados.png", dpi=150)
plt.close()
print("✓ Gráfico 3 guardado: grafico3_completados.png")


# ─────────────────────────────────────────────
# 5. CONCLUSIONES (resumen en consola)
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("5. CONCLUSIONES")
print("=" * 50)
print(f"""
- Género favorito:       {df['genero'].value_counts().idxmax()}
- Juego con más horas:   {df.loc[df['horas_jugadas'].idxmax(), 'nombre']} ({df['horas_jugadas'].max()} h)
- Puntuación más alta:   {df.loc[df['puntuacion'].idxmax(), 'nombre']} ({df['puntuacion'].max()}/10)
- Media de horas:        {media_horas:.1f} h por juego
- Media de puntuación:   {media_puntuacion:.2f} / 10
- Juegos completados:    {completados.get(True, 0)} de {len(df)} ({completados.get(True, 0)/len(df)*100:.0f}%)
""")

print("Análisis completado, revisa los 3 gráficos generados.")
