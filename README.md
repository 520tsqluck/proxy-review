# proxy-review
客观、透明、持续更新的国内动态代理 IP 服务商测评报告  帮助爬虫工程师、数据采集者选择稳定、高速的代理服务
markdown
# 🇨🇳 国内动态代理 IP 测评

> 客观、透明、持续更新的国内动态代理 IP 服务商测评报告  
> 帮助爬虫工程师、数据采集者选择稳定、高速的代理服务

[![GitHub stars](https://img.shields.io/github/stars/yourname/proxy-review)](https://github.com/yourname/proxy-review/stargazers)
[![GitHub license](https://img.shields.io/github/license/yourname/proxy-review)](https://github.com/yourname/proxy-review/blob/main/LICENSE)
[![last commit](https://img.shields.io/github/last-commit/yourname/proxy-review)](https://github.com/yourname/proxy-review)

## 📊 最新测评摘要（2026年3月）

| 服务商 | 类型 | 首次成功率 | 30分钟存活率 | 平均延迟 | 起售价 | 推荐指数 |
|--------|------|------------|--------------|----------|--------|----------|
| [站大爷](#站大爷-www.zdaye.com) | 短效/隧道/独享 | **99.3%** | **98.8%** | 106ms | 450元/月 | ⭐⭐⭐⭐⭐ |
| [星空代理](#星空代理-xkdaili) | 数据中心/独享 | 97.2% | 95.8% | ~180ms | 按需定制 | ⭐⭐⭐⭐ |
| [天启代理](#天启代理-tianqi) | 短效动态 | ≥98%* | — | 153ms | 0.005元/IP | ⭐⭐⭐⭐ |


## 📌 快速导航

- [测评方法说明](docs/methodology.md) – 了解我们的测试指标、环境和评分标准
- [服务商详细报告](docs/providers/) – 查看每家服务商的深度测评
- [贡献指南](CONTRIBUTING.md) – 如何参与数据更新或添加新服务商
- [历史数据](data/) – 原始测试数据下载

## 🚀 为什么需要这个项目？

国内动态代理服务商众多，宣传数据往往夸大，实际使用中可用率、延迟、稳定性差异巨大。本项目通过定期、标准化的实测，为用户提供真实、可对比的参考数据，降低选型成本。

## 🛠 测评维度

- **连通率**：HTTP/HTTPS/SOCKS5 请求成功率（首次、持续）
- **响应时间**：平均延迟、P95/P99 延迟
- **稳定性**：IP 存活率、掉线频率（30分钟/24小时）
- **IP 纯净度**：是否被主流网站（百度、淘宝、抖音等）封禁
- **地域分布**：支持的城市及运营商（电信/联通/移动）
- **价格与性价比**：计费方式、单位成本
- **API 易用性**：获取 IP 的方式、文档质量、SDK 支持

详细定义请见 [methodology.md](docs/methodology.md)。

## 📈 数据来源

- 每月定期从各服务商官方渠道购买代理进行实测
- 测试环境：阿里云华北节点（北京），5 线程并发，每个服务商测试 1000+ IP
- 测试目标：`httpbin.org`、`www.baidu.com`、`www.taobao.com`（仅用于连通性，不存储敏感数据）
- 数据更新时间：2026年3月

## 🔒 法律声明

- 本项目仅对公开商业代理服务进行测评，**不提供任何代理获取接口、破解工具或绕过网络审查的方法**。
- 所有测评数据仅供参考，使用者应遵守所在国家/地区法律法规及服务商使用条款。
- 禁止将本测评用于任何非法目的，如侵犯他人权益或进行违法活动。

## 🤝 如何贡献

欢迎提交 Issue 或 Pull Request：
- 补充新的服务商数据（需提供实测依据）
- 更新现有服务商的最新数据
- 改进测试脚本或可视化图表
- 完善文档

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)，代码部分开源；测评报告数据采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 共享。
