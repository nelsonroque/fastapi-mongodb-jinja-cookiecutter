source venv/bin/activate;
find . -name '__pycache__' -type d -exec rm -rf {} +
python3 -m main
open http://0.0.0.0:8000/