#-*- coding:utf-8 -*-
nums = [10,11,12,13,14,15]

#在for中无break会执行的，没什么用
for num in nums:
    print num
    break
else:
    print('='*10)