# Start Guide

This project bundles a frontend dashboard, FastAPI backend, Meilisearch index and a PostgreSQL database. Docker Compose is used to launch all components together.

## Voraussetzungen
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/)

## Starten
1. Öffne ein Terminal im Projektverzeichnis.
2. Starte alle Dienste:
   ```bash
   docker-compose up
   ```
   Das Frontend läuft danach unter http://localhost:5173 und das Backend unter http://localhost:8000.

## Anmeldung
Im Login-Dialog der Anwendung können die folgenden Testbenutzer genutzt werden:

| Benutzername | Passwort | Rolle  |
|--------------|----------|--------|
| `alice`      | `secret` | Nutzer |
| `admin`      | `admin`  | Admin  |

## Nutzung
* **Suche**: Gib einen Begriff ein und filtere nach Typ, Quelle, Themen oder Entitäten.
* **Dokumente**: Öffne einen Treffer, um Metadaten einzusehen.
* **Notizen**: Als eingeloggter Nutzer können Notizen und Tags zu einem Dokument gespeichert werden.
* **Export**: Admins können gespeicherte Notizen als CSV oder PDF herunterladen.

Für eine Übersicht der API besuche http://localhost:8000/docs sobald die Dienste laufen.
