#-*- coding：utf8 -*-

#那么在使用 from xxx import * 时只有__all__里面的东西能用
__all__ = ["test1"]

def test1():
    print "test1"

def test2():
    print "test2"