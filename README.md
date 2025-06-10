# Vercel Python 项目基础测试

## 项目简介
这是一个 Vercel Python 无服务器函数部署测试项目，包含基础 Python 函数和 FastAPI 应用示例。

## 项目结构
```
velcel项目部署测试/
├── api/
│   ├── hello.py          # 基础 Python API 函数
│   └── app.py           # FastAPI 应用
├── Pipfile              # Python 环境配置
├── requirements.txt      # Python 依赖（可选，本地开发用）
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 功能
- 基础的 Python HTTP 函数
- FastAPI 应用框架
- 返回 JSON 格式响应  
- Vercel 自动检测 Python 3.10 环境
- RESTful API 设计

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

### 基础 Python 函数
```bash
# GET 请求
curl https://your-project.vercel.app/api/hello
# 返回: Hello from Python on Vercel!
```

### FastAPI 应用
```bash
# 主页
curl https://your-project.vercel.app/api/app
# 返回: {"message": "Hello from FastAPI on Vercel!", ...}

# 应用信息
curl https://your-project.vercel.app/api/app/info
# 返回: {"app": "FastAPI on Vercel", "version": "1.0.0", ...}

# 健康检查
curl https://your-project.vercel.app/api/app/health
# 返回: {"status": "healthy", ...}

# POST 数据测试
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "test", "message": "hello"}' \
  https://your-project.vercel.app/api/app/echo
```

## 依赖说明
- `fastapi`: Web 框架
- `uvicorn`: ASGI 服务器
- `mangum`: FastAPI 的 Serverless 适配器

## 工作原理
- Vercel 检测到 `Pipfile` 自动使用 Python 运行时
- `mangum` 将 FastAPI 应用适配为 Serverless Functions
- 每个 `api/*.py` 文件自动成为独立的端点
- FastAPI 提供自动 API 文档（但在 Serverless 中受限）

现在您可以测试两种不同的 Python 部署方式了！ 