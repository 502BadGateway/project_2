class info():
    def __init__(self):
        self.info1 = 1
        self.info2 = 'time'
        print 'initialised'

class MainFrame():
    def __init__(self):
        a=info()
        print a.info1
        b=page1(a)
        c=page2(a)
        print a.info1

class page1():
    def __init__(self, information):
        self.info=information
        self.info.info1=3

class page2():
    def __init__(self, information):
        self.info=information
        print self.info.info1

t=MainFrame()

"""
import urllib
resource = urllib.urlopen("http://maps.googleapis.com/maps/api/staticmap?center=51.5073509,-0.1277583&zoom=12&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels%7Cvisibility:off")
output = open("testName2.jpg","wb")
output.write(resource.read())
print"""