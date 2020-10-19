# /bin/bash

source venv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=main
# flask run
python main.py