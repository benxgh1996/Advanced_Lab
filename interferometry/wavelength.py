import numpy
import math

f = open("wl_data.csv", "r")

lines = f.readline()
f.close()

data = []
single_data_list = lines.split("\r")
for line in single_data_list:
	single_data = line.split(",")
	data.append([single_data[0], single_data[1]])
data[0][0] = "0"

data_final = []
for single_data in data:
	data_final.append((float(single_data[0]), float(single_data[1])))
data = data_final

SEQ_LENGTH = 24
print("sequence length is: ", SEQ_LENGTH)
data_group = []
i = 0
s = 0
group_number = 0
for single_data in data:
	s += single_data[1]
	if i % SEQ_LENGTH == SEQ_LENGTH - 1:
		# data_group will have elements in form of [group number, first index in a group, group sum]
		data_group.append([group_number, group_number * SEQ_LENGTH, s])
		group_number += 1
		s = 0
	i += 1

print("Length of data_group: ", len(data_group))
# print(data_group)
minimums = []

# isAmbiguous = False
# for i in range(len(data_group) - 1):
# 	if data_group[i][2] == data_group[i + 1][2]:
# 		print("Ambiguity at: ", data_group[i], data_group[i + 1])
# 		isAmbiguous = True
# if not isAmbiguous:
# 	print("No ambiguity.")

for i in range(1, len(data_group) - 1):
	if data_group[i][2] < -0.8 * SEQ_LENGTH:
		if data_group[i][2] <= data_group[i - 1][2] and data_group[i][2] <= data_group[i + 1][2]:
			minimums.append(data_group[i])
			if data_group[i][2] == data_group[i - 1][2] or data_group[i][2] == data_group[i + 1][2]:
				print("ambiguity at: ", data_group[i - 1], data_group[i], data_group[i + 1])

print("Number of minimums is: ", len(minimums))

# i = 0
# for group in minimums:
# 	i += 1
# 	print(i, group[1] + SEQ_LENGTH / 2),

# print data_group[minimums[19][0] - 1], data_group[minimums[19][0]], data_group[minimums[19][0] + 1]
# print data_group[minimums[26][0] - 1], data_group[minimums[26][0]], data_group[minimums[26][0] + 1]

min_times = []
for minimum in minimums:
	min_times.append(minimum[1] * 0.001 + SEQ_LENGTH * 0.001 / 2)
	

def getStandardDeviation(min_times, standard):
	intervals = []
	for i in range(1, len(min_times)):
		intervals.append(min_times[i] - min_times[i - 1])
	print(len(intervals))
	print(intervals)
	print "Original STD: ", numpy.std(intervals)
	for i in range(len(intervals)):
		intervals[i] -= standard
		intervals[i] **= 2
	return "Standard deviation:" + str(math.sqrt(sum(intervals)/float(len(intervals))))
		
print getStandardDeviation(min_times, 0.409788)
# f = open("wl_out.csv", "w")
# for i in range(len(minimums)):
# 	f.write(str(i + 1) + "," + str(min_times[i]) + "\n")
# f.close()




