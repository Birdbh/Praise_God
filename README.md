Praise God Our Lord!
This codebase is used to post a video on Instagram and also to create a post on Instagram using Facebook Creator Studio. The codebase uses the following libraries:

instagrapi: This library is used to interact with the Instagram API and perform actions such as logging in and uploading videos.
selenium: This library is used to automate web browsers such as Chrome, Firefox, and Edge. It is used in this codebase to interact with the Facebook Creator Studio website and perform actions such as logging in, creating posts, and uploading videos.
How to use the codebase
Posting on Instagram
Enter your Instagram username and password in the USERNAME and PASSWORD variables respectively.
Run the post() function to upload a video named __temp__.mp4 with the caption "Praise God Our Lord!" and a bunch of hashtags.
Creating a post on Instagram using Facebook Creator Studio
Run the webpost() function, this will open chrome and log you into Facebook Creator Studio and Instagram, wait for few seconds, it will automatically open the window to create a post
Select Reel post and post the video.
Creating a post on Instagram using Facebook Creator Studio v2
Run the webpostv2() function, this will open chrome and log you into Facebook, since it is not implemented so you can add your own logic to it.
Scraping Bible Verse
Run the WebScraper.getquote() function, it will return a random Bible verse from the website https://www.invajy.com/bible-verses/
Note
Make sure that you have the latest version of Chrome and the ChromeDriver installed.
You must have an active Instagram account and a Facebook Creator Studio account to use this codebase.
The webpost() function is only tested on Chrome browser, it might not work on other browsers.
The WebScraper.getquote() function is only scraping from one website if you want to scrape from other website you can change the value of SCRAPE_URL to desired website.
The webpostv2() function is not implemented yet and needs to be implemented as per the requirement.
Additional Note
Be aware that using this codebase to automate Instagram interactions may violate Instagram's terms of service and could result in your account being banned. Use at your own risk.
Always make sure to not include sensitive information like username or password in public codebase.
