from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - text-color-editor--coll-6dac587277b14e25b81ba64b79c8df28',debug=False,docs_url='/confident-gopal-844d6cf09c1611ef92d60242c0a8900393/docs',openapi_url='/confident-gopal-844d6cf09c1611ef92d60242c0a8900393/openapi.json')

app.include_router(router, prefix='/confident-gopal-844d6cf09c1611ef92d60242c0a8900393/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()