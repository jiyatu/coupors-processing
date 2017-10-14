import codecs
import xlsxwriter
import os
import re
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
def delblankline(infile,outfile):
    if infile.endswith('txt'):
        infopen = codecs.open(infile,'r','utf16')
        outfopen = codecs.open(outfile,'w','utf16')
        lines = infopen.readlines()
        for line in lines:
            if line.split():
                outfopen.writelines(line)
            else:
                outfopen.writelines("")
        infopen.close()
        outfopen.close()
def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    #word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)
    return match
# from xlutils.copy import copy
def isEmpty(str):
    if str =="":
        return True
    else:
        return False
def readdir(rootdir):
    '''excel = 'C:\\Users\\JYT\\Desktop\\test\\test.xlsx'
    try:
        rdx = xlrd.open_workbook(excel, formatting_info=True)  # 打开Excel，并保留原格式
    except:
       print("no excel in %s " % excel)'''
    adict = {"Ô": "У", "Ö": "Ц", "Æ": "Ж", "Ý": "Э", "Í": "Н", "Ã": "Г", "Ø": "Ш", "¯": "Ү", "Ç": "З", "Ê": "К",
             "Ú": "Ъ", "Å": "Е", "Ù": "Щ", "É": "Й", "Û": "Ы", "Á": "Б", "ª": "Ө", "À": "А", "Õ": "Х", "Ð": "Р",
             "Î": "О", "Ë": "Л", "Ä": "Д", "Ï": "П", "ß": "Я", "×": "Ч", "¨": "Ё", "Ñ": "С", "Ì": "М", "È": "И",
             "Ò": "Т", "Ü": "Ь", "Â": "В", "Þ": "Ю", "ô": "ф", "ö": "ц", "ó": "у", "æ": "ж", "ý": "э", "í": "н",
             "ã": "г", "ø": "ш", "¿": "ү", "ç": "з", "ê": "к", "ú": "ъ", "å": "е", "ù": "щ", "é": "й", "û": "ы",
             "á": "б", "º": "ө", "à": "а", "õ": "х", "ð": "р", "î": "о", "ë": "л", "ä": "д", "ï": "п", "ÿ": "я",
             "÷": "ч", "¸": "ё", "ñ": "с", "ì": "м", "è": "и", "ò": "т", "ü": "ь", "â": "в", "þ": "ю"}
    wtx = xlsxwriter.Workbook("F:\博士工作\导师任务\新建文件夹\z要处理的文件\\corpus2-new.xlsx")  # 在指定目录下创建一个excle
    sheet = wtx.add_worksheet("西里尔2")  # 新建一个sheet
    # wtx = copy(rdx)  # 复制为可读写的wtx
    # sheet = wtx.get_sheet(0)
    blod = wtx.add_format({"bold": True})  # 定义exlce中写入的字体
    for parent, dirnames, filenames in os.walk(rootdir):
        # print(parent)  # 查看文件的父目录
        n = -1  # 定义一个变量
        for filename in filenames:  # 将文件夹下所有文件写入Excel
            abspath = os.path.join(parent, filename)
            nabspath = os.path.join(parent, "new" + filename)
            print(abspath)
            print('/n' * 3)
            delblankline(abspath, nabspath)
            # os.remove(abspath)
            filename = "new" + filename
            if filename.endswith('txt') and filename.startswith('new')and filename != "1我自己弄的对照表.txt":
                with codecs.open(nabspath, 'r', 'utf16') as f:
                    lineC = f.readline()  # 读取中文
                    # f = open(abspath, 'r')
                    lineM = f.readline()
                    if contain_zh(lineM):
                        for key, value in adict.items():
                            lineC = lineC.replace(key, value)
                        #lineC = lineM
                        #lineM = f.readline()
                        while lineC and lineM:
                            n = n + 1
                            sheet.write(n, 0, lineM, blod)  # 分行分列写入
                            sheet.write(n, 1, lineC, blod)  # 分行分列写入
                            sheet.write(n, 2, filename, blod)
                            lineC = f.readline()
                            if isEmpty(lineC):
                                break
                            for key, value in adict.items():
                                lineC = lineC.replace(key, value)
                                # lantype = judgeLan(lineC)
                            # if lantype[0] == "uk":'''
                            # c = num_second(lineC)
                            # if not (is_chinese(c[0:1])):
                            if  (contain_zh(lineC)):
                                lineC = f.readline()
                                #  for key, value in adict.items():
                                #   lineM = lineM.replace(key, value)

                            lineM = f.readline()  # 读取中文
                            if isEmpty(lineM):
                                break
                            # word = num_second(lineM)
                            # for word in  lineM.split(' '):
                            # for
                            # lantype = judgeLan(lineM)
                            # if is_chinese(word[0:1]):
                            if not contain_zh(lineM):
                                lineC = lineM
                                lineM = f.readline()
                    for key, value in adict.items():
                        lineM = lineM.replace(key, value)

                    while lineC and lineM:
                        n = n + 1
                        sheet.write(n, 0, lineC, blod)  # 分行分列写入
                        sheet.write(n, 1, lineM, blod)  # 分行分列写入
                        sheet.write(n, 2, filename,blod)
                        lineC = f.readline()  # 读取中文
                        if isEmpty(lineC):
                            break
                        if not (contain_zh(lineC)):
                            lineC = f.readline()

                        lineM = f.readline()
                        if isEmpty(lineM):
                            break
                        for key, value in adict.items():
                            lineM = lineM.replace(key, value)
                        if contain_zh(lineM):
                            lineC = lineM
                            lineM = f.readline()

                        # lines.decode('utf-8').encode('unicode')  # 当前脚本编码为utf-8
    wtx.close()  # 关闭excle
    # for lines in f.readlines():
    #  sheet.write(i, j, lines)
    #  j += 1
    # i += 1
    print("write new information successfully")
    # wtx.save(excel)
    print("save the information successfully!")


readdir('F:\博士工作\导师任务\新建文件夹\z要处理的文件')
