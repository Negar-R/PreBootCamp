def GCD (a : float, b : float) -> float:
    '''
    این تابع قرار عه ب . م . م حساب کنه 
    '''
    while b:
        a , b = b , a%b
        
    return a

print(GCD(15,1320))

print(GCD.__doc__)

'''
doc_string
'''
