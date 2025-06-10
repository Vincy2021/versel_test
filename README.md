# Vercel Python 项目基础测试

## 项目简介
这是一个 Vercel Python 无服务器函数部署测试项目，包含基础 Python 函数和 FastAPI 应用示例。FastAPI 应用直接导出为 ASGI 应用，让 Vercel 自动检测和运行。

## 项目结构
```
velcel项目部署测试/
├── api/
│   ├── hello.py          # 基础 Python API 函数
│   └── app.py           # FastAPI 应用（主应用）
├── Pipfile              # Python 环境配置
├── requirements.txt      # Python 依赖
├── vercel.json          # Vercel 路由配置
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 功能
- 基础的 Python HTTP 函数
- FastAPI 应用框架，直接通过根路径访问
- 返回 JSON 格式响应  
- Vercel 自动检测 Python 3.10 环境和 ASGI 应用
- RESTful API 设计
- 简化的路由配置

## 部署步骤

### 1. 安装 Vercel CLI
```bash
npm install -g vercel
```

### 2. 登录 Vercel
```bash
vercel login
```

### 3. 部署项目
```bash
# 在项目根目录运行
vercel
```

### 4. 本地测试
```bash
# 启动本地开发服务器
vercel dev
```

## API 端点测试

### 🌟 FastAPI 应用（根路径访问）
```bash
# 主页 - 直接通过根路径访问
curl https://your-project.vercel.app/
# 返回: {"message": "Hello from FastAPI on Vercel!", ...}

# 应用信息
curl https://your-project.vercel.app/info
# 返回: {"app": "FastAPI on Vercel", "version": "1.0.0", ...}

# 健康检查
curl https://your-project.vercel.app/health
# 返回: {"status": "healthy", ...}

# POST 数据测试
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "test", "message": "hello"}' \
  https://your-project.vercel.app/echo
```

### 📡 基础 Python 函数
```bash
# 基础函数
curl https://your-project.vercel.app/api/hello
# 返回: Hello from Python on Vercel!
```

## 配置文件说明

### requirements.txt（主要依赖）
```txt
fastapi==0.104.1
```

### vercel.json 路由配置（简化版）
```json
{
  "routes": [
    { "src": "/(.*)", "dest": "api/app.py" }
  ]
}
```

**路由规则说明：**
- 所有请求都路由到 `api/app.py`，由 FastAPI 应用处理路由分发
- 基础 Python 函数通过 `/api/hello` 路径访问
- **无需 builds 配置** - Vercel 自动检测 Python 项目

### Pipfile 依赖管理
```toml
[requires]
python_version = "3.10"

[packages]
fastapi = "*"
uvicorn = "*"  # 本地开发用
```

## 依赖说明
- `fastapi==0.104.1`: 现代 Python Web 框架
- `uvicorn`: 本地开发用 ASGI 服务器

## 关键代码说明

### FastAPI 应用（无需 Mangum）
```python
from fastapi import FastAPI
from datetime import datetime

# 直接创建 FastAPI 应用，Vercel 自动检测
app = FastAPI(title="Vercel FastAPI 测试", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

# 注意：不需要 handler = Mangum(app)
```

### 基础 Python 函数
```python
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Hello from Python on Vercel!".encode('utf-8'))
```

## 访问方式

| 端点类型 | URL | 描述 |
|---------|-----|-----|
| FastAPI 主页 | `https://your-app.vercel.app/` | FastAPI 应用根路径 |
| FastAPI 信息 | `https://your-app.vercel.app/info` | 应用信息 |
| FastAPI 健康检查 | `https://your-app.vercel.app/health` | 健康状态 |
| 基础函数 | `https://your-app.vercel.app/api/hello` | 简单文本响应 |

## 工作原理
- Vercel 自动检测 `app` 变量作为 ASGI 应用
- 通过 `requirements.txt` 和 `Pipfile` 自动识别 Python 项目
- 不需要 Mangum 适配器，Vercel 内置 ASGI 支持
- `vercel.json` 只配置路由，无需 builds 配置
- FastAPI 负责内部路由分发

## 🎯 推荐测试流程
1. 访问 `https://your-project.vercel.app/` 验证 FastAPI 主页
2. 访问 `https://your-project.vercel.app/health` 检查应用状态
3. 访问 `https://your-project.vercel.app/info` 查看应用信息
4. 使用 POST 请求测试 `https://your-project.vercel.app/echo` 端点
5. 访问 `https://your-project.vercel.app/api/hello` 测试基础函数

## 🐛 故障排除
- **issubclass 错误**: 已通过删除 `handler = Mangum(app)` 解决
- **builds 警告**: 已通过删除 `builds` 配置解决，让 Vercel 自动检测
- **依赖简化**: 只需要 `fastapi`，Vercel 自动处理 ASGI
- **路由配置**: 所有请求都交给 FastAPI 处理，更简洁
- **ASGI 自动检测**: Vercel 会自动识别 `app` 变量作为 ASGI 应用

现在您的应用应该能够正常运行，且没有任何警告了！ 🚀 