# Usa una imagen base de Python oficial y ligera
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos primero para aprovechar el cache de Docker.
# Si los requerimientos no cambian, esta capa no se reconstruirá.
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio backend (el contexto de build) al directorio de trabajo /app del contenedor.
# Esto incluye tu directorio 'app', los modelos .pkl y los datos .csv.
COPY . .

# Expone el puerto 8000 para que la API sea accesible desde fuera del contenedor
EXPOSE 8000

# Comando para iniciar el servidor Uvicorn cuando el contenedor se ejecute.
# Asume que tu archivo principal está en 'app/main.py' y la instancia de FastAPI se llama 'app'.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
