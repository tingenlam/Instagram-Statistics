from instagram_private_api import Client
import ssl

# Credentials - Use a throwaway account to avoid risking suspension.
username = ''
password = ''

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

api = Client(username, password)

target_username = 'lamtingen' # User must be public or username must be following target_username.
user_id = api.username_info(target_username)['user']['pk']
print("Account: @",target_username)

# Use pagination to retrieve all results bc 'user_following()' method only returns 100 results.

# Get followers - not v accurate idky
followers_users = []
next_max_id = None

while True:
    followers = api.user_followers(user_id, rank_token=api.generate_uuid(), max_id=next_max_id)
    followers_users.extend([follower['username'] for follower in followers['users']])
    
    if 'next_max_id' not in followers:
        break
    
    next_max_id = followers['next_max_id']

followers_set = set(followers_users)
print("Number of followers: ", len(followers_set))

# Get following - quite accurate but +-1
following_users = []
next_max_id = None

while True:
    following = api.user_following(user_id, rank_token=api.generate_uuid(), max_id=next_max_id)
    following_users.extend([following_user['username'] for following_user in following['users']])
    
    if 'next_max_id' not in following:
        break
    
    next_max_id = following['next_max_id']

following_set = set(following_users)
print("Number of following: ", len(following_set))

# Get unfollowers
unfollowers = following_set - followers_set
print("Unfollowers: ", len(unfollowers))
if len(unfollowers) == 0:
    print('There are no unfollowers. :D')
else:
    for unfollower in unfollowers:
        print(unfollower)

# Get not following
not_following = followers_set - following_set
print("Not following: ", len(not_following))
if len(not_following) == 0:
    print("There are no followers that you don't follow back.")
else:
    for not_following_user in not_following:
        print(not_following_user)
