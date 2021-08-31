#coding:utf-8
import requests
# 获取网络图片的BASE64数据
def url_to_base64code(url):
    hds = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)'
    }
    r = requests.get(url, headers=hds)
    print(r.content)
    return r.content
def run():
    print("======================markdown文件插入图片代码的助手======================")
    print("请输入：图片的网址")
    print("       本地图片的路径")
    print("       输入3，再使用工具，截图")
    t=input("请输入:")
    if 'http' in t:
        pass
    elif t[1:3]==':\\':
        pass
    elif t=='3':
        pass

if __name__=="__main__":
    url = 'https://cdn.jsdelivr.net/gh/kangzai228/blog_cdn_jsdelivr@1.0.1/assets/img/my_photo.png'
    url_to_base64code(url)