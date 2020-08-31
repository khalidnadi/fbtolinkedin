# linkedin-connection-clicker

_This bot uses:_
- [x] Python
- [x] Selenium
- [x] pynput
- [x] selenium.common.exceptions

The primary use is to import FB contacts to LinkedIn users and is specifically applicable for users with a lot of FB friends. There is no longer a method for automating this process as Linkedin and FB ended collaboration due to a court case.
The second use is to just automate clicking add in order to boost connections.

The first stop is to populate the friends.csv file from FB. This can be done using the following steps: https://www.contactmapping.com/blog/2019/8/12/how-to-export-your-facebook-friends-list-to-google-contacts



## If you want to use this bot to import FB friends (*and you are on Windows*), follow these easy steps!
1. Download and extract the zip of the repo into your ``Downloads`` folder.
2. Install Python [***with this installer***](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe) and open perform the following keyboard shortcuts/commands:
- ``Windows Key + R`` and then type ``cmd`` and press ``Enter``
- Type ``cd Downloads/linkedin-connection-clicker-master`` and press ``Enter``
- Type ``pip install pynput selenium wheel`` and press enter
- close the ``cmd`` window
3. Install Firefox from [***here***](https://www.mozilla.org/en-US/firefox/new/) (***or*** skip to step 3, if you already have it)
4. Right-click ``run_connect-clicker.bat`` hover over ``Send To`` and click ``Desktop(create shortcut)``
5. Create a new blank text document called secrets.py in the ``linkedin-connection-clicker`` folder (*the extension **must be .py**)
6. Edit ``secrets.py`` with a text editor, such as ``Notepad`` and insert the following lines, including the single quotes, substituting your information:
- ``email = 'your LinkedIn login email here'``
- ``password = 'your LinkedIn password here'``
(LinkedIn Connection Clicker **does not save your information**)
7. Save and close the text editor.
8. Launch ``run-connect-clicker.bat`` directly or using the shortcut on your desktop
9. When the ``Windows SmartScreen`` window pops up, click ``more info`` and then ``run anyway`` (This is just to protect you in the event that you download a malicious batch file and try to run it. If you don't feel safe, feel free to scan the files with your antivirus software before you override the smart screen warning)
10. Watch the bot do its funciton.
11. If you just want to add friends go to the runbot.py and comment out commenceClicking2 and then uncomment the last 2 functions. 
