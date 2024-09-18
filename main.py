import uvicorn
from fastapi import FastAPI


app  = FastAPI()


@app.get('/')
def index():
    return {'message': "hello Stranger"}

@app.get('/welcome')
def get_name(name:str):
    return {'my name is ' : f"{ name}"}
 
if __name__ == "__main__":

    uvicorn.run(app,host='127.0.0.1',port=8000)
    #uvicorn main:app --reload

