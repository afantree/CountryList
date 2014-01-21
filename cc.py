#encoding=utf-8
import os,sys,sqlite3
from xml.etree import ElementTree

def dealDict(adict,cu):
    name = ' '
    code = ' '
    nameCN = ' '
    numberCode = '0'
    dialingCode = '0'
    for item in adict:
        if item.tag == 'Country_name':
            name = item.text
        if item.tag == 'Code':
            code = item.text
        if item.tag == 'Country_name_CN':
            nameCN = item.text
        if item.tag == 'NumberCode':
            numberCode = item.text
        if item.tag == 'DialingCode':
            dialingCode = item.text
    sqlStr = u"insert into countryList(name,code,nameCN,numberCode,dialingCode) values('"+name.replace("'","")+"','"+code+"','"+nameCN+"','"+numberCode+"','"+dialingCode+"');"
    print sqlStr
    cu.execute(sqlStr)
    

if __name__ == '__main__':
    treeroot=ElementTree.parse(os.getcwd()+'/CountryList.xml').getroot()
    conn = sqlite3.connect(os.getcwd()+'/CountryList.rdb')
    cu = conn.cursor()
    for item in treeroot:
        print item
        dealDict(item,cu)
    conn.commit()
