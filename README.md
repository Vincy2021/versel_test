# Vercel Python 项目基础测试

## 项目简介
这是一个最简化的 Vercel Python 无服务器函数部署测试项目，使用 Pipfile 让 Vercel 自动检测 Python 环境。

## 项目结构
```
velcel项目部署测试/
├── api/
│   └── hello.py          # 基础 Python API 函数
├── Pipfile              # Python 环境配置（让 Vercel 自动检测）
├── requirements.txt      # Python 依赖（可选，本地开发用）
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 功能
- 基础的 Python HTTP 函数
- 返回简单的文本响应  
- Vercel 自动检测 Python 3.9 环境
- 最小化配置，无需 vercel.json

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

## 测试
部署后访问 `https://your-project.vercel.app/api/hello` 应该看到：
```
Hello from Python on Vercel!
```

## 命令行测试
```bash
curl https://your-project.vercel.app/api/hello
```

## 工作原理
- Vercel 检测到 `Pipfile` 后会自动使用 Python 运行时
- `python_version = "3.9"` 指定使用 Python 3.9
- 所有 `api/*.py` 文件自动成为 Serverless Functions
- 无需复杂配置，Vercel 自动处理路由

就这么简单！ 