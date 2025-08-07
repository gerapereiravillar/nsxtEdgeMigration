# EdgeMigrator

Una aplicación Flask que permite migrar configuraciones de Edge entre dos instancias de vCloud Director. API RESTful lista para integrarse con GUI o CLI.

## Características

- Autenticación contra dos entornos vCloud Director
- Migración de configuración de Edge vía API
- Arquitectura limpia y modular
- Pronto para expandirse con GUI o CLI

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/edge-migrator.git
cd edge-migrator
```

2. Crea un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutá la app:
```bash
python main.py
```

2. Desde el frontend o Postman, hacé una petición:
```http
POST http://localhost:5000/migrate
Content-Type: application/json
{
  "source_url": "...",
  "source_token": "...",
  "dest_url": "...",
  "dest_token": "...",
  "edge_id": "edge-1"
}
```

3. También podés abrir la interfaz en:
http://localhost:5000

## Endpoints API

### `POST /migrate`
Migrar un edge de un entorno a otro.

### `GET /health`
Verifica si el backend está corriendo.

## Contribuciones

Pull requests bienvenidos. Para cambios mayores, por favor abrí un issue primero para discutir qué querés cambiar.

## Licencia

MIT

## Autor

Gerardo Pereira - [LinkedIn](https://www.linkedin.com/in/gerardopereira)
