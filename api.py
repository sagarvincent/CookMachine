# import libraries
from fastapi import FastAPI, HTTPException, Depends
from mysql.connector import connect, Error

app = FastAPI()

# Global variable to store database configuration
db_info = None

# Dependency to get the database connection
def get_db():
    try:
        connection = None
        connection = connect(**db_info)
        yield connection
    finally:
        if connection:
            connection.close()

# Function to establish connection to server and database
@app.post("/db_config")
async def set_db_config(db_config: dict):
    global db_info
    db_info = db_config
    return {"message": "Database configuration set successfully"}

# Example endpoint to query data from the database
@app.get("/get_data")
async def get_data(db: str = Depends(get_db)):
    print("here")
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM recipes;")
        result = cursor.fetchall()
        return {"data": result}
    except Error as e:
        error_message = f"Database error: {e}"
        #print(error_message)
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)








































