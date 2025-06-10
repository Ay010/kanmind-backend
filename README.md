# KanMind Backend

Ein Backend-Projekt für Kanban-Boards und Aufgabenverwaltung, basierend auf Django und Django REST Framework.

## Features

- Benutzerverwaltung mit eigenem User-Modell
- Token-basierte Authentifizierung
- REST-API für Boards, Tasks und User
- CORS-Unterstützung (für Entwicklung offen für alle Ursprünge)

## Voraussetzungen

- Python 3.10 oder höher
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) Virtuelle Umgebung (empfohlen)

## Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/Ay010/kanmind-backend.git
   cd kanmind-backend
   ```
2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Konfiguration

- Die wichtigsten Einstellungen befinden sich in `kanmind/settings.py`.
- Für produktive Nutzung sollten sensible Daten (wie `SECRET_KEY`) in eine `.env`-Datei ausgelagert werden (z.B. mit [django-environ](https://django-environ.readthedocs.io/en/latest/)).
- Standardmäßig wird SQLite als Datenbank verwendet. Für andere Datenbanken bitte die Einstellungen in `settings.py` anpassen.

## Migrationen & Superuser

1. Migrationen anwenden:
   ```bash
   python manage.py migrate
   ```
2. Superuser anlegen:
   ```bash
   python manage.py createsuperuser
   ```

## Projekt starten

```bash
python manage.py runserver
```

Das Backend ist dann erreichbar unter: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API-Authentifizierung

- Die API verwendet Token-Authentifizierung.
- Nach dem Login erhält der User einen Token, der bei weiteren API-Requests im Header `Authorization: Token <token>` mitgesendet werden muss.

## Besonderheiten & Hinweise

- **CORS:** Für Entwicklung ist CORS für alle Ursprünge erlaubt. In Produktion bitte auf spezifische Domains einschränken!
- **User-Modell:** Es wird ein eigenes User-Modell verwendet (`user_auth.User`).
- **Standardrechte:** Alle API-Endpunkte sind nur für authentifizierte Nutzer zugänglich.
- **Datenbank:** Die Datei `db.sqlite3` ist in `.gitignore` und wird nicht mitgeliefert.

## Beispiel: Token erhalten

```bash
POST /user_auth/api/token/
{
  "username": "<dein_username>",
  "password": "<dein_passwort>"
}
```

Antwort:

```json
{
  "token": "<dein_token>"
}
```

## Weiterführende Links

- [Django Dokumentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**Fragen oder Probleme?**
Bitte ein Issue im [GitHub-Repository](https://github.com/Ay010/kanmind-backend) erstellen.
