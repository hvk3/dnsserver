import random
dnsRecordList = ['192.168.55.56', '192.168.55.115', '192.168.49.237']	#maintains records of dns servers
priorityList = []
sumPriorityList = []
f = open('/etc/bind/zones/db.example.com','r')
sum = 0
for i in range(3):
	priority = random.randint(1,1000000)
	sum += priority
	priorityList.append(priority)
	sumPriorityList.append(0)
for i in range(len(priorityList)):
	priorityList[i] = (int)((float)(priorityList[i]/(sum + 0.0)) * 1000000)
	sumPriorityList[i] = priorityList[i]
for i in range(1,len(priorityList)):
	sumPriorityList[i] = sumPriorityList[i - 1] + priorityList[i]
b = random.randint(1,1000000)
pos = -1
for i in range(len(priorityList)):
	if(sumPriorityList[i]>b):
		pos = i
		break

lines = f.readlines()
if '@' not in lines[len(lines)-1]:
	lines = lines[:-1]
lines.append('www\t\t\t\tIN\t\tA\t\t'+dnsRecordList[pos]+"\n")
f.close()
open('/etc/bind/zones/db.example.com', 'w').close()
f = open('/etc/bind/zones/db.example.com','w')
for i in range(len(lines)):
	f.write(lines[i])
f.close()