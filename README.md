# get-citations
用于从谷歌学术上爬取SIGIR上论文的引用数。

fetch_paper.py用于获取SIGIR网站上的全部论文名称，若要修改数量，可以直接修改return函数的返回值
get_citations.py为主要的程序，用于获取Google Scholar的论文引用数
website.py用于呈现论文和引用数，提供更新功能和搜索功能。


只需在vscode中运行get_citations.py，可以获得citations_selenium.json文件。
后再终端中输入   streamlit run website.py即可打开网页。
