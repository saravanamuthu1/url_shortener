# URL Shortener API 🚀

A high-performance URL Shortener REST API built with **FastAPI**, **Async SQLAlchemy**, and managed with **`uv`**.

---

## 🌟 Features

- 🔑 **Authentication & Authorization**: User registration, login, and API token generation.
- 🔗 **URL Shortening & Custom Aliases**: Generate unique short links or create personalized aliases with expiration handling (`expires_at`) and access control (`is_public`).
- 🔄 **Fast Redirection**: High-performance HTTP 302 redirection endpoint (`/{short_code}`).
- 📊 **Analytics & Event Tracking**: Logs redirection events including timestamp, IP address, device type, and geolocation (`country`).
- 👥 **Access Permissions**: Share private URL management permissions across users (`url_permission`).

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM & Database**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (AsyncIO Engine with `aiosqlite` / PostgreSQL)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

---

## 📁 Project Structure

```text
url_shortner/
├── app/
│   ├── main.py              # FastAPI application initialization & router registration
│   ├── config.py            # Environment configuration settings
│   ├── database.py          # Async database engine & session dependency
│   ├── models.py            # SQLAlchemy ORM models (User, Url, UrlPermission, RedirectEvent)
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   └── routers/             # API route modules
│       ├── auth.py          # /auth authentication endpoints
│       ├── url.py           # /urls link management & analytics endpoints
│       └── redirect.py      # /{short_code} redirection handling
├── tests/                   # Automated unit and integration tests
├── pyproject.toml           # Project metadata and dependencies
└── uv.lock                  # Lockfile managed by uv
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.13+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) installed on your system

### Installation & Setup

1. **Clone the repository** and navigate to the project directory:
   ```bash
   cd url_shortner
   ```

2. **Sync dependencies and virtual environment**:
   ```bash
   uv sync
   ```

3. **Run the development server**:
   ```bash
   uv run uvicorn app.main:app --reload
   ```
   The API server will be available at `http://127.0.0.1:8000`.

4. **Interactive API Documentation**:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🔌 API Endpoints Summary

### 🔑 Authentication (`/auth`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/signup` | Register a new user account |
| `POST` | `/auth/login` | Authenticate user credentials |
| `POST` | `/auth/token` | Generate API access token |

### 🔗 URL Management (`/urls`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/urls/shorten` | Create a new short URL |
| `GET` | `/urls/all` | List all URLs owned or accessible by user |
| `GET` | `/urls/{short_code}` | Get detailed metadata of a short URL |
| `PATCH` | `/urls/{short_code}` | Update short URL settings or target link |
| `DELETE` | `/urls/{short_code}` | Delete a short URL |
| `GET` | `/urls/{short_code}/analytics` | Retrieve click analytics & redirect event logs |
| `POST` | `/urls/{short_code}/permissions` | Share URL access permissions with another user |
| `DELETE` | `/urls/{short_code}/permissions/{user_id}` | Revoke URL access permissions |

### 🔄 Redirection
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/{short_code}` | Redirect to target original URL & track analytics event |