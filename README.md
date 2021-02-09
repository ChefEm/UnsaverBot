# UnsaverBot

## Intagram post unsaver bot built using selenium

This script automates the process of unsaving the saved posts of your instagram account. Just launch the script and it will do your work automatically.

- Note: Your internet speed must not be lacking, otherwise the program will fail to work because program will try to access the elements of the page that might not have been loaded in the browser.
- Note: It will unsave 100 saved posts in one run, you can change it from code to whatever number you want on line 47.

## Requirements

1. Python
2. Selenium python library `pip3 install selenium`
3. tqdm python library `pip3 install tqdm`
4. Use existing or if there is some issue with it, get new version of [chromedriver_win32](https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/) for chrome browser or if you use firefox, get [geckodriver](https://github.com/mozilla/geckodriver/releases)

## This script works with

1. Windows 10
2. Python 3.7.4 or greater

## Getting Started

1. If you are using chrome browser, before running the script comment line 11 and uncomment line 12.