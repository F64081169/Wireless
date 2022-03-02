import matplotlib.pyplot as plt

Q1_BEST_EFFORT = 1901
Q1_BEST_ENTROPY = 47
Q1_MINIMUM = 1130
Q1_MY = 2690

Q1 = [Q1_BEST_EFFORT,Q1_BEST_ENTROPY,Q1_MINIMUM,Q1_MY]

Q2_BEST_EFFORT = 294
Q2_BEST_ENTROPY= 12
Q2_MINIMUM = 162
Q2_MY = 351
line = plt.plot(Q1)
plt.title("TOTAL SWITCH")
plt.ylabel("times")
plt.xlabel("algorithm:BEST_EFFORT,ENTROPY,MINIMUM,My_Algo")
plt.setp(line,marker = "o") 
plt.show()

Q2 = [Q2_BEST_EFFORT,Q2_BEST_ENTROPY,Q2_MINIMUM,Q2_MY]
line2 = plt.plot(Q2)
plt.title("TOTAL SWITCH")
plt.ylabel("times")
plt.xlabel("algorithm:BEST_EFFORT,ENTROPY,MINIMUM,My_Algo")
plt.setp(line2,marker = "o") 
plt.show()