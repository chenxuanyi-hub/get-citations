# get-citations
基本概述：

  用于从谷歌学术上爬取SIGIR上论文的引用数。

  fetch_paper.py用于获取SIGIR网站上的全部论文名称，若要修改数量，可以直接修改return函数的返回值
  
  get_citations.py为主要的程序，用于获取Google Scholar的论文引用数
  
  website.py用于呈现论文和引用数，提供更新功能和搜索功能。



注意事项：

  对于fetch_paper.py，需要用到的模块及作用分别是：
  
    requests，用于请求网页
    
    bs4 ,用于解析html文件为DOM树
  
  对于get_citations.py，需要用到的模块及作用分别是：
  
    time、random，用于在访问之后等待随机数，来模仿人类访问的行为
    
    json，用于将获得的论文名称和引用数的字典转为json文件
    
    re，用于搜索引用数，最开始是为了防止数字之间存在逗号所以使用正则表达式，但发现谷歌学术上引用数无逗号
    
    BeautifulSoup，用于解析网页
    
    from webdriver_manager.chrome import ChromeDriverManager；from selenium import webdriver； from selenium.webdriver.chrome.service import Service 用来作为浏览器驱动，人为的解决人机验证问题，是对于谷歌学术反爬虫手段的应对
    
    fetch_paper，用于获取论文列表
  
  对于website.py，需要用到的模块及作用分别是：
  
    streamlit，用于网页的制作与呈现
    
    pandas，用于制表
    
    json，用于读入get_citations.py获得的json文件
    
    os，用于添加json文件路径，方便后期修改
    
    subprocess，用于网页更新，点下更新按钮之后，会开启一个子进程，再次运行get_citations.py
  
  
  本项目使用到的库函数较多，在运行前请先确认环境是否已经配好,
  
  可在终端里使用pip list确认自己安装的库,
  
  若没有安装，使用 pip install <模块名>来进行安装。



使用说明：

  fetch_paper.py无需运行，在get_citations.py会自动调用。
  
  只需在vscode中运行get_citations.py，可以获得citations_selenium.json文件，运行时，终端会显示论文获取进程。
  
  运行get_citations.py，大概率会跳出谷歌学术的页面进行人机验证，需手动完成，正常需要两次人机验证，约280篇进行一次人机验证。若未及时进行人机验证，会导致将引用数记为null，同时终端给出超时的提醒。
  
  等到终端显示：
  
                已保存 citations_selenium.json，浏览器已关闭
                请在终端输入 streamlit run website.py
                
  在终端中输入   streamlit run website.py即可打开网页，可视化获取结果。
