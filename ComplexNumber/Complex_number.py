
# coding: utf-8

# ## Task: Making Complex_Numbers Package:
# 
# 
# Define a class called complex_number which accepts 2 parameters:
# 
# * x: int64, float64, represents real component of the complex number
# * y: int64, float64, represents imaginary component of the complex number

# In[1]:

class Complex(object):
    try: 
        def __init__(self, real, imag=0.0):
            if((type(real)==int or type(real)==float)and(type(imag)==int or type(imag)==float)) :
                self.r = real
                self.i = imag
                self.math = __import__('math')
                self.sys = __import__('sys')
            else :
                print('use the float or int real and imaginary part')
    except:
        print('Error in intiation')

    def __add__(self, other):
        try:
            return Complex(self.r + other.r,
                           self.i + other.i)
        except EXception as e:
            print('Error in add \n',e)

    def __sub__(self, other):
        try:
            return Complex(self.r - other.r,
                       self.i - other.i)
        except EXception as e:
                print('Error in sub \n',e)

    def __mul__(self, other):
        try:
            return Complex(self.r*other.r - self.i*other.i,
                       self.i*other.r + self.r*other.i)
        except Exception as e :
                print('Error in mul \n', e)

    def __truediv__(self, other):
        try:
            sr, si, orr, oi = self.r, self.i, other.r, other.i 
            r = float(orr**2 + oi**2)
            return Complex((sr*orr+si*oi)/r, (si*orr-sr*oi)/r)
        except Exception as e:
            print('Error in division \n', e)
    def __abs__(self):
        try:
            return self.math.sqrt(self.r**2 + self.i**2)
        except Exception as e :
            print('Error in abs \n', e)
    
    def __repr__(self) :
        try:
            return '{0:.2f}{1:+.2f}i'.format(self.r,self.i)
        except Exception as e :
                print('Error in represnt \n', e)
        
    def real(self):
        return self.r
        
    def imag(self):
        return self.i
    
    def argument(self):
        try:
            return (self.math.atan(self.i/self.r))
        except Exception as e :
                print('Error in argument \n', e)
        
    def conjugate(self):
        return complex(self.r, - self.i)  
    


# In[2]:

a=Complex(2,3)
b=Complex(3.4,4.3)


# ### Questions:
# Define the follwoing operations for the class:
# 
# * representation in the form of x + yi when used with print command
# * '+'
# * '-'
# * '*'
# * '/'

# In[3]:

print('a :',a)
print('a+b :',a+b)
print('a-b :',a-b)
print('a*b :',a*b)
print('a/b :',a/b)


# * abs()
# * real() [Returns real component of the complex number]
# * imag() [Returns complex component of the complex number]
# * argument() [Returns argument of the complex number]
# * conjugate() [Returns conjugate of the complex number]
# 

# In[4]:

print('abs(b) :',abs(b))
print('a.real :',a.real())
print('b.imag :',b.imag())
print('a.argument() :',a.argument())
print('b.conjugate :',b.conjugate())


# #### Error handling

# In[5]:

c=Complex(0,0)
a/c


# In[6]:

get_ipython().system('jupyter nbconvert --to python Untitled.ipynb')

