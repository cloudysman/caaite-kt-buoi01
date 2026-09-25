# Dich vu chat

Du an nho cua buoi 1, dung de tap Git va GitHub.

## Cach chay

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Mo http://localhost:8000/health de kiem tra.
