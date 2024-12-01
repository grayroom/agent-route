import time

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from lc import llm_with_tools
from sr import rl

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/route")
async def get_route(query: str = Query(...)):
    begin = time.time()
    ret = rl(query).__repr__()
    time_taken = f"Time taken: {time.time() - begin}"

    return {"response": ret, "time_taken": time_taken}


@app.get("/chain")
def invoke_chain(
        query: str = Query(...),
):
    begin = time.time()
    ret = llm_with_tools.invoke(query)
    time_taken = f"Time taken: {time.time() - begin}"

    return {"response": ret, "time_taken": time_taken}
