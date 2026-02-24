# 清除上下文插件 (clear_context)

AstrBot 插件，用于清除模型上下文、管理会话状态

## 📋 功能特性

- ✅ **清除模型上下文**：通过指令快速清除当前会话的模型上下文
- 📊 **查看上下文信息**：显示当前上下文的长度和内容
- 📖 **详细帮助信息**：提供完整的指令列表和使用说明
- 🎨 **美观的 Markdown 消息**：使用 Markdown 格式输出信息，界面更加美观
- 🛡️ **完善的错误处理**：提高插件的稳定性和可靠性

## 🚀 安装方法

1. 将插件目录 `plugin_upload_clear_context` 复制到 AstrBot 的插件目录中
2. 重启 AstrBot 服务
3. 插件将自动加载并生效

## 💡 使用说明

### 指令列表

| 指令 | 功能 |
|------|------|
| `/clear` | 清除当前模型上下文 |
| `/context` | 查看当前上下文信息 |
| `/clear_help` | 显示插件帮助信息 |

### 示例

1. **清除上下文**：
   ```
   /clear
   ```
   响应：
   ```
   ✅ 上下文已成功清除
   ```

2. **查看上下文**：
   ```
   /context
   ```
   响应：
   ```markdown
   ## 当前上下文信息

   ### 上下文长度
   1234 字符

   ### 上下文内容
   ```
   [上下文内容预览]...
   ```
   ```

3. **查看帮助**：
   ```
   /clear_help
   ```
   响应：
   ```markdown
   ## 清除上下文插件帮助

   ### 指令列表
   - `/clear` - 清除当前模型上下文
   - `/context` - 查看当前上下文信息
   - `/clear_help` - 显示此帮助信息

   ### 功能说明
   此插件用于管理模型上下文，可帮助解决上下文过长导致的问题，提高模型响应质量。
   ```

## 📁 插件结构

```
plugin_upload_clear_context/
├── main.py          # 插件主要代码
├── metadata.yaml    # 插件元数据
├── README.md        # 插件说明文档
├── LICENSE          # 许可证文件
└── .gitignore       # Git 忽略文件
```

## 🔧 技术实现

- **基于 AstrBot 插件架构**：使用 AstrBot 提供的插件 API 开发
- **异步编程**：使用 Python 异步特性，提高性能
- **错误处理**：完善的异常捕获和处理机制
- **Markdown 支持**：使用 Markdown 格式输出消息，提升用户体验

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个插件！

## 📄 许可证

本插件采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🔗 相关链接

- [AstrBot 官方仓库](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot 插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)
