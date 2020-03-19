import requests
import re
import os
import sys
import time
import random

from get_song import get_song
from list_missing import list_missing

# creates the remote url from the local version in HTML
def stitch_url(original, tail):
    pattern = re.compile("^(https?://.*\.[a-z]*)")
    head = pattern.findall(original)[0]
    return head+tail

# parses khinsider HTML for song links and passes them to get_song()
def get_all_songs(url, fix_missing=False):
    pattern = re.compile("<td class=\"clickable-row\"><a href=\"(.*)\">(.*)</a></td>")
    web_content = requests.get(url).text
    matches = pattern.findall(str(web_content))

    if len(matches) < 0:
        print("No matches found! Exiting.")
        return False

    # code specific to missing tracks
    fix_counter = 0
    if fix_missing:
        missing = list_missing(os.getcwd())

    if fix_missing:
        print("Getting {} missing tracks.".format(len(missing)))
    else:
        print("{} matches found.".format(len(matches)))
    for match in matches:
        fix_counter += 1
        if fix_missing:
            if fix_counter in missing:
                print("  {} {}".format((match[1] + " -").ljust(32), match[0]))
                get_song(stitch_url(url, match[0]))
        else:
            print("  {} {}".format((match[1] + " -").ljust(32), match[0]))
            get_song(stitch_url(url, match[0]))
    
    print("\nDone.")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("2 arguments expected; found {}.".format(len(sys.argv) - 1))
        exit()
    folder = sys.argv[1]
    try:    # move into desired folder
        os.chdir(folder)
    except: # folder does not exist
        print("Desired folder is not valid.")
        exit()
    url = sys.argv[2]
    if "-fix-missing" in sys.argv:
        get_all_songs(url, fix_missing=True)
    else:
        get_all_songs(url)

