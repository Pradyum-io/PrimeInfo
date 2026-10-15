# Deploying the contact-form backend

The backend is standard-library Python only (no `requirements.txt` needed).
The static website stays on GitHub Pages; only `/api/*` is hosted here.

## Start command
```
python3 server.py
```
Build command: none (use `true` if the host requires one). Python 3.8+.
Health check path: `/api/health` (returns only `{"status","service"}`).

## Required environment variables (production)
| Variable | Value |
|---|---|
| `APP_ENV` | `production` |
| `CORS_ORIGINS` | `https://primecoreinfo.com` (comma-separate extra origins). `*` is rejected. |
| `DATABASE_PATH` | Absolute path on a persistent disk, e.g. `/var/data/enquiries.db` |
| `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_USE_TLS` | Email provider (Gmail needs an app password) |
| `NOTIFICATION_EMAIL` | Recipient (default `connect@primecoreinfo.com`) |

Optional: `PORT` (usually injected by the host), `TRUSTED_PROXY_COUNT` (see below),
`RATE_LIMIT_MAX_REQUESTS`, `RATE_LIMIT_WINDOW_SECONDS`, `SERVE_STATIC` (default `false` in production).

The server **refuses to start** in production if `CORS_ORIGINS` is missing or
contains `*`, or if `DATABASE_PATH` is not an absolute path in an existing,
writable directory. Set secrets in the host dashboard, never in the repo.

## Persistent storage (example: Render)
SQLite needs a disk that survives deploys. On Render: use a **Web Service**
on a paid plan, add a **Disk** (e.g. mount path `/var/data`), and set
`DATABASE_PATH=/var/data/enquiries.db`. Without a disk, inquiries are lost on
every deploy/restart. Other hosts: mount a volume and point `DATABASE_PATH` at it.
Back up the database file regularly.

## Client IP / rate limiting
`X-Forwarded-For` is ignored by default (the direct peer address is used).
Behind a reverse proxy, every client would then share the proxy's IP, so set
`TRUSTED_PROXY_COUNT` to the number of proxies you control (typically `1`).
The rate-limit state is in memory and resets on restart.

## Wiring the website
Set `data-api-url="https://<your-backend-host>"` on the form in `build_pages.py`,
run `python3 build_pages.py`, and publish the site.

## Local development
```
python3 server.py     # APP_ENV defaults to development; serves site + API on :8000
```
Local mode serves only allow-listed web file types and never dotfiles,
`backend/`, `.py`, `.db` or `.env` files.
