import streamlit as st
import json
import os

SNAPSHOT_FILE = "data/followers_snapshot.json"

def load_usernames(file_obj):
    data = json.load(file_obj)
    return set(entry['string_list_data'][0]['value'] for entry in data)

def save_snapshot(usernames):
    with open(SNAPSHOT_FILE, 'w') as f:
        json.dump(sorted(list(usernames)), f)

def load_snapshot():
    if not os.path.exists(SNAPSHOT_FILE):
        return set()
    with open(SNAPSHOT_FILE, 'r') as f:
        return set(json.load(f))

st.set_page_config(page_title="Instagram Unfollowers Tracker", layout="wide")

st.title("📉 Instagram Unfollowers Tracker")
st.markdown("Upload your **followers.json** from Instagram's data download to see who unfollowed or followed you since your last check.")

uploaded_file = st.file_uploader("Upload your `followers.json` file", type="json")

if uploaded_file:
    try:
        current_followers = load_usernames(uploaded_file)
        previous_followers = load_snapshot()

        st.success(f"✅ Successfully loaded {len(current_followers)} followers.")

        if not previous_followers:
            save_snapshot(current_followers)
            st.info("📸 No previous snapshot found. Snapshot saved for future comparison.")
        else:
            unfollowers = previous_followers - current_followers
            new_followers = current_followers - previous_followers

            col1, col2 = st.columns(2)

            with col1:
                st.metric("👎 Unfollowers", len(unfollowers))
                if unfollowers:
                    st.text_area("Unfollowers List", "\n".join(sorted(unfollowers)), height=200)

            with col2:
                st.metric("👍 New Followers", len(new_followers))
                if new_followers:
                    st.text_area("New Followers List", "\n".join(sorted(new_followers)), height=200)

            save_snapshot(current_followers)
            st.success("📂 Snapshot updated successfully.")
    except Exception as e:
        st.error(f"Error processing file: {e}")
