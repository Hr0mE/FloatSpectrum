def spectr(start, end, step=1, deep=2): #функция range, но для float
    d = 10**deep
    return [i/d for i in range(round(start*d), round(end*d), round(step*d))] 

def int_spectr(start, end, step=1, deep=2): #Выводит только целые числа на промежутке, чем больше глубина, тем больше точность целых чисел
    d = 10**deep
    return [int(i/d) for i in range(round(start*d), round(end*d), round(step*d)) if str(i/d)[-1] == '0']


'''
args = (9, 4, -1.53)
print(spectr(*args))    
print(int_spectr(*args))
'''
