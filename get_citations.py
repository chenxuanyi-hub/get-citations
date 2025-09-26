import time
import random
import json
import re
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fetch_paper import fetch 

profile_args = [
    "--disable-blink-features=AutomationControlled",
    "--start-maximized",
    "--disable-infobars",
    "--log-level=3"
    ]

chrome_options = webdriver.ChromeOptions()
 
for a in profile_args:
    chrome_options.add_argument(a)

def start_driver(proxy = None):
    #启动 ChromeDriver 并返回 driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    if proxy:
        chrome_options.add_argument(f"--proxy-server={proxy}")
    return driver

def captcha(driver):
    """
    如果 Google 要求人机验证，手动完成后按回车继续。
    这里做简单检测：若页面中含有常见 captcha 文本，提示手动处理。
    """
    page = driver.page_source
    if "sorry, we can't verify that you're not a robot" in page.lower():
        print("\n Google Scholar 要求人机验证 (CAPTCHA)。")
        print("请在打开的 Chrome 窗口中手动完成验证")
        time.sleep(random.uniform(4.0, 6.0)) # 给浏览器一点时间刷新会话

def get_citations(html):
    #用 BeautifulSoup 从第一个搜索结果中提取引用数（Cited by / 被引用次数）
    soup = BeautifulSoup(html, "lxml")
    first = soup.find("div", class_="gs_ri")
    if not first:
        return None
    # 在第一个结果块中查找所有链接文本，挑出含 Cited by 的
    for a in first.find_all("a"):
        txt = a.get_text(strip=True)
        if re.search(r"Cited by", txt):
            m = re.search(r"(\d+)", txt)
            if m:
                return int(m.group())

    return None

def get_citations_selenium(driver, title, lang="en"):
    #在当前 driver 会话中查询单个 title 并返回引用数或 None
    q = title.replace(" ", "+")
    url = f"https://scholar.google.com/scholar?q={q}&hl={lang}"
    driver.get(url)
    time.sleep(random.uniform(2.0, 4.0))  # 等待页面初步加载

    # 若页面提示人机验证，暂停并提示人工操作
    captcha(driver)

    start_time = time.time()           # 记录开始时间
    max_wait = 60                     
    while True:
        time.sleep(random.uniform(4.0, 7.0))                  
        html = driver.page_source
        if "sorry, we can't verify that you're not a robot" in html.lower():
            print("检测到 CAPTCHA，请手动完成验证。")  
        else:
            break                       # CAPTCHA 已消失，继续
        if time.time() - start_time > max_wait:
            print("等待时间过长，跳过该条目（返回 None）。")
            return None
    cites = get_citations(html)
    return cites



if __name__ == "__main__":
    url = 'https://sigir2025.dei.unipd.it/accepted-papers.html' 
    papers = fetch(url) 

    driver = start_driver(proxy = 'http://127.0.0.1:7897')
    citations = {}

    try:
        for idx, title in enumerate(papers, 1):
            print(f"\n[{idx}/{len(papers)}] 查询：{title}")
            cites = get_citations_selenium(driver, title, lang="en")
            citations[title] = cites
            print(f"→ {title} → 引用数: {cites}")

            # 随机等待，模拟人类行为
            wait_secs = random.uniform(10.0, 20.0)
            print(f"等待 {wait_secs:.1f}s 后继续...")
            time.sleep(wait_secs)

    finally:
        with open("citations_selenium.json", "w", encoding="utf-8") as f:
            json.dump(citations, f, ensure_ascii=False, indent=2)
        driver.quit()
        print("\n已保存 citations_selenium.json，浏览器已关闭。")
        print("请在终端输入 streamlit run website.py")

