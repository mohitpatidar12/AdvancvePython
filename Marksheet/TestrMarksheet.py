import MarksheetBean
import MarksheetDao
from MarksheetDao import *

def testAdd():
    mb= MarksheetBean()
   # mb.setRollNo(11)
    mb.setName("hit")
    mb.setPhysics(80)
    mb.setMaths(95)
    mb.setChemistry(79)
    md= MarksheetDao()
    md.Add(mb)
    print("success full")

testAdd()

def testDelete():
    mb = MarksheetBean()

    mb.setRollNo(1002)
    md = MarksheetDao()
    md.Delete(mb)

    print("successful delete ")

#testDelete()

def testupdate():
    mb = MarksheetBean()

    mb.setName("rahul")
    mb.setRollNo(211)
    mb.setPhysics(51)
    mb.setChemistry(52)
    mb.setMaths(53)
    md= MarksheetDao()
    md.update(mb)
    print("successful update")

#testupdate()

def testsearch():
    md=MarksheetDao()
    md.search()
    print("successful search ")
# testsearch()

def serch_single():
    mb=MarksheetBean()
    mb.setRollNo(211)
    md=MarksheetDao()
    md.search_single(mb)
    print("successful single search ")
#serch_single()


