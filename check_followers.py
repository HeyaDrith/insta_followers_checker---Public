import json
import os

def load_usernames(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

        # Format 1: List of dicts (followers.json)
        if isinstance(data, list) and 'string_list_data' in data[0]:
            return {entry['string_list_data'][0]['value'] for entry in data}

        # Format 2: Dict with key (following.json)
        elif isinstance(data, dict):
            for key in data:
                entries = data[key]
                if isinstance(entries, list) and 'string_list_data' in entries[0]:
                    return {entry['string_list_data'][0]['value'] for entry in entries}

        raise ValueError(f"Unsupported format in {filename}")


def main():
    print("Instagram Follow Checker\n")

    print("Welcome! This tool will help you see who has sneakily unfollowed you on insta. Just download your data from instagram. This can be done through the app or on a computer. If needed watch a guide video on how to do this.\n")
    print("Once you have your files ready, drag both into the folder! Now with all the files ready and the main script read, you should be able to put ur suspicions to rest!")

    print("When entering name be sure to include .json\n")



    followers_file = input("What is the name of your followers file?: ")
    following_file = input("What is the name of your following file?: ")

    # Check if files exist
    if not os.path.isfile(followers_file) or not os.path.isfile(following_file):
        print("❌ Make sure both 'followers_1.json' and 'following.json' are in the same folder as this script.")
        return

    try:
        followers = load_usernames(followers_file)
        following = load_usernames(following_file)

        not_following_back = sorted(following - followers)
        not_following_you = sorted(followers - following)

        print("\n🔍 Users you follow who don't follow you back:\n")
        for user in not_following_back:
            print(f"- {user}")
        print(f"\nTotal: {len(not_following_back)}")

        print("\n👀 Users who follow you, but you don't follow back:\n")
        for user in not_following_you:
            print(f"- {user}")
        print(f"\nTotal: {len(not_following_you)}")

    except Exception as e:
        print("\n❌ Error reading files:", e)

if __name__ == '__main__':
    main()
