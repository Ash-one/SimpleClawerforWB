import re


def getFrontAndBack(filename:str):
    if filename.__contains__('.txt'):
        file = open(filename, encoding='gbk')
        keyword = filename.replace('.txt', '')
    else:
        file = open(filename+'.txt',encoding='gbk')
        keyword = filename

    str_infile = file.read()
    pattern = '([\S]{0,5})'+keyword+'([\S]{0,5})'
    text = re.findall(pattern,str_infile)
    print(text)


if __name__ == "__main__":
    getFrontAndBack('死马')

