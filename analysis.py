import re
import jieba

def getFrontAndBack(filename:str):
    if filename.__contains__('.txt'):
        file = open(filename, encoding='gbk')
        keyword = filename.replace('.txt', '').replace('/examples/','')
    else:
        file = open(filename+'.txt',encoding='gbk')
        keyword = filename.replace('./examples/','')

    str_infile = file.read()
    pattern = '([\S]{0,5})'+keyword+'([\S]{0,5})'
    text = re.findall(pattern,str_infile)
    # for txt in text:
    #     print(txt)

    return text


def cutforDic(text:list):
    front_dic = {}
    back_dic = {}
    stopwords  = [w.strip() for w in open('stopwords.txt').readlines()]
    for t in text:
        seg_list1 = jieba.lcut(t[0])
        seg_list2 = jieba.lcut(t[1])
        for seg in seg_list1 :
            if seg not in stopwords:
                if seg in front_dic :
                    front_dic[seg]+=1
                elif seg not in front_dic :
                    front_dic[seg]=1
        for seg in seg_list2 :
            if seg not in stopwords:
                if seg in back_dic:
                    back_dic[seg]+=1
                elif seg not in back_dic:
                    back_dic[seg]=1

    print(sorted(front_dic.items(), key=lambda item: item[1], reverse=True))
    print(sorted(back_dic.items(), key=lambda item: item[1], reverse=True))

if __name__ == "__main__":

    cutforDic(getFrontAndBack('./examples/死马.txt'))
