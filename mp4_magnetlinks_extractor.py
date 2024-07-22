#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_cookies(url):
    test_url = url

    # 启动 Chrome 浏览器
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)

    # 访问目标网站
    driver.get(test_url)

    # 获取浏览器中的所有 cookies
    cookies = driver.get_cookies()
    return cookies

def get_magnet_links(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
  #      ,'Cookie': cookie
    }
    # 创建一个 requests 的 Session 对象
    session = requests.Session()

    # 将 Selenium 获取的 cookies 添加到 requests 的 Session 中
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
        
