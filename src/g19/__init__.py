#!/usr/bin/env python



FB_DEVICE = "/dev/fb1"


LED_DEVICES = "/sys/class/leds/g19_0:{color}:{c_type}/brightness"

        

class KeyboardColors(object):
    
    _colors = ("green", "red", "blue")
   
    def __getattr__(self, name):
        if (name in KeyboardColors._colors):
            return open(LED_DEVICES.format(**{'color':name, 'c_type':"bl"}), "rb").read()
    
    def __setattr__(self, name, value):
        print value
        open(LED_DEVICES.format(**{'color':name, 'c_type':"bl"}), "r+b").write(value)
    
    

print KeyboardColors().green

KeyboardColors().green = 0

print KeyboardColors().green

class KeyboardColors2:
    
    
    
    class Background:

        __TYPE = "bl"
        
        
        def __get__(self, obj, cls=None):
            pass
        
        def __set__(self, obj, val):
            pass
        
        def __delete__(self, obj):
            pass
            

        @property
        def green(self):
            
            return open(LED_DEVICES.format).read()
        
        @green.setter
        def green(self, g):
            pass
        
        @property
        def red(self):
            pass
        
        @red.setter
        def red(self, r):
            pass
        
        @property
        def blue(self):
            pass
        
        @blue.setter
        def blue(self, b):
            pass
        
        @property
        def color(self):
            pass
        
        @color.setter
        def color(self, color):
            pass
