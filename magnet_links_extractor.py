#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_cookies(url):
    test_url = url

# Create a Chrome webdriver with options for ant-bot detection 
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)

# Access target webpage
    driver.get(test_url)
# Save cookies from the webpage
    cookies = driver.get_cookies()
    return cookies

def get_magnet_links(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    try:
        response = session.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        magnet_links = []
        print=(response.content)
        # Find all <a> tags with href containing 'magnet:'
        for link in soup.find_all('a', href=re.compile(r'magnet:')):
            magnet_links.append(link['href'])

        return magnet_links
    except Exception as e:
        print(f"Error fetching magnet links: {e}")
        return []

if __name__ == "__main__":
    target_url = input("Please paste the btdx link here:")
    cookies=get_cookies(target_url)

    mp4_magnet_links = get_magnet_links(target_url)

    if mp4_magnet_links:
        for link in mp4_magnet_links:
            print(link)
    else:
        print("No MP4 magnet links found on the page.")
        
