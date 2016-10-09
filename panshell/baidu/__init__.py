#coding=utf-8
#author@alingse
#2016.10.09

from panshell.core import FS


class baidu(FS):
    name = 'baidu'
    def __init__(self,**kwargs):
        name = kwargs.pop('name',self.name)
        FS.__init__(self,name,**kwargs)

    def do_ls(self,line):
        print(self.name,'ls')
