# -*- coding: utf8 -*-

class Calc:
    """
    Calc 类用于将模板字符串转化为计算类，输出相应的系数
    系数要求唯一，template 的格式如下所示：
    {
       coeff1: {'gt': 3.1, 'lt': 4.2},
       coeff2: {'ge': 5.2, 'lt': 5.6},
       coeff3: {'gt': 7.2, 'le': 8.5},
       coeff5: {'eq': 8.9},
       ...
    }
    """
    def __init__(self, score, template):
        self.score = score
        self.template = template
        
    def __translate(self, x, kargs):
        calStr = []
        for k, v in kargs.items():
            if k is 'gt':
                calStr.append('%f>%f' % (x, v))
            elif k is 'ge':
                calStr.append('%f>=%f' % (x, v))
            elif k is 'lt':
                calStr.append('%f<%f' % (x, v))
            elif k is 'le':
                calStr.append('%f<=%f' % (x, v))
            elif k is 'eq':
                calStr.append('%f==%f' % (x, v))
        return ' and '.join(calStr)
    
    def calc(self):
        for k, v in self.kwg.items():
            calstr = self.__translate(self.x, v)
            result = eval(calstr)
            if result:
                return k

        return None