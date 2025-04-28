# Copyright (C) 2023 Authors of the MCDA project - All Rights Reserved

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

# create application
app = FastAPI()

# configure cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def hello():
    logging.info("/hello endpoint called")
    return {"message": "Test"}

if __name__ == '__main__':
    # start application
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
