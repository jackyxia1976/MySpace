#purpose: try import function
# Purpose2:Try Class
# from Sort import sort1
from D10_corepro.auth_corepro import auth_corepro as auth1

import json

class Mysort(object):
    "Main for 练习Class使用"
    def __init__(self,A,B,C,x=3,fname='imooc.txt'):
        self.A = A
        self.B = B
        self.C = C
        self.fname=fname
        self.x = x
        print(self.x)
        # self.sort1([self.A,self.B,self.C])
        # self.Timeprint()
        # self.find_start_python(self.fname)
        # self.lamdafunc(self.x)
        self.fileoper()

    def sort1(self,arr):
        tot=len(arr)
        for i in range(0,tot):
            for j in range(0,tot-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        self.arr=arr
        print(self.arr)
        return self.arr

    def Timeprint(self):
        #import time
        import datetime
        nowtime = (datetime.datetime.now()-datetime.timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S")
        print('採集時間：',nowtime)
        # nowtime1 = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # print('採集時間1：',nowtime1)
        return nowtime

    def find_start_python(self,fname):
         f=open(self.fname)
         for line in f:
             if line.startswith('python'):
                 print (line)
         # find_start_python('imooc.txt')

    def lamdafunc(self,x):
        f2=lambda y:y*y
        # print("f2:",f2(self.x))
        return f2(x)

    def fileoper(self):
        fo=open("imooc.txt","r+")
        # print ("file name:",fo.name)
        lines=fo.readlines()
        L=""
        L1=""
        data_list=[]
        for line in lines:
            # line=line.strip()
            line = line.replace("\n", '')
            # print (type(line))
            print (line)
            # data_list=data_list.append(line)
            L=L+line+","
        L="{"+L+"}"
        #最后一个字符不能为“，”
        L = ''.join([L[i] for i in range(len(L)) if i!= 104])
        print(L)
        L = json.loads(L)
        print(type(L))

        #下面的方法也可以，更科学
        # 最后一个字符不能为“，”
        for i in range(lines.__len__() - 1):
            lines[i] = lines[i].replace("\n", '')
            L1=L1+lines[i]+","
        L1=L1+lines[lines.__len__() - 1].replace('\n','')
        L1="{"+L1+"}"
        L=json.loads(L1)
        print(type(L1))

        # print ("file close?:",fo.closed)
        # print ("file mode:",fo.mode)


# Mysort.Timeprint()
# print(Mysort.__doc__)
A_sort=Mysort(1,10,3,x=1234,fname='imooc.txt')
# print (A_sort.B)
# A_sort.find_start_python('imooc.txt')
T=A_sort.Timeprint()
# print("Now:",T)
print("Call:",A_sort.lamdafunc(A_sort.x))

# B5device=auth1(
#     ProductKey='6453668283668082833',
#     DeviceName='P115XK828',
#     DeviceSecret='188c8a493e14354ed0ae164db678ff55446f97a13abfd3430f2e6f98f8d3b6dfe7b48efae725977c15af5f1207efd7b462ab4d8a3e556e15c856cc940b0c2a6e'
# )
