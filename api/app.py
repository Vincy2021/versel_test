from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from datetime import datetime

# 创建 FastAPI 应用实例
app = FastAPI(title="Vercel FastAPI 测试", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI on Vercel!",
        "timestamp": datetime.now().isoformat(),
        "status": "running"
    }

@app.get("/info")
def get_info():
    return {
        "app": "FastAPI on Vercel",
        "version": "1.0.0",
        "python_version": "3.10",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/echo")
def echo_data(data: dict):
    return {
        "message": "Data received successfully",
        "received_data": data,
        "timestamp": datetime.now().isoformat()
    }

# Vercel 需要一个 handler 函数
from mangum import Adapter
handler = Adapter(app) 