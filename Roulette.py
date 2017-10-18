import random


class InRange:
    'an inside object of a roullete, used to compare if larger or smaller'
    def __init__(self, min_value, max_value):
        self.__minValue = float(min_value)
        self.__maxValue = float(max_value)

    def __cmp__(self, other):
        if type(other) is not float and type(other) is not int:
            raise ValueError('cannot compare ' + self.__class__.__name__ + ' to a ' + str(type(other)) + ' type')

        if self.__minValue > other:
            return 1

        if self.__maxValue <= other:
            return -1

        return 0

    def min(self):
        return self.__minValue

    def max(self):
        return self.__maxValue

    def __repr__(self):
        return 'InRange(' + str(self.__minValue) + ', ' + str(self.__maxValue) + ')'

    def __str__(self):
        return repr(self)


class Roulette:
    'A Roulette like chooser, input objects with the chance to get it, returns randomly a single object'
    def __init__(self):
        self.__maxRandValue = 0
        self.__objectList = []

    def __str__(self):
        ret_str = 'Roulette('
        first = True
        for item in self.__objectList:
            if not first:
                ret_str += ',\n'
            else:
                first = False
            ret_str += str(item[0]) + ': ' + str(type(item[1]))
        ret_str += ')'
        return ret_str

    def append(self, chance, obj):
        if type(chance) is not float and type(chance) is not int:
            raise ValueError('chance must be a float or an int, it cannot be a ' + str(type(chance)))
        self.__objectList.append((InRange(self.__maxRandValue, self.__maxRandValue + chance), obj))
        self.__maxRandValue += chance

    def iteritems(self):
        for item in self.__objectList:
            yield item[0], item[1]

    def max(self):
        return self.__maxRandValue

    def roll(self):

        if len(self.__objectList) == 0:
            raise ValueError('Roulette is empty')

        val = random.uniform(0, self.__maxRandValue)
        # binary search
        first = 0
        last = len(self.__objectList) - 1

        while first <= last:
            midpoint = (first + last) // 2
            if self.__objectList[midpoint][0] == val:
                return self.__objectList[midpoint][1]
            elif self.__objectList[midpoint][0] > val:
                last = midpoint - 1
            else:
                first = midpoint + 1

        raise ValueError('something went wrong, this should not happened, val = ', str(val) + ', ' + str(self))
