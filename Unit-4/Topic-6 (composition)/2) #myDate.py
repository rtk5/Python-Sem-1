#
class MyDate:
    def __init__(self,dd,mm,yy):
        self.dd=dd
        self.mm=mm
        self.yy=yy
    def __str__(self):
        return str(self.dd)+"-"+str(self.mm)+"-"+str(self.yy)
    def key(self):
        return self.dd*365+self.mm*30+self.dd
d=MyDate(15,8,1947)
print(d)

#independence day
class MyEvent:
    def __init__(self,dd,mm,yy,detail):
        self.date=MyDate(dd,mm,yy)
        self.detail=detail
    def __str__(self):
        return str(self.date)+"=>"+self.detail
    def key(self):
        return self.date.key()
e=MyEvent(15,8,1947,"Independence Day")
print(e)

mylist=[MyEvent(26,1,1956,"Republic day"),MyEvent(2,10,1868,'Gandhi Jayanti')]
for e in sorted(mylist,key=MyEvent.key):
    print(e)
    