# Vercel Python 项目基础测试

## 项目简介
这是一个最简化的 Vercel Python 无服务器函数部署测试项目。

## 项目结构
```
velcel项目部署测试/
├── api/
│   └── hello.py          # 基础 Python API 函数
├── requirements.txt      # Python 依赖（空文件）
├── vercel.json          # Vercel 配置
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 功能
- 基础的 Python HTTP 函数
- 返回简单的文本响应
- 最小化配置

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

就这么简单！ 