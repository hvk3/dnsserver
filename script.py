import random


def write_records(recordFile):
	dnsRecordList = ['192.168.55.56', '192.168.55.115', '192.168.49.237']
	priorityList = []
	with open(recordFile,'r') as f:
		priority_sum = 0
		for i in range(3):
			priority = random.randint(1,1000000)
			priority_sum += priority
			priorityList.append(priority)
		for i in range(len(priorityList)):
			priorityList[i] = (int)((float)(priorityList[i] / (priority_sum + 0.0)) * 1000000)
		sumPriorityList = priorityList[:]
		for i in range(1,len(priorityList)):
			sumPriorityList[i] = sumPriorityList[i - 1] + priorityList[i]
		b = random.randint(1,1000000)
		pos = -1
		for i in range(len(priorityList)):
			if sumPriorityList[i] > b:
				pos = i
				break
		lines = f.readlines()
		if '@' not in lines[len(lines)-1]:
			lines = lines[:-1]
		lines.append('www\t\t\t\tIN\t\tA\t\t' + dnsRecordList[pos] + '\n')
	with open(recordFile, 'w') as f:
		for i in range(len(lines)):
			f.write(lines[i])


if __name__ == "__main__":
	write_records('/etc/bind/zones/db.example.com')
