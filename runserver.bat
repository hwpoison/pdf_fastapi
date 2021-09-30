@echo off
uvicorn app:app --reload  --reload-exclude *.pdf --host 0.0.0.0
pause