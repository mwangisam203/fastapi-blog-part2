# 📝 FastAPI Blog

A personal blog web application built with **FastAPI**, **Jinja2 templates**, and **Bootstrap 5**. This project is part of my backend development journey — learning Python, REST APIs, SQL, PostgreSQL, Docker, and cloud infrastructure by building real things.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Templating | Jinja2 |
| Styling | Bootstrap 5, Custom CSS |
| Static Files | FastAPI StaticFiles |
| Server | Uvicorn (ASGI) |
| Fonts | Google Fonts (Montserrat, Nunito) |

---

## 📁 Project Structure

```
fastapi-blog/
├── main.py                  # FastAPI app, routes and post data
├── templates/
│   ├── layout.html          # Base template (navbar, footer, theme toggle)
│   └── home.html            # Home page — lists all blog posts
├── static/
│   ├── css/
│   │   └── main.css         # Custom styles + dark mode + animations
│   ├── images/
│   │   └── profilep.jpeg    # Author profile picture
│   ├── icons/
│   │   ├── favicon.ico
│   │   ├── icon.svg
│   │   └── icon.png
│   └── site.webmanifest
└── .venv/                   # Python virtual environment
```

---

## ⚙️ Features

- **Blog post listing** — Posts displayed as cards with author, date, title and content
- **Author profile pictures** — Circular profile images per post
- **Light / Dark / Auto theme toggle** — Persisted via localStorage
- **Responsive design** — Mobile-friendly via Bootstrap 5 grid
- **Smooth animations** — Card lift on hover, title underline animation, sidebar slide effect
- **REST API endpoints** — JSON responses available alongside the HTML views
- **FastAPI auto docs** — Available at `/docs` (Swagger UI)

---

## 🛣️ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Home page (HTML) |
| `GET` | `/posts` | Returns all posts as JSON |
| `GET` | `/posts/{post_id}` | Returns a single post by ID |
| `GET` | `/docs` | Swagger UI (auto-generated) |

---
🔥 Error Handling
The app has custom error handlers for clean error responses — both for API routes (JSON) and browser routes (HTML error page).
HTTP Exception Handler
Catches all standard HTTP errors (404, 403, 500, etc.). If the request is to an /api route, it returns a JSON response. Otherwise it renders a custom error.html template.

Validation Error Handler
Catches FastAPI's RequestValidationError (triggered when request data fails validation). API routes get a detailed JSON error, browser routes get a friendly error page.
Key design decision: The handlers check request.url.path.startswith("/api") to serve the right response format — JSON for API consumers, HTML for browser users.

## 🏁 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 4. Run the development server

```bash
uvicorn main:app --reload
```

### 5. Open in your browser

```
http://127.0.0.1:8000
```

---

## 🧠 What I Learned Building This

- How FastAPI handles routing, request objects and template responses
- The difference between sync and async route handlers
- How Jinja2 template inheritance works (`layout.html` → `home.html`)
- Serving static files (CSS, images, icons) with FastAPI's `StaticFiles`
- How Bootstrap 5's grid system and dark mode theming works
- Debugging `TypeError: unhashable type: 'dict'` — caused by passing arguments in the wrong order to `TemplateResponse`
- How Starlette's newer `TemplateResponse` signature requires `request` as a direct keyword argument, not inside the context dict

---

## 🐛 Known Issues / Work in Progress

- Posts are currently hardcoded in `main.py` — database integration (PostgreSQL) coming soon
- Login and Register buttons are placeholders — authentication coming soon
- No user accounts or profile management yet
- Docker and cloud deployment coming in future phases

---

## 🗺️ Roadmap

- [ ] PostgreSQL database integration with SQLAlchemy
- [ ] User authentication (register, login, logout)
- [ ] Create, edit and delete posts
- [ ] User profile pages with uploadable profile pictures
- [ ] Dockerize the application
- [ ] Deploy to cloud (AWS / GCP)

---

## 👤 Author

**Mwangi Sam alias Kajeiy**
- GitHub: https://github.com/mwangisam203
- LinkedIn: https://www.linkedin.com/in/samson-maina-26883116a/

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).