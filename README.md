# CSC325 – CI/CD Pipeline with GitHub Actions

A small Django + Django REST Framework backend that is tested and deployed by a
four-stage GitHub Actions pipeline (`.github/workflows/csc325_ci_cd.yml`).

## Endpoints

| Method | Path            | Response                                           |
|--------|-----------------|----------------------------------------------------|
| GET    | `/api/health/`  | `{"status": "ok"}`                                 |
| GET    | `/api/hello/`   | `{"message": "Hello, World!", "course": "CSC325"}` |
| GET    | `/api/hello/?name=Ada` | `{"message": "Hello, Ada!", ...}`           |

## Run locally

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate     Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py test --verbosity 2
python manage.py runserver        # then open http://127.0.0.1:8000/api/hello/
```

## Pipeline

```
push to main ──► Setup ──► Dependencies ──► Test ──► Deploy
```

| Stage        | What it does                                                    |
|--------------|-----------------------------------------------------------------|
| Setup        | Checks out the code and installs Python                         |
| Dependencies | Installs `requirements.txt`, runs `pip check`                   |
| Test         | Runs `manage.py check` and the full test suite                  |
| Deploy       | Runs only on `main` and only after Test succeeds (`needs: test`)|

Pull requests into `main` run Setup, Dependencies and Test; Deploy is skipped.
The `main` branch is protected by a ruleset: changes arrive through a pull
request from a feature branch and the Test check must pass before merging.

## Deployment

The Deploy stage prints the deployment details. If the repository secret
`RENDER_DEPLOY_HOOK_URL` and the variable `APP_URL` are set, it also triggers a
real deploy on Render (configured in `render.yaml`) and smoke-tests
`/api/health/` on the live app.
