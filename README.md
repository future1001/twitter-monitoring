# Twitter 监控机器人

这个项目是一个 Python 脚本，用于监控特定 Twitter 用户的最新推文，并通过 Telegram 机器人发送通知。

## 功能

- 监控指定的 Twitter 用户的最新推文
- 当检测到新推文时，通过 Telegram 发送通知
- 使用 Twitter API v2 和 Telegram Bot API
- 定期检查更新（默认每5分钟）

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/你的用户名/twitter-monitoring.git
   cd twitter-monitoring
   ```

2. 安装所需的依赖：
   ```
   pip install -r requirements.txt
   ```

3. 复制 `.env.example` 文件并重命名为 `.env`：
   ```
   cp .env.example .env
   ```

4. 在 `.env` 文件中填入您的 Twitter API 和 Telegram Bot 凭证。

## 配置

在 `monitoring.py` 文件中，您可以修改 `USERS_TO_MONITOR` 列表来指定要监控的 Twitter 用户。

## 使用

运行脚本：
