# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:05:06 2018

@author: Balaji
"""
from math import atan2,acos

class vector():
    
    def _init_(self,v): # constructor to initialize a vector from a given vector
        self.x = v.x    # x component of the vector
        self.y = v.y    # y component of the vector
        self.z = v.z    # z component of the vector
    
    def __init__(self,x = 0,y = 0,z = 0): 
        if isinstance(x,vector):
            self._init_(x)
        else :
            self.x = x
            self.y = y
            self.z = z
  
    def set(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
        
    def setmag(self,mag):
        temp = self.unit()
        temp.mul(mag)
        self.set(temp.x,temp.y,temp.z)
        
    def __repr__(self):
        return f'{self.x}i{self.y:+}j{self.z:+}k'
    
    def copy(self):
        temp = vector(self)
        return temp
        
    def mag(self):
        x = pow(self.x,2)
        y = pow(self.y,2)
        z = pow(self.z,2)
        return pow(x+y+z,0.5)
    
    def __abs__(self):
        return (self.x*self.x + self.y*self.y + self.z*self.z)**0.5
    
    def add(self,A,B=0,C=0):
        if isinstance(A,vector):
            self.x+= A.x
            self.y+= A.y
            self.z+= A.z
        else :
            self.x+=A
            self.y+=B
            self.z+=C
    
    def __add__(self,A):
        x = self.x + A.x
        y = self.y + A.y
        z = self.z + A.z
        temp = vector(x,y,z)
        return temp
        
    def sub(self,A,B=0,C=0):
        if isinstance(A,vector):
            self.x-= A.x
            self.y-= A.y
            self.z-= A.z
        else :
            self.x-=A
            self.y-=B
            self.z-=C

    def __sub__(self,A):
        x = self.x - A.x
        y = self.y - A.y
        z = self.z - A.z
        temp = vector(x,y,z)
        return temp
    
    def mul(self,scale):
        self.x*=scale
        self.y*=scale
        self.z*=scale
            
    def __mul__(self,scale):
        if isinstance(scale,vector):
            temp = self.dot(scale)
            return temp
        elif isinstance(scale,int) or isinstance(scale,float):
            temp = vector(self)
            temp.x*=scale
            temp.y*=scale
            temp.z*=scale
            return temp
    
    def div(self,n):
        self.x/=n
        self.y/=n
        self.z/=n
    
    def __truediv__(self,scale):
        if isinstance(scale,int) or isinstance(scale,float):
            temp = vector(self)
            temp.x/=scale
            temp.y/=scale
            temp.z/=scale
            return temp
        elif isinstance(scale,vector):
            temp = vector()
            temp.x = self.x/scale.x
            temp.y = self.y/scale.y
            temp.z = self.z/scale.z
            return temp
    
    def dist(self,v):
        dx = self.x - v.x
        dy = self.y - v.y
        dz = self.z - v.z
        return pow((dx*dx + dy*dy + dz*dz),0.5)
    
    @staticmethod
    def distance(v1,v2):
        dx = v1.x - v2.x
        dy = v1.y - v2.y
        dz = v1.z - v2.z
        return pow((dx*dx + dy*dy + dz*dz),0.5)

    def dot(self,A):
        x = self.x*A.x
        y = self.y*A.y
        z = self.z*A.z
        return (x+y+z)
    
    def cross(self,v1):
        temp = vector()
        temp.x = self.y*v1.z - self.z*v1.y
        temp.y = self.z*v1.x - self.x*v1.z
        temp.z = self.x*v1.y - self.y*v1.x
        return temp
    
    def unit(self):
        return self/abs(self)
    
    def limit(self,max):
        if (abs(self) > max):
            temp = self.unit()
            temp.mul(max)
            self.set(temp.x,temp.y,temp.z)
        
    def heading2D(self):
        angle = atan2(-self.y,self.x)
        return -1*angle
    @staticmethod
    def angleBetween(v1,v2):
        DOT = v1*v2
        v1mag = abs(v1)
        v2mag = abs(v2)
        return acos(DOT / (v1mag * v2mag))
    
    def array(self):
        array = [None,None,None,None,None]
        array[0] = self.x
        array[1] = self.y
        array[2] = self.z
        array[3] = abs(self)
        array[4] = self.heading2D()
        return array
        
