from fastapi import FastAPI
# import uvicorn


app=FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to the fast api",
        "status":"Healthy"
    }



# if __name__=="__main__":
#     uvicorn.run("main:app",host="127.0.0.1",port="8080",reload=True)

