# Claude Tool MCP

[English Version](./README_CN.md)

这个项目是一个MCP（Model Control Plane）服务器，允许在其他大模型上使用Claude的技能系统，特别是来自 [anthropics/skills](https://github.com/anthropics/skills/tree/main) 仓库的技能。

## 前提要求

- Python 3.12
- uv 包管理工具

## 使用步骤

### 1. 克隆本仓库

```bash
git clone https://github.com/SimFG/claude-skill-mcp.git
cd claude-skill-mcp
```

### 2. 同步依赖

使用uv工具同步项目依赖：

```bash
uv sync
```

### 3. 克隆Claude Skills仓库

```bash
git clone https://github.com/anthropics/skills.git
```

### 4. 配置MCP服务器

创建或修改MCP配置文件，添加以下内容（请替换`xxx`为实际路径）：

```json
{
  "mcpServers": {
    "claude-skill-mcp": {
      "command": "uv",
      "args": [
        "run",
        "mcp",
        "run",
        "/xxx/claude-skill-mcp/server.py"
      ],
      "env": {
        "CLAUDE_TOOL_PATH": "/xxx/skills",
        "UV_PYTHON": "/xxx/claude-skill-mcp/.venv"
      }
    }
  }
}
```

## 功能说明

该MCP服务器能够：

- 加载Claude Skills仓库中的工具
- 提供工具列表和使用接口
- 允许其他大模型调用Claude风格的工具

## 支持的工具

通过加载anthropics/skills仓库，您可以使用多种工具，包括但不限于：

- 文档处理工具（docx, pdf, pptx, xlsx）
- 创意设计工具
- 开发和技术工具
- 企业通信工具

## 注意事项

- 请确保Python版本为3.12
- 配置路径时请使用绝对路径
- 环境变量`CLAUDE_TOOL_PATH`可以指向多个工具目录，使用逗号分隔
- 环境变量`UV_PYTHON`必须指向项目的虚拟环境目录

## 示例

以下是使用canvas-design工具绘制星河主题图片的示例：

**输入**：
使用canvas-design tool，绘制以星河为主题的图片，输出png

**输出**：
生成的图片如下所示：

![星河主题图片](example/canvas-design/stellar-river.png)