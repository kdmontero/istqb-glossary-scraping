# istqb-glossary-scraping
This is a quick one-off web-scraping script to get all the glossary terms and definitions of ISTQB website (as of July 2023)

The default printed view of the glossary contains unnecessary information, so I built this tool that extracts only the terms 
and their definitions. Once copied, users can easily edit and format the content however they prefer.

## Setup
In `istqb_glossary.py`, change the `chromedriver` variable to the file path of your chromedriver
```
chromedriver = r'C:\Users\file\path\to\your\chromedriver_win32\chromedriver.exe'
```
