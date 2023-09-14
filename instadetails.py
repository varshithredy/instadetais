import instaloader

# Creating an Instaloader() object
ig = instaloader.Instaloader()

# Taking the Instagram username as input from the user
usrname = input("Enter username:")

# Fetching the details of the provided username using Instaloader object
profile = instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username + " is having " + str(profile.followers) + ' followers.')
print(profile.username + " is following " + str(profile.followees) + ' people')
print("Bio: ", profile.biography)

# Downloading the profile picture of the provided user
ig.download_profile(usrname, profile_pic_only=True)
