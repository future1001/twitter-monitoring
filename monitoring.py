import tweepy
import telegram
import time
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Twitter API凭证
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Telegram Bot凭证
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 初始化Twitter客户端
twitter_client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

# 初始化Telegram Bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# 要监控的Twitter用户列表
USERS_TO_MONITOR = ['elonmusk', 'cz_binance', 'SBF_FTX']

def get_user_id(username):
    try:
        user = twitter_client.get_user(username=username)
        return user.data.id
    except Exception as e:
        print(f"获取用户ID时出错 {username}: {e}")
        return None

def get_latest_tweets(user_id):
    try:
        tweets = twitter_client.get_users_tweets(id=user_id, max_results=5)
        return tweets.data[0] if tweets.data else None
    except Exception as e:
        print(f"获取推文时出错，用户ID {user_id}: {e}")
        return None

def send_telegram_message(message):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except telegram.error.TelegramError as e:
        print(f"发送Telegram消息时出错: {e}")

def main():
    user_ids = {user: get_user_id(user) for user in USERS_TO_MONITOR}
    last_tweet_ids = {user: None for user in USERS_TO_MONITOR}

    while True:
        for user, user_id in user_ids.items():
            if user_id:
                latest_tweet = get_latest_tweets(user_id)
                if latest_tweet and latest_tweet.id != last_tweet_ids[user]:
                    message = f"新推文来自 @{user}:\n{latest_tweet.text}"
                    send_telegram_message(message)
                    last_tweet_ids[user] = latest_tweet.id

        time.sleep(300)  # 每5分钟检查一次

if __name__ == "__main__":
    main()