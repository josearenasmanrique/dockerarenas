FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip


# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor (app.py y alimentos.db)
COPY . /app

# Instala las dependencias de la aplicación
RUN pip3 --no-cache-dir install -r requirements.txt


# Ejecuta la aplicación Flask
CMD ["python3", "apirest.py"]

