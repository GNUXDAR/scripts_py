# Fast API
[FastAPI](https://fastapi.tiangolo.com/)  

# env
$ cd my-project  
$ python3 -m venv .venv  
$ . .venv/bin/activate ó source .venv/bin/activate  

# Install
$ pip install fastapi  
$ pip install uvicorn  

# Export Requirements  
$ pip freeze > requirements.txt  
$ pip install -r requirements.txt  

# Run
$ uvicorn main:app --reload  
open in browser: http://127.0.0.1:8000  
 http://127.0.0.1:8000/items/5?q=somequery  

# Docs of API
http://127.0.0.1:8000/docs  
http://127.0.0.1:8000/redoc  