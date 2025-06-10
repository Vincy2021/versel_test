# Vercel Python 项目基础测试

## 项目简介
这是一个 Vercel Python 无服务器函数部署测试项目，包含基础 Python 函数和 FastAPI 应用示例。使用自定义路由配置，让 FastAPI 应用可以直接通过根路径访问。

## 项目结构
```
velcel项目部署测试/
├── api/
│   ├── hello.py          # 基础 Python API 函数
│   └── app.py           # FastAPI 应用
├── Pipfile              # Python 环境配置
├── requirements.txt      # Python 依赖（主要依赖文件）
├── vercel.json          # Vercel 路由配置
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 功能
- 基础的 Python HTTP 函数
- FastAPI 应用框架，支持根路径直接访问
- 返回 JSON 格式响应  
- Vercel 自动检测 Python 3.10 环境
- RESTful API 设计
- 自定义路由配置

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
# GET 请求
curl https://your-project.vercel.app/api/hello
# 返回: Hello from Python on Vercel!
```

### 🔄 传统路径访问（仍然有效）
```bash
# FastAPI 应用也可以通过 /api/ 路径访问
curl https://your-project.vercel.app/api/app
curl https://your-project.vercel.app/api/app/info
curl https://your-project.vercel.app/api/app/health
```

## 配置文件说明

### requirements.txt（主要依赖）
```txt
fastapi==0.104.1
uvicorn==0.24.0
mangum==0.16.0
```

### vercel.json 路由配置
```json
{
  "routes": [
    { "src": "/", "dest": "api/app.py" },
    { "src": "/api/(.*)", "dest": "api/$1.py" }
  ]
}
```

**路由规则说明：**
- `"/" → "api/app.py"` - 根路径直接访问 FastAPI 应用
- `"/api/(.*)" → "api/$1.py"` - `/api/` 路径按文件名路由

### Pipfile 依赖管理（备用）
```toml
[requires]
python_version = "3.10"

[packages]
fastapi = "*"
uvicorn = "*"
mangum = "*"
```

## 依赖说明
- `fastapi==0.104.1`: 现代 Python Web 框架
- `uvicorn==0.24.0`: ASGI 服务器
- `mangum==0.16.0`: FastAPI 的 Serverless 适配器

## 关键代码说明

### FastAPI + Mangum 集成
```python
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

# 重要：使用 Mangum 而不是 Adapter
handler = Mangum(app)
```

## 访问方式对比

| 端点类型 | 根路径访问 | 传统路径访问 |
|---------|-----------|-------------|
| FastAPI 主页 | `https://your-app.vercel.app/` | `https://your-app.vercel.app/api/app` |
| FastAPI 信息 | `https://your-app.vercel.app/info` | `https://your-app.vercel.app/api/app/info` |
| 基础函数 | ❌ 不适用 | `https://your-app.vercel.app/api/hello` |

## 工作原理
- Vercel 自动检测到 `requirements.txt` 和 `Pipfile` 使用 Python 运行时
- `requirements.txt` 确保 FastAPI 相关依赖正确安装
- `vercel.json` 自定义路由规则，让 FastAPI 可以根路径访问
- `Mangum` 将 FastAPI 应用适配为 Serverless Functions

## 🎯 推荐测试流程
1. 访问 `https://your-project.vercel.app/` 验证 FastAPI 主页
2. 访问 `https://your-project.vercel.app/health` 检查应用状态
3. 访问 `https://your-project.vercel.app/api/hello` 验证基础函数
4. 使用 POST 请求测试 `https://your-project.vercel.app/echo` 端点

## 🐛 故障排除
- **mangum 导入错误**: 新版本使用 `from mangum import Mangum` 而不是 `Adapter`
- **依赖安装**: 确保 `requirements.txt` 包含正确版本的依赖
- **构建警告**: 已通过简化 `vercel.json` 配置解决
- **版本兼容**: 使用稳定版本 mangum==0.16.0 避免 API 变更问题

现在您的 FastAPI 应用应该能够正确运行了！ 🚀 