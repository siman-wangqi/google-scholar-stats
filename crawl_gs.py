# 爬取谷歌学术引用量的脚本
from scholarly import scholarly
import json
import os

YOUR_USER_ID = "wv7uLCMAAAAJ&hl" 

def get_citations():
    try:
        # 爬取你的谷歌学术数据
        author = scholarly.search_author_id(YOUR_USER_ID)
        author = scholarly.fill(author)
        total_citations = str(author['citedby'])  # 提取总引用量
        return total_citations
    except Exception as e:
        print(f"爬取失败：{e}")
        return "0"  # 失败时显示0

# 生成shields.io需要的JSON文件
data = {"message": get_citations()}
with open("gs_data_shieldsio.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print(f"当前引用量：{data['message']}")
