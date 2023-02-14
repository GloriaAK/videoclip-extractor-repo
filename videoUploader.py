"""
This script uses the requests library to send a POST request to the URL http://your-website.com/upload with the video
file as a multipart/form-data file.

Note: This is just a basic example to get you started. You'll need to modify the code to handle any additional
parameters, error handling, and response parsing that your website requires.
"""

import requests

url = "http://your-website.com/upload"
video = open("path/to/video.mp4", "rb")

files = {'video': ('video.mp4', video, 'video/mp4')}

response = requests.post(url, files=files)

if response.status_code == 200:
    print("Upload successful")
else:
    print("Upload failed")

video.close()
