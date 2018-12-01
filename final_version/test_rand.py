import random
import math

def check_randomness(sequence_list):
	avg_sequence = sum(sequence_list)/len(sequence_list)
	binary_sequence_list = []
	for item in sequence_list:
		if item>=avg_sequence: binary_sequence_list.append(1)
		else: binary_sequence_list.append(0)
	n1 = sum(binary_sequence_list)
	n0 = len(binary_sequence_list)-n1
	n = n0 + n1
	R = 1
	index_zero = binary_sequence_list[0]
	for i in range(1,n):
		if binary_sequence_list[i] != index_zero:
			R += 1
			index_zero = binary_sequence_list[i]
	meanR = ((2*n0*n1)/n)+1	#based the test formula (see Wikipedia for 'Runs Test')
	varienceR = ((meanR-1)*(meanR-2))/(n-1)
	stddevR = math.sqrt(varienceR)
	Z = (R-meanR)/(stddevR)
	if abs(Z)>1.96: return(1)
	else: return(-1)
	return(Z)


c = list(range(100,1000000))
d = random.sample(c,1500)
print(check_randomness(d))
