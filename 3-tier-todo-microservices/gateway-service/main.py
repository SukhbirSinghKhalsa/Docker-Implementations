from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="API Gateway")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

TASK_SERVICE_URL = os.getenv("TASK_SERVICE_URL", "http://localhost:8001")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8002")

async def forward_request(method: str, url: str, body: bytes):
    async with httpx.AsyncClient() as client:
        try:
            req = client.build_request(method, url, content=body)
            response = await client.send(req)
            return Response(content=response.content, status_code=response.status_code)
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")

@app.api_route("/api/tasks/{path:path}", methods=["GET", "POST", "DELETE"])
async def route_tasks(path: str, request: Request):
    body = await request.body()
    url = f"{TASK_SERVICE_URL}/tasks/{path}"
    if url.endswith("/"): url = url[:-1]
    return await forward_request(request.method, url, body)

@app.api_route("/api/users/{path:path}", methods=["GET", "POST"])
async def route_users(path: str, request: Request):
    body = await request.body()
    url = f"{USER_SERVICE_URL}/users/{path}"
    if url.endswith("/"): url = url[:-1]
    return await forward_request(request.method, url, body)
