# learning_log
 Familiarity with Django. I make a network log 'Learning log' to track the information received on various topics. From The Crash Course in Python by Eric Metiz.

## Secure configuration

Use Python 3.12+ and install `requirements.txt` in an isolated virtual environment.
Django reads process environment variables; it does not load `.env` automatically.
Set SECRET_KEY to a separate newly generated key (at least 50 characters),
DEBUG=false and explicit comma-separated ALLOWED_HOSTS before production startup.
There is no committed or automatic fallback key. For local development only:

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(64))')"
export DEBUG=true
export ALLOWED_HOSTS=localhost,127.0.0.1
```

Keep production values in your hosting secret store or a file outside the source
checkout with mode 600 (parent directory 700). `.env.example` contains names only.
Terminate TLS at a trusted proxy; production enables HTTPS redirects and secure
session/CSRF cookies. Set TRUST_PROXY_SSL_HEADER=1 only when the proxy strips
client-supplied X-Forwarded-Proto and sets it itself. Add exact HTTPS origins to
CSRF_TRUSTED_ORIGINS if needed; never use wildcard hosts. Run
`python manage.py check --deploy` with the production environment.

Before deploying framework upgrades, back up the database, test migrations on a
copy, then run `python manage.py migrate` and collect static files as appropriate.
Any previously committed SECRET_KEY is disclosed even after this change: replace
it in every environment that used it and restart the application. Do not keep the
old value in SECRET_KEY_FALLBACKS; rotation invalidates existing sessions/tokens.
