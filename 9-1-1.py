import matplotlib.pyplot as plt

A_length = [55, 57, 64, 63, 58, 49, 54, 61]
A_height = [30, 31, 36, 30, 33, 25, 37, 34]
B_length = [56, 47, 56, 46, 49, 53, 52, 48]
B_height = [52, 52, 50, 53, 50, 53, 49, 54]

plt.scatter(A_length, A_height, c='r', label='A Group')
plt.scatter(B_length, B_height,c='b',marker='^', label='B Group')

plt.xlabel('Length')
plt.ylabel('Height')
plt.title("Group Size")
plt.legend(loc='upper right')

newdata_length = [52]
newdata_height = [42]

plt.scatter(newdata_length, newdata_height, s=100, marker='p', c='g', label='new Data')