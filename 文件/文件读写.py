#-*- coding:utf-8 -*-
import sys
import os


'''
基本文件读写
'''

#打开方式 r w a（一般操作文本）
#二进制方式打开rb wb ab（声音，图像）
#可读写r+（必须存在） w+（存在打开，不存在创建） a+
#二进制方式打开可读写rb+ wb+ ab+

def showStr():
    file = open('test.txt', 'r')
    print file.read()
    file.close()

def writeFile(str):
    file = open('test.txt','w')
    file.write(str)
    file.close()

def appendFile(str):
    file = open('test.txt','a')
    file.write(str)
    file.close()
    
def backupFile(filePath):
    fileOld = open(filePath,'r')
    
    partition = filePath.find(".")
    type = sys.getfilesystemencoding()
    newName = (filePath[0:partition]+"(备份)"+filePath[partition:]).decode('utf-8').encode(type)
    
    fileNew = open(newName,'w')
    
    while True:
        str = fileOld.read(1024)
        if len(str) != 0:
            fileNew.write(str)
        else:
            break
    
    fileOld.close()
    fileNew.close()
    
#test

# writeFile("haha13")
# appendFile(" world")
# showStr()
# 
# backupFile("test.txt")

    
# readlines()读出内容，返回为列表，遇到换行法号就放一个元素
# readline()读一行内容，返回一个字符串

'''
文件定位
tell():当前文件位置
seek(offset,from):移动文件读取的指针
    offset:偏移量
    from：0.开头；1.当前位置；2.结尾
'''
def printFilePosition():
    file = open('test.txt','r')
    print file.tell()
    file.close

def printFileSeek(offset,frm=0):
    file = open('test.txt','r')
    file.seek(offset,frm)
    print file.tell()
    print file.read(1)
    
# test
# printFileSeek(2)


'''
文件重命名与路径相关

os来操作
os.rename(old, new)
os.mkdir(path)
os.chdir(path)
os.getcwd()
os.listdir
'''


#test
#os.rename('testbak.txt', 'testback.txt')
# type = sys.getfilesystemencoding()
# for fileName in os.listdir('.'):
#     print fileName.decode(type).encode('utf-8')
'''
批量重命名文件
'''

def renameAllFiles():
    type = sys.getfilesystemencoding()
    for fileName in os.listdir('.'):
        if fileName.split('.')[-1] == 'txt':
            print fileName.decode(type).encode('utf-8')

renameAllFiles()