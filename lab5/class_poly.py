
class Polynomial:
    def __init__(self, data_init):
        if isinstance(data_init, dict):
            self._data = dict(data_init)
            
        if isinstance(data_init, list):
            new_data_init = {}
            for i in range(len(data_init)):
                new_data_init[i] = data_init[i]
            self._data = dict(new_data_init)       
    
    def __setitem__(self, key, value):
        self._data[key] = value
        
    
    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            return ('0')
    
    def __delitem__(self, key):
        del self._data[key]
    
    def __str__(self):
        result = ''
        
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] != 0:
                if self._data[i] == 1:
                    if i == 0:
                        result = result + '1'
                    elif i == 1:
                        result = result + 'x'
                    else:
                        result = result  + 'x' +'^' + str(i) 
                elif self._data[i] < 0:
                    if self._data[i] == -1:
                        if i == 0:
                            result = result + '-1'
                        elif i == 1:
                            result = result + '-x'
                        else:
                            result = result  + '-x' +'^' + str(i)
                    else:
                        if i == 1:
                            result = result + str(-self._data[i]) + '*x'
                        elif i == 0:
                            result = result + str(-self._data[i])
                        else:
                            result = result + str(-self._data[i]) + '*x' +'^' + str(i)
                else:
                    if i == 1:
                        result = result + str(self._data[i]) + '*x'
                    elif i == 0:
                        result = result + str(self._data[i])
                    else:
                        result = result + str(self._data[i]) + '*x' +'^' + str(i)
            if i != 0 and self._data[i-1] > 0 and result != '':
                result = result + ' + '
            elif i != 0 and self._data[i-1] < 0 and result != '':
                result = result + ' - '
        return result

    def __add__(self, other):
        poly = Polynomial({})
        for i in range(len(self._data)):
            poly._data[i] = self._data[i] + other._data[i]
        return poly
            
    def __sub__(self, other):
        poly = Polynomial({})
        for i in range(len(self._data)):
            poly._data[i] = self._data[i] - other._data[i]
        return poly
    
    def __mul__(self, other):
        d = dict()
        for i in range(len(self._data)*len(other._data)):
            d[i] = 0
        for k in range(len(self._data)):
            for j in range(len(other._data)):
                d[k+j] = d[k+j] + self._data[k]*other._data[j]
        poly = Polynomial(d)
        return poly

    def __pow__(self, num):
        poly = Polynomial({})
        for i in range(num-1):
            poly = self*poly
        return poly

    def __neg__(self):
        poly = Polynomial({})
        for i in range(len(self._data)):
            poly._data[i] = -self._data[i].copy()
        return poly

    def __call__(self, value):
        result = 0
        for i in range(len(self._data)):
            result = result + self._data[i]*(value**i)
        return result


p1 = Polynomial([2, 1])
p2 = Polynomial({0: -2, 1: 1})
print(p1 + p2)
print(p1)
print(p2)

