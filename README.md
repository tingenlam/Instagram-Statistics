# Instagram-Statistics
A program for anyone curious about a user's Instagram statistics.

Instructions:
1. Run 'pip install -r requirements.txt'
2. Edit credentials (username, password) in instagram.py
3. Edit target_username in instagram.py
4. Run instagram.py

This program allows you to check:
1. List of users who the target_username follows but are not following back.
2. List of users who follows the target_username but the target_username does not follow back.
3. [Open to suggestions on how you think I can expand this program.]

Do note that:
- Use a throwaway account to avoid suspension as Instagram tracks suspicious log in activity.
- The logged in account cannot have 2FA activated as the program cannot bypass 2FA.
- In order to search up users, the target_username must either be a public profile, or the logged in account must be following the target_username.
- If you encounter a 'ClientChallengeRequiredError' error, just log in via the app once for verification.
