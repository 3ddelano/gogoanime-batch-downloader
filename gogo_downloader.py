from bs4 import BeautifulSoup
import sys
from pySmartDL import SmartDL
from requests import get
from os import path

# INPUT VARS
anime_url = "https://www1.gogoanime.ai/aho-girl-episode-1"
start_ep = 1
end_ep = 2
highest_quality = 5
should_download = "1"
output_name = "Aho Girl"
output_folder = "D:\\Downloads\\Video"

# GET INPUTS
# anime_url = input(
#     "Enter the URL of the 1st episode of the anime from GOGOANIME: ")
# start_ep = int(input("Enter the starting epsiode number: "))
# end_ep = int(input("Enter the ending episode number: "))
# print("Enter the highest quality to get (if the mentioned quality is not found the lower quality will be selected)")
# print("1. 240p  2. 360p  3. 480p  4. 720p  5. 1080p  6. HDP")
# highest_quality = int(input("Enter a quality number from 1-6: "))-1
# should_download = input(
#     "Enter 1 if you want to download the episodes or Enter 2 if you want to only save the episode links to a txt file: ")
# output_name = input("Enter the output file name: ")
# output_folder = input("Enter the full path of the output folder: ")

found_error = False
if len(anime_url) < 5:
    print("Error: Invalid URL of 1st episode")
    found_error = True

if highest_quality < 0 or highest_quality > 5:
    print("Error: Invalid quaility mention. Enter only a number from 1-6")
    found_error = True

if len(output_name) < 1:
    print("Error: Invalid output name. Enter at least 2 characters.")
    found_error = True

if not path.isabs(output_folder):
    print("Error: Invalid output path.")
    found_error = True

if found_error == True:
    print("Done")
    sys.exit()

# PRIVATE VARS
anime_base = anime_url[:anime_url.rindex("-")]+"-"
qualities = ["240p", "360p", "480p", "720p",
             "1080p", "GOOGLEAPIS"]

# HELPER FUNCTIONS


def downloadLink(link, filepath):
    obj = SmartDL(link, filepath)
    obj.start()


def getLinks(url, filter):
    links = []

    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_links = soup.find_all("a", href=True)
    for link in all_links:
        if link.has_attr('href'):
            url = link.get("href")
            if filter in url:
                links.append(url)
    return links


# SCRAPING CODE
print("######### GOGOANIME BATCH DOWNLOADER | 3ddelano #########\n")
to_download = []
for ep in range(start_ep, end_ep+1):
    all_download_links = getLinks(anime_base + str(ep), "download")
    if len(all_download_links) == 0:
        print(f"EP {ep} | NOT FOUND")
        continue
    # Get the highest quality available but not exceeding the user's mentioned quality
    found_mp4 = None
    for download_link in all_download_links:
        all_mp4_links = getLinks(download_link, ".mp4")
        req_quality = highest_quality
        while not found_mp4 and req_quality >= 0:
            for mp4 in all_mp4_links:
                if qualities[req_quality].lower() in mp4:
                    found_mp4 = {"link": mp4,
                                 "quality": qualities[req_quality]}
            req_quality -= 1

    if found_mp4:
        print(f"EP {ep} | ({found_mp4['quality']}) | {found_mp4['link']}")
        ep_path = path.normpath(output_folder + "/" +
                                output_name + "_" + str(ep) + ".mp4")
        if should_download == "1":
            downloadLink(found_mp4["link"], ep_path)
        else:
            to_download.append(found_mp4["link"])
    else:
        all_mp4_links = getLinks(all_download_links[0], ".mp4")
        if all_mp4_links and len(all_mp4_links) > 0:
            found_mp4 = {"link": all_mp4_links[0], "quality": "None"}
        else:
            print(f"MP4 NOT FOUND FOR EP {ep}")

if len(to_download) != 0:
    file_path = path.normpath(output_folder + "/" + output_name + ".txt")
    text_file = open(file_path, "w+")
    text_file.write("\n".join(to_download))
    text_file.close()

print("Done")
