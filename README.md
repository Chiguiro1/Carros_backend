# Carros API
API REST para gestionar carros y marcas usando FastAPI y PostgreSQL.

# tecnolocias usadas
- FastAPI
- PostgreSQL (vía Docker)
- SQLAlchemy
- Pydantic

- Docker
- Docker Compose
- Python 3.11 

1. Clona el repositorio:

git clone https://github.com/TU_USUARIO/carros_backend.git

2. Entra en el directorio:

cd carros_backend

3. Levanta el docker:

docker-compose up --build

4. Entra a la api

http://localhost:8020/docs

# Uso en windows
Instala Docker Desktop y asegúrate de tener habilitado el soporte para WSL2 (Windows Subsystem for Linux).

Usa un entorno de terminal como Git Bash o PowerShell. Se recomienda Git Bash porque se comporta más parecido a Linux. Evite usar CMD.exe para ejecutar comandos Docker o Unix como curl.

Si usas montaje de volúmenes en Docker, asegúrate que Docker Desktop tiene acceso a la carpeta donde está tu proyecto. Esto se configura en las opciones de “File Sharing” de Docker Desktop.

Si Docker va lento o se bloquea, verifica que la virtualización esté habilitada en la BIOS y que tu PC tenga recursos suficientes (RAM y CPU).
