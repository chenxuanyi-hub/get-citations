import streamlit as st
import pandas as pd
import json
import os
import subprocess

st.set_page_config(page_title="Citations in Google Scholar")
st.title("Citations in Google Scholar")

base_path = os.path.dirname(__file__)
file_name = 'citations_selenium.json'
file_path = os.path.join(base_path,file_name)

if st.button('更新'):
    subprocess.run(["python", os.path.join(base_path, "get_citations.py")])
    st.success("数据已更新！")


with open(file_path,'r',encoding='utf-8') as all:
    papers = json.load(all)
    df = pd.DataFrame(list(papers.items()), columns=["论文标题", "引用数"])
    df.index = df.index + 1

    query = st.text_input("输入论文标题关键词进行搜索")
    if query:
        filtered_df = df[df["论文标题"].str.contains(query, case=False, na=False)]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)
    st.write(f"总共 {len(df)} 篇论文。")
    st.markdown("""
    **说明**：
    - 本页面展示了通过 Selenium 自动化浏览器查询 Google Scholar 获取的论文引用数。
    - 由于 Google Scholar 对自动化查询有限制，可能会遇到验证码（
CAPTCHA）问题，导致部分论文引用数无法获取。
    - 若需要更新数据，请点击上方“更新”按钮，程序会重新运行 `get_citations.py` 脚本。
    - 请确保在运行环境中已正确配置 Selenium 和 ChromeDriver。
    """)




