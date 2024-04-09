'''from network2 import *
 = Network("G:/UT/2_Transportation Network Analysis/Homeworks/Homework 5/Coding/SiouxFalls_net.txt",
              "G:/UT/2_Transportation Network Analysis/Homeworks/Homework 5/Coding/SiouxFalls_trips.txt")

net.userEquilibrium("FW", 40, 1e-6, 1)

highway=('(5,9)','(9,5)','(9,10)','(10,9)','(10,15)','(15,10)','(15,22)','(22,15)','(22,21)','(21,22)')

for i in highway:   
   net.link[i].capacity*=2
   net.link[i].freeFlowTime*=0.5


net.userEquilibrium("FW", 40, 1e-6, 1)'''

from network import *

net = Network("SiouxFalls_net.tntp", "SiouxFalls_trips.tntp")
highway=('(5,9)','(9,5)','(9,10)','(10,9)','(10,15)','(15,10)','(15,22)','(22,15)','(22,21)','(21,22)')

for i in highway:   
   net.link[i].capacity*=2
   net.link[i].freeFlowTime*=0.5


net.userEquilibrium("FW", 1000000, 1e-6, net.averageExcessCost)


for i in self.link:
    print("%s,%f",(self.link[i].flow,self.link[i].cost))
