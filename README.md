# gogoanime-batch-downloader
A python script to download anime episodes in any quality from Gogoanime.
```diff
- NOTE: Due to certain changes in GogoAnime some links may need Captcha verification and thus won't work with this script. To bypass this make sure to use "HDP" quality only.
```
# Installation
Download the zip and extract it to a folder. Open a command prompt in that folder and and then `pip install -r requirements.txt` then `python gogo_downloader.py`.

# Usage
Enter the URL of the 1st episode of the anime you want to download then enter the starting episode number and ending episode number.
Then mention the quality which you want, if the mentioned quality is not found a lower quality will be selected.
If you want to download the video files enter 1 or if you only want the links of the videos enter 2.
The latter option is if you want to use another program such as IDM to download the videos (a .txt file will be generated).
You also need to mention an output file name and folder path.

# Example - Downloading video
<img src="https://i.imgur.com/aXcMJsL.png" width="1000" title="terminal output">

## Gives the output as
<img src="https://i.imgur.com/YrMO1wv.png" width="700" title="file output">

# Example - Saving Links
<img src="https://i.imgur.com/52hNqnE.png" width="1000" title="terminal output">

## Gives the output as
<img src="https://i.imgur.com/X3oTgRf.png" width="700" title="file output">

## Disclaimer
This repo/project was written as an educational intro to web-scraping and network analysis. It is provided publicly as a an open source project for nothing other than educational purposes. I do not take responsibility for how you use this software nor do I recommend you use it in any way that may infringe on any business.

## Legal Warning
This application is not endorsed or affiliated with any anime stream provider. The usage of this application enables episodes to be downloaded for offline convenience which may be forbidden by law in your country. Usage of this application may also cause a violation of the agreed Terms of Service between you and the stream provider. This tool is not responsible for your actions; please make an informed decision prior to using this application. Usage of third party programs and/or libraries may be forbidden in your country without proper consent of the copyright holder.
