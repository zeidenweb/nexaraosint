import instaloader

def zeidenfonc1(zeidenvar1):
    zeidenvar2 = instaloader.Instaloader()

    try:
        zeidenvar3 = instaloader.Profile.from_username(zeidenvar2.context, zeidenvar1)

        with open(f"{zeidenvar1}_info.txt", "w", encoding="utf-8") as zeidenvar4:
            zeidenvar4.write(f"Profile: {zeidenvar1}\n")
            zeidenvar4.write(f"Full Name: {zeidenvar3.full_name}\n")
            zeidenvar4.write(f"Instagram ID: {zeidenvar3.userid}\n")
            zeidenvar4.write(f"Bio: {zeidenvar3.biography}\n")
            zeidenvar4.write(f"External URL: {zeidenvar3.external_url}\n")
            zeidenvar4.write(f"Followers: {zeidenvar3.followers}\n")
            zeidenvar4.write(f"Following: {zeidenvar3.followees}\n")
            zeidenvar4.write(f"Posts: {zeidenvar3.mediacount}\n")
            zeidenvar4.write(f"Private Account: {zeidenvar3.is_private}\n")
            zeidenvar4.write(f"Verified Account: {zeidenvar3.is_verified}\n")
            zeidenvar4.write(f"Profile Picture URL: {zeidenvar3.profile_pic_url}\n\n")

            if zeidenvar3.is_private:
                zeidenvar4.write("This is a private account. Only limited information is available.\n")
                print(f"The profile {zeidenvar1} is private. Limited information has been saved.")
            else:
                zeidenvar4.write("\nPosts:\n")
                for zeidenvar5 in zeidenvar3.get_posts():
                    zeidenvar4.write(f"Post ID: {zeidenvar5.mediaid}\n")
                    zeidenvar4.write(f"Caption: {zeidenvar5.caption}\n")
                    zeidenvar4.write(f"Hashtags: {', '.join(zeidenvar5.caption_hashtags)}\n")
                    zeidenvar4.write(f"URL: {zeidenvar5.url}\n")
                    zeidenvar4.write(f"Likes: {zeidenvar5.likes}\n")
                    zeidenvar4.write(f"Comments: {zeidenvar5.comments}\n")
                    zeidenvar4.write(f"Posted on: {zeidenvar5.date_utc}\n")
                    zeidenvar4.write("\n")

        print(f"Data for {zeidenvar1} has been saved to {zeidenvar1}_info.txt.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {zeidenvar1} does not exist.")
    except instaloader.exceptions.ConnectionException as zeidenvar6:
        print(f"Connection error: {zeidenvar6}")
    except Exception as zeidenvar7:
        print(f"An error occurred: {zeidenvar7}")

def zeidenfonc2():
    zeidenvar8 = input("Enter the Instagram username: ")
    zeidenfonc1(zeidenvar8)

if __name__ == "__main__":
    zeidenfonc2()
