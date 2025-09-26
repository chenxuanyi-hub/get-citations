# import requests
# from bs4 import BeautifulSoup
# def fetch(url):
    
#     response = requests.get(url)

#     soup = BeautifulSoup(response.text,'lxml')
#     titles = soup.find_all("span", class_="accepted-paper-title")

#     res = [tag.get_text(strip = True) for tag in titles]
#     return res[:10]
# if __name__ == "__main__":
#     url = "https://sigir2025.dei.unipd.it/accepted-papers.html"  
#     found = fetch(url)
#     for idx, t in enumerate(found, start=1):
#         print(f"{idx}. {t}")
#         if t == 'FairDiverse: A Comprehensive Toolkit for Fairness- and Diversity-aware Information Retrieval':
#             print('这是第{}个'.format(idx))


import requests
from bs4 import BeautifulSoup

def fetch(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }


    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount("https://", adapter)

    try:
        response = session.get(url, headers=headers, timeout=15, verify=True)
        response.raise_for_status()
    except requests.exceptions.SSLError:
        print("SSL 错误，尝试禁用证书验证...")
        response = session.get(url, headers=headers, timeout=15, verify=False)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return []

    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all("span", class_="accepted-paper-title")
    res = [tag.get_text(strip=True) for tag in titles]
    return res

if __name__ == "__main__":
    url = "https://sigir2025.dei.unipd.it/accepted-papers.html"  
    found = fetch(url)
    for idx, t in enumerate(found, start=1):
        print(f"{idx}. {t}")
        if t == 'FairDiverse: A Comprehensive Toolkit for Fairness- and Diversity-aware Information Retrieval':
            print('这是第{}个'.format(idx))
