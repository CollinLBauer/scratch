import requests
import re
import sys
import os
import time
import random

def get_song(url):
    # get website and find url
    pattern = re.compile("<audio .* src=(.*)></audio>")
    web_content = requests.get(url).content
    matches = pattern.findall(str(web_content))

    if len(matches) < 0:
        print("No matches found! Exiting.")
        return False
    print("Target found:", matches[0])

    # download file
    time.sleep(random.random() * 15 + 5)
    os.system("wget {}".format(matches[0]))
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("2 arguments expected; found {}.".format(len(sys.argv) - 1))
        exit()
    folder = sys.argv[1]
    os.chdir(folder)
    url = sys.argv[2]
    get_song(url)
