import importlib
import os
import re

from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index_view(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})
@app.get("/itme/{id}")
async def read_itme(request: Request, id:str):
    return templates.TemplateResponse("item.html", {"request": request, "id":id})

def register_api(app: FastAPI):
    module_names = []
    for file in os.listdir('api'):
        if file in ('__pycache__', 'base.py', '__init__.py','music163'):
            continue
        #python3.8以上
        # .py
        if module_name := re.findall(r'(\w+)\.py', file):
            module_names.append(module_name[0])
        else:
            # package
            module_names.append(file)
        # #python3.8以下
        # module_names.append(re.findall(r'(\w+)\.py', file)[0])

    for module_name in module_names:
        module = importlib.import_module(f'api.{module_name}')
        if hasattr(module, 'ResponseModel') and hasattr(module, 'process'):
            app.post(
                f'/{module_name}',
                response_model=module.ResponseModel,
                description=module.__doc__ or '',
            )(module.process)

register_api(app)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=9000)
