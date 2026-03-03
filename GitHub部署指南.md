# 🚀 GitHub Actions 部署指南

## ✅ 当前配置状态
所有关键配置已完成：
- ✅ DeepSeek API Key：已配置
- ✅ 飞书Webhook：已配置并测试成功
- ✅ 股票列表：已设置为你的测试股票 (002131,300499,600330)
- ✅ GitHub Actions工作流：已存在

## 📋 部署步骤

### 步骤1：推送代码到GitHub
```bash
# 初始化Git仓库（如果还没初始化）
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "初始化配置：添加DeepSeek API和飞书Webhook，设置测试股票列表"

# 添加远程仓库（替换为你的GitHub仓库地址）
git remote add origin https://github.com/你的用户名/daily_stock_analysis.git

# 推送代码
git branch -M main
git push -u origin main
```

### 步骤2：配置GitHub Secrets
在GitHub仓库中设置：
1. 进入仓库 → Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 添加以下Secrets：

| Secret名称 | 值 | 说明 |
|-----------|-----|------|
| `OPENAI_API_KEY` | `sk-d91d1344f8b34b1eb086c334654019d9` | 你的DeepSeek API Key |
| `FEISHU_WEBHOOK_URL` | `https://open.feishu.cn/open-apis/bot/v2/hook/0c3d5407-1ad5-4b06-91e4-74ac985bde01` | 飞书Webhook地址 |
| `STOCK_LIST` | `002131,300499,600330` | 你的股票列表 |
| `OPENAI_BASE_URL` | `https://api.deepseek.com/v1` | DeepSeek API地址 |

### 步骤3：启用GitHub Actions
1. 进入仓库 → Actions
2. 点击 "I understand my workflows, go ahead and enable them"
3. 找到 "每日股票分析" 工作流
4. 点击 "Enable workflow"

### 步骤4：手动触发测试运行
1. 在Actions页面，点击 "每日股票分析"
2. 点击 "Run workflow"
3. 选择运行模式（推荐：full - 完整分析）
4. 点击 "Run workflow"

## ⏰ 自动运行时间
- **默认时间**：每个交易日北京时间18:00自动运行
- **运行频率**：周一到周五（交易日）
- **可调整**：如需其他时间，可编辑 `.github/workflows/daily_analysis.yml`

## 📊 预期输出

### 飞书将收到：
1. **决策仪表盘**：每只股票的买入/观望/卖出建议
2. **详细分析**：技术面、基本面、新闻舆情
3. **买卖点位**：精确的买入价、止损价、目标价
4. **大盘复盘**：市场概况、板块表现

### 示例格式：
```
🎯 2026-03-03 决策仪表盘
共分析3只股票 | 🟢买入:1 🟡观望:1 🔴卖出:1

📊 分析结果摘要
🟢 利欧股份(002131): 买入 | 评分 78 | 看多
🟡 高澜股份(300499): 观望 | 评分 62 | 震荡  
🔴 天通股份(600330): 卖出 | 评分 45 | 看空
```

## 🔧 自定义配置

### 修改股票列表
1. 编辑 `.env` 文件中的 `STOCK_LIST`
2. 或在GitHub Secrets中更新 `STOCK_LIST`

### 调整分析策略
编辑 `.env` 文件：
```bash
# 短线交易推荐策略
AGENT_SKILLS=bull_trend,ma_golden_cross,volume_breakout,shrink_pullback

# 或启用所有策略
AGENT_SKILLS=all
```

### 修改推送设置
```bash
# 报告类型：simple(精简) 或 full(完整)
REPORT_TYPE=full

# 仅推送摘要（不含个股详情）
REPORT_SUMMARY_ONLY=false

# 单股推送模式（每分析完一只立即推送）
SINGLE_STOCK_NOTIFY=false
```

## 🐛 故障排除

### 常见问题：

#### 1. GitHub Actions运行失败
- **检查**：Actions → 具体运行 → 查看日志
- **常见原因**：Secrets配置错误、依赖安装失败
- **解决**：确认Secrets值正确，重新运行

#### 2. 飞书收不到消息
- **检查**：飞书机器人是否启用，Webhook地址是否正确
- **测试**：运行 `test_simple.py` 验证Webhook
- **解决**：重新配置飞书机器人

#### 3. API调用失败
- **检查**：DeepSeek API Key是否有效，额度是否充足
- **测试**：访问 https://platform.deepseek.com 验证API Key
- **解决**：更换API Key或检查网络

#### 4. 数据获取失败
- **检查**：股票代码格式是否正确，市场是否开盘
- **解决**：确认股票代码，尝试更换数据源

## 📈 监控和维护

### 1. 查看运行状态
- GitHub Actions页面：查看每次运行结果
- 飞书消息：确认分析报告正常推送
- 日志文件：GitHub Actions运行日志

### 2. 更新配置
- 修改 `.env` 文件后需要重新推送代码
- 修改GitHub Secrets立即生效

### 3. 扩展功能
- **添加更多股票**：更新 `STOCK_LIST`
- **添加通知渠道**：配置企业微信、Telegram等
- **调整分析频率**：修改GitHub Actions的cron表达式

## 🎯 你的测试股票信息

| 股票代码 | 股票名称 | 市场 | 备注 |
|---------|---------|------|------|
| 002131 | 利欧股份 | 深市 | 中小板 |
| 300499 | 高澜股份 | 深市 | 创业板 |
| 600330 | 天通股份 | 沪市 | 主板 |

## 📞 获取帮助
- 项目文档：`docs/` 目录
- 完整指南：`docs/full-guide.md`
- GitHub Issues：提交问题
- 飞书联系：通过配置的机器人反馈问题

## 🎉 完成部署！
完成以上步骤后，你的股票分析系统将：
1. 每天自动分析指定股票
2. 生成详细的决策报告
3. 推送到飞书方便查看
4. 完全自动化运行，无需人工干预

现在就开始部署吧！