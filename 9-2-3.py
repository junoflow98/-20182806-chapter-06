import matplotlib.pyplot as plt

황제펭귄_length = [90, 98, 85, 83, 73, 97, 93, 80]
황제펭귄_height = [36.2, 39.1, 30.4, 33.6, 22.9, 37.3, 34.2, 31.1]
젠투펭귄_length = [55, 65, 67, 78, 81, 83, 63, 77]
젠투펭귄_height = [9.6, 10.7, 8.9, 16.3, 18.0, 17.3, 5.9, 16.1]
바위뛰기펭귄_length = [44, 48, 58, 41, 46, 57, 41, 45]
바위뛰기펭귄_height = [3.5, 4.1, 4.9, 3.0, 4.8, 5.3, 3.6, 3.8]

d_data = np.column_stack((dach_length, dach_height))
d_label = np.zeros(len(d_data))
j_data = np.column_stack((jin_length, jin_height))
j_label = np.ones(len(j_data))

groups = np.concatenate((d_data, j_data))
labels = np.concatenate((d_label, j_label))

group_classes = {0:'황제펭귄', 1:'젠투펭귄', 2:'바위뛰기펭귄'}

print('iris 데이터의 레이블:', iris.target)