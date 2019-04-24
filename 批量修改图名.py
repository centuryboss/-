import xlrd
import os

list={}

def readList(path):
    book=xlrd.open_workbook(path)
    sheet=book.sheet_by_index(0)
    for i in range(sheet.nrows):
        num=str(int(sheet.cell(i,0).value))
        title=str(sheet.cell(i,1).value)
        list[num]=title
def main():
     name_list_path=input("输入文件名列表的xls文件地址：")
     readList(name_list_path)
     print(list)
     file_path=input("输入待修改文件目录：")+"\\"
     folder=os.listdir(file_path)
     prefix=input("输入文件名前缀：")
     separation=input("输入分隔符：")
     for file in folder:
         extension=file.split(".")[-1]
         num=file.split(".")[0]
         try:
             title=list[num]
             if prefix=="":
                new_name=num+separation+title+"."+extension
             else:
                new_name=prefix+separation+num+separation+title+"."+extension
             os.rename(file_path+file,file_path+new_name)
         except Exception:
             print(file+" 图名未给出！")
             
if __name__=="__main__":
    main()