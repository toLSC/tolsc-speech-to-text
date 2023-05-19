# toLSC Speech To Text API 🎙️📝

Este repositorio contiene la aplicación de Speech to Text desarrollada en FastAPI con el modelo Whisper. La aplicación convierte el habla en texto utilizando técnicas de procesamiento de voz.

## Instrucciones de Uso

1. Construye la imagen de Docker ejecutando el siguiente comando:

```sh
docker build -t tolsc-s2t
```

2. Inicia el contenedor de Docker con la imagen creada:

```sh
docker run -dp8000:8000 tolsc-s2t
```

3. Realiza las peticiones a través de la API utilizando multipart/formdata con método POST con la llave "audio_file" de la siguiente manera:


```sh
http://your.deploy.ip:8000/speech-to-text
```

También puedes realizar la petición utilizando el siguiente comando de cURL:

```sh
curl -X POST -F "audio_file=@audio.m4a" http://your.deploy.ip:8000/speech-to-text
```

Ten en cuenta que la API solo acepta archivos de audio en formato `.m4a`.

## Colaboradores

- Santiago Fernández (sa.fernandez@javeriana.edu.co)
- Fabian Olarte (olarte_fabian@javeriana.edu.co)
- Mateo Rosero (roseroq-j@javeriana.edu.co)
- Andrés Vásquez (af.vasquezr@javeriana.edu.co)