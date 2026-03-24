# 贡献指南

感谢您对 `proxy-review` 项目的关注！我们欢迎任何形式的贡献，无论是报告问题、补充数据还是改进文档。

---

## 如何参与

### 1. 报告问题
- 在 [Issues](https://github.com/yourusername/proxy-review/issues) 中提交新问题。
- 请清晰描述问题，并提供相关截图或日志。

### 2. 补充或更新服务商数据
如果您有某服务商的最新实测数据，欢迎提交 Pull Request。

**要求**：
- 数据必须来自实际测试，不可凭空捏造。
- 请按照 `providers/` 目录下已有的格式编写报告。
- 如有原始数据，请一并放入 `data/` 目录。

### 3. 改进测试脚本
- 测试脚本位于 `scripts/test_proxy.py`。
- 可优化性能、增加新功能（如SOCKS5支持）或修复 bug。
- 请确保修改后的脚本在本地能正常运行。

### 4. 完善文档
- 修复错别字、语法错误。
- 补充缺失的说明。
- 翻译成其他语言（可选）。

---

## Pull Request 流程

1. Fork 本仓库。
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开 Pull Request。

我们会尽快审核，并提供反馈。

---

## 数据格式规范

- 原始数据 CSV 文件：包含列 `timestamp`, `proxy`, `target`, `status_code`, `response_time`, `error_msg`。
- 服务商报告 Markdown：使用二级标题 `## 服务商名称`，包含基本介绍、测试结果、优缺点、适用场景等。

---

## 代码风格

- Python 脚本遵循 PEP8。
- Markdown 文件使用标准语法，保持整洁。

---

## 行为准则

请友善、尊重地参与讨论。本项目秉持开源精神，欢迎所有人贡献。
