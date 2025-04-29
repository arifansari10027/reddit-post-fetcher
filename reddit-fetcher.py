import os
import praw
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get variables from .env
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def fetch_latest_posts(subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"\n🔍 Fetching posts from r/{subreddit_name}...\n")

        for post in subreddit.new(limit=5):
            print("📌 Title:", post.title)
            print("👤 Author:", post.author)
            print("👍 Upvotes:", post.score)
            print("-" * 40)

    except Exception as e:
        print("❌ Something went wrong:", e)

# Run the function
fetch_latest_posts("python")  # You can change "python" to any subreddit
