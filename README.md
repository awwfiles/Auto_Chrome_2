# Auto_Chrome
 A cross platform pyhton IDE implimenting selenium 4


### This is an open-source project. 
If you want to support this project or me, please check out my NFTs and maybe buy some, i accept most bids.
https://opensea.io/collection/cryptoverse1
or Donate below:
https://paypal.me/CloudMaking?locale.x=en_GB

---
### Video instructions and Demo (updated video coming soon - subscribe to Youtube)
-----> https://youtu.be/510XSoaZ0LI <-----


### Requirements
1. Python3 and pip
2. Chrome browser v.96+
3. ****for MacOS you might have to manually install the latest version of the chromedriver and place it in the "chromedrivers" folder (additionally you might have to add the chromedriver to your firewall exceptions) read notes below form a MacOS user fo rmore detials****

# INSTRUCTIONS
1. Download and update Python and The Chrome browser (if you don’t have it already)
2. Download and extract the project in your desired location (keep all files and folders that come with the repo in this folder)
3. shift+Rigth click inside project folder and click "open powershell window here" 
4. Pip install requirements.txt by running the following comand (pip install -r requirements.txt) (google how to do this for MAC [in terminal enter] pip install -r {repo path}requirements.txt)
5. Run the script (Auto_Chrome.py) by double clickiing it (for MAC right click and run in python launcher)
6. Open a preset file inside the script (make sure to pick the right preset for you or make your own)
6. fill in the varible for your project uplaod properties, examples are provided (you can save for next time)
7. Press the "Open Browser" button (download and login into the metamask extension and go to your collection on  opensea)
8. Run the script

### PRESET BUILDER COMANDS (normal python code and syntax works)
#### Video tutorial on how ot make your own presets: https://www.youtube.com/watch?v=l3UgWmqL89o&t=1s
#### Find CSS and XPATH codes through the inspect window on chrome
##### all base selenium code also works fine (this just maks it so you dont need to setup anything)
1. go_to(adress)
2. css_and_key(code, key)
3. xpath_and_key(code, key)
4. css_and_click(code)
5. xpath_and_click(code)
6. linktext_click(text)
7. linktext_key(text, key) [havnt tested this yet]

#### Must watch video for understanding selenum and making your own automation bots : https://www.youtube.com/watch?v=tRNwTXeJ75U

# Important Notes please read before starting: 
1. Do not move anything in or out of the main script folder.
2. (here is a link to a handy script which does that for you: https://github.com/FireMarshmallow/Easy-file-renamer)
3. as far as know this only works with windows and MAC os
4. you might get a confirmation sign request form metamask on the first uplaod, you can manually click it and the script will carry on, if you click and press "start" again
5. if you get a  [TypeError: can only concatenate str (not "re.Pattern") to str] on launch , use th escript without the syntax highlighting.
6. if you get [chromedriver permission error] on macOS please manually download and place the chromedriver in the chromedrivers folder (delete the other chromedrivers in that folder) found here https://chromedriver.chromium.org/downloads (download the lastest version for MacOS)
---

# Message for a MacOS user
You might need to remove the quarantine attribute from the chromedriver, I did this by issuing the following command in the Terminal: 
xattr -r -d com.apple.quarantine ~/Downloads/Auto_Chrome_2-main/chromedrivers/chromedriver

You might also need to add the chromedriver to the mac Firewall exception list like so:

System Preferences > Security & Privacy > (Unlock the padlock if necessary) Firewall options > click on the + icon and locate the chromedriver

---

If you have any questions or want to get in contact you can find me on instagram and twitter by searching @cloudmaking (feel free to DM).
