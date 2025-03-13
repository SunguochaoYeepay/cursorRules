# Cursor 项目配置模板

这是一个用于快速初始化和配置项目的 Cursor IDE 配置模板。它提供了一套完整的前后端项目配置规则和初始化工具。

## 🌟 特性

- 📦 完整的项目配置模板
- 🚀 快速项目初始化工具
- 🛠 可定制的构建规则
- 🔒 内置安全配置
- 📊 性能优化指南
- 🔄 自动化工作流

## 📁 目录结构

```
.cursor/
├── config/              # 全局配置
│   └── settings.toml    # IDE 设置
├── rules/               # 项目规则
│   ├── frontend/        # 前端规则
│   │   └── vue.rules.toml
│   ├── backend/         # 后端规则
│   │   └── python.rules.toml
│   └── common/          # 通用规则
│       ├── security.rules.toml
│       └── style.rules.toml
├── templates/           # 项目模板
│   ├── frontend/        # 前端模板
│   ├── backend/         # 后端模板
│   └── common/         # 通用模板
├── scripts/            # 工具脚本
│   └── init.py        # 初始化脚本
└── README.md          # 说明文档
```

## 🚀 快速开始

### 初始化新项目

1. **全栈项目（Vue + FastAPI + MySQL + Ant Design）**
   ```bash
   python .cursor/scripts/init.py /path/to/your/project
   ```

2. **前端项目**
   ```bash
   python .cursor/scripts/init.py /path/to/your/project --type frontend
   ```

3. **后端项目**
   ```bash
   python .cursor/scripts/init.py /path/to/your/project --type backend
   ```

### 自定义选项

- 不使用 MySQL：`--no-mysql`
- 不使用 Ant Design：`--no-ant`

示例：
```bash
# 创建不使用 MySQL 的后端项目
python .cursor/scripts/init.py /path/to/your/project --type backend --no-mysql

# 创建不使用 Ant Design 的前端项目
python .cursor/scripts/init.py /path/to/your/project --type frontend --no-ant
```

## 📋 配置说明

### 前端配置 (Vue.js)

- 技术栈：Vue 3 + TypeScript + Vite
- UI 框架：Ant Design Vue
- 状态管理：Pinia
- 路由：Vue Router
- 开发端口：8080

### 后端配置 (Python)

- 框架：FastAPI
- 数据库：MySQL (可选)
- ORM：SQLAlchemy
- 开发端口：3000
- 文档：Swagger UI (/docs)

### 通用配置

- 代码风格
- 安全规则
- Git 工作流
- 性能优化
- 测试规范

## 🔧 开发环境

### 前端要求

- Node.js >= 16
- pnpm >= 8
- TypeScript >= 5.0

### 后端要求

- Python >= 3.9
- pip >= 22.0
- virtualenv 或 venv

## 📚 使用指南

### 前端开发

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建生产版本
pnpm build

# 运行测试
pnpm test
```

### 后端开发

```bash
# 创建虚拟环境
python -m venv venv

# 激活环境
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate   # Windows

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
uvicorn main:app --reload --port 3000
```

## 🔐 安全配置

- CORS 策略
- CSP 设置
- 数据库安全
- API 认证
- 敏感信息处理

## 🔄 自动化功能

- 热重载
- 代码格式化
- 类型检查
- 依赖更新
- 测试自动化

## 📈 性能优化

- 代码分割
- 懒加载
- 缓存策略
- 图片优化
- 打包优化

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 发起 Pull Request

## 📝 版本历史

- v1.0.0 (2024-03-21)
  - 初始版本发布
  - 支持 Vue.js 和 FastAPI
  - 添加项目初始化工具

## 📄 许可证

MIT License

## 🙋‍♂️ 常见问题

### Q: 如何更新配置模板？
A: 直接编辑 `.cursor/rules/` 目录下的相应 .toml 文件。

### Q: 如何添加新的项目类型？
A: 在 `.cursor/rules/` 和 `.cursor/templates/` 中添加新的配置文件，并更新 init.py。

### Q: 如何自定义构建配置？
A: 修改相应的 rules.toml 文件中的 [build] 部分。

## 🔗 相关链接

- [Vue.js 文档](https://vuejs.org/)
- [Ant Design Vue 文档](https://antdv.com/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/)

cursorRules/
├── .cursor/
│   ├── config/              # 全局配置
│   ├── rules/               # 项目规则
│   ├── templates/           # 项目模板
│   ├── scripts/             # 工具脚本
│   └── README.md           # 使用文档
└── .gitignore              # Git 忽略文件 
