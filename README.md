# 获取引用（get-citations）

## 项目简介

本项目用于自动从 Google Scholar 上抓取 SIGIR 会议论文的引用数，并以网页形式展示和搜索。

## 主要功能

- 自动获取 SIGIR 网站上的全部论文列表
- 爬取论文在 Google Scholar 上的引用数(需要认为完成人机验证）
- 可视化展示论文与引用数，支持搜索与一键数据更新

## 文件说明

- [`fetch_paper.py`](https://github.com/chenxuanyi-hub/get-citations/blob/main/fetch_paper.py)  
  获取 SIGIR 论文列表。论文数量可通过修改 return 函数调整。
- [`get_citations.py`](https://github.com/chenxuanyi-hub/get-citations/blob/main/get_citations.py)  
  主程序，自动调用 `fetch_paper.py`，获取 Google Scholar 引用数。
- [`website.py`](https://github.com/chenxuanyi-hub/get-citations/blob/main/website.py)  
  使用 Streamlit 制作网页，展示论文与引用数，支持搜索和数据更新。

## 依赖库

请确保已安装以下 Python 库：

- [`requests`](https://docs.python-requests.org/en/master/)
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [`selenium`](https://selenium-python.readthedocs.io/)
- [`webdriver-manager`](https://github.com/SergeyPirogov/webdriver_manager)
- [`streamlit`](https://docs.streamlit.io/)
- [`pandas`](https://pandas.pydata.org/)

安装方式：
```bash
pip install requests beautifulsoup4 selenium webdriver-manager streamlit pandas
```

## 使用说明

1. **运行主程序**
    - 在 VSCode 或终端运行 [`get_citations.py`](https://github.com/chenxuanyi-hub/get-citations/blob/main/get_citations.py)，自动获取论文的引用数
    - 运行过程中会弹出 Google Scholar 页面，请手动完成人机验证（约每 280 篇需验证一次）
    - 若验证超时，部分引用数会记为 `null`，并提示超时

2. **数据保存与展示**
    - 程序结束后，终端显示：
      ```
      已保存 citations_selenium.json，浏览器已关闭
      请在终端输入 streamlit run website.py
      ```
    - 按提示输入 `streamlit run website.py`，即可打开本地网页，浏览和搜索论文引用数

3. **更新数据**
    - 网页内点击“更新”按钮，可自动运行 [`get_citations.py`](https://github.com/chenxuanyi-hub/get-citations/blob/main/get_citations.py) 并刷新数据

## 注意事项

- 建议使用 Chrome 浏览器，并确保 ChromeDriver 版本与本地浏览器兼容
- 需手动处理 Google Scholar 的人机验证
- 若引用数获取失败，将显示为 `null`
- 可使用 `pip list` 检查依赖库安装情况

