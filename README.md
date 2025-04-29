# Reddit API Task – Social Media Automation Engineer Test

## Description
This Python script connects to Reddit using the PRAW (Python Reddit API Wrapper) library and fetches the **5 latest posts** from the **r/Python** subreddit.

Each post's **title**, **author**, and **upvote count** is printed to the console.

---

## Setup Instructions

### 1. Clone or Download
Clone this repo or download the ZIP file and extract it.

### 2. Create a Reddit App
- Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
- Click "Create another app"
- Choose `script` as the type
- Fill in a name and `http://localhost:8080` as redirect URI
- Copy the generated `client_id` and `client_secret`

![Screenshot](https://github.com/arifansari10027/reddit-post-fetcher/blob/d136bc36a4f7bb868d5294dd7c0fd659625a615c/reddit-secrets.png)

### 3. Create `.env` File
Inside the project folder, create a `.env` file with:

```
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=script:reddit.fetcher:v1.0 (by /u/your-reddit-username)
```

Replace with your actual credentials.

### 4. Install Dependencies
Install Python packages using pip:

```bash
pip install praw python-dotenv
```

### 5. Run the Script

```bash
python reddit_fetcher.py
```

---

## Output Example

```
🔍 Fetching latest posts from r/Python...

📌 Title: How to build a Telegram bot with Python
👤 Author: py_enthusiast
👍 Upvotes: 841
------------------------------------------------------------
...
```

---

## Author

arif_exe_ (Reddit ID)
