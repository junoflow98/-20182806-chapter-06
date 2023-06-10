import matplotlib.pyplot as plt

황제펭귄_length = [90, 98, 85, 83, 73, 97, 93, 80]
황제펭귄_height = [36.2, 39.1, 30.4, 33.6, 22.9, 37.3, 34.2, 31.1]
젠투펭귄_length = [55, 65, 67, 78, 81, 83, 63, 77]
젠투펭귄_height = [9.6, 10.7, 8.9, 16.3, 18.0, 17.3, 5.9, 16.1]
바위뛰기펭귄_length = [44, 48, 58, 41, 46, 57, 41, 45]
바위뛰기펭귄_height = [3.5, 4.1, 4.9, 3.0, 4.8, 5.3, 3.6, 3.8]

plt.scatter(황제펭귄_length, 황제펭귄_height, c='r', label='황제펭귄 Group')
plt.scatter(젠투펭귄_length, 젠투펭귄_height, c='r', label='젠투펭귄 Group')
plt.scatter(바위뛰기펭귄_length, 바위뛰기펭귄_height,c='바위뛰기펭귄',marker='^', label='바위뛰기펭귄 Group')

plt.xlabel('Length')
plt.ylabel('Height')
plt.title("Group Size")
plt.legend(loc='upper right')

newdata_length = [59]
newdata_height = [35]

plt.scatter(newdata_length, newdata_height, s=100, marker='p', c='g', label='new Data')