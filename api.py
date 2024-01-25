# import libraries
from fastapi import FastAPI, HTTPException


app = FastAPI()
db_info = None


# function to establish connection to server and database
@app.get("/db_config")
async def db_info(db_config):

    db_info = db_config

# function to close connection to database


# get data function


# insert data function


# delete data


# 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)





































