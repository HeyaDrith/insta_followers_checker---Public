# Instagram Non-Followers Checker

This Python script helps you find out:
- Who **does not follow you back** on Instagram.
- Who **you do not follow back**.

## 🔧 How It Works

The script compares your Instagram **followers** and **following** lists using JSON data files you can download from your Instagram account.

## 📁 Requirements

- Python 3.x
- A code editor like [VSCode](https://code.visualstudio.com/) (recommended)

## 📥 Getting Started

1. **Download your Instagram data** from your account settings:
   - Go to **Settings > Privacy and Security > Data Download** on Instagram.
   - Request your data in **JSON format**.
   - After receiving the email from Instagram, download and unzip the data.

2. **Locate the following files** in your Instagram data folder:
   - `followers.json`
   - `following.json`

3. **Place these two files** in the **same folder** as the Python script.

4. **Run the script** using your terminal or code editor:
   ```bash
   python check_nonfollowers.py
