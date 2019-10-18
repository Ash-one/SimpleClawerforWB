import requests
import json
import re


def writeIntoFile(filename:str, content:str):
    file = open(filename, "a+")  # 以追加的方式
    file.write(content)

def replaceByRe(content:str):
    text  = re.sub(r'[<]([^\u4e00-\u9fa5]*)[>]', '', content)
    text2 = re.sub(r'[<]img[\S|\s]*[>]', '', text)
    text3 = re.sub(r'[<]a[\S|\s]*[>]', '', text2)
    return text3

def parserHTML(filename:str, string: str):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D'+ string +'&page_type=searchall&page=1'
    html = requests.get(url, headers=headers)
    html.raise_for_status()
    s = json.loads(html.text)

    data = s['data']

    pageNum = int(int(data['cardlistInfo']['total'])/10)

    for j in range(1, 10):
        try:
            text = s['data']['cards'][j]['mblog']['text']
            print(str(j) +"  " +replaceByRe(text))
            writeIntoFile(filename,str(j) +"\t" +replaceByRe(text)+'\n')
        except:
            continue


    for i in range(2,pageNum):
        url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D' + string + '&page_type=searchall&page=' + str(i)
        html = requests.get(url, headers=headers)
        html.raise_for_status()
        s = json.loads(html.text)

        for j in range(0,10):
            try:
                text = s['data']['cards'][j]['mblog']['text']
                print(str((i - 1) * 10 + j) +"  " +replaceByRe(text))
                writeIntoFile(filename,str((i - 1) * 10 + j) +"\t" +replaceByRe(text)+'\n')
            except:
                continue

def KeyWordClawer(filename:str, keyword:str):
    parserHTML(filename,keyword)


if __name__ == "__main__":
    KeyWordClawer("./examples/死马.txt","死马")
