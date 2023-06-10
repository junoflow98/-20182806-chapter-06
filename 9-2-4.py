import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

A_length = [55, 57, 64, 63, 58, 49, 54, 61]
A_height = [30, 31, 36, 30, 33, 25, 37, 34]
B_length = [56, 47, 56, 46, 49, 53, 52, 48]
B_height = [52, 52, 50, 53, 50, 53, 49, 54]
C_length = [56, 47, 56, 46, 49, 53, 52, 48]
C_height = [52, 52, 50, 53, 50, 53, 49, 54]
D_length = [56, 47, 56, 46, 49, 53, 52, 48]
D_height = [52, 52, 50, 53, 50, 53, 49, 54]
E_length = [56, 47, 56, 46, 49, 53, 52, 48]
E_height = [52, 52, 50, 53, 50, 53, 49, 54]

d_data = np.column_stack((dach_length, dach_height))
d_label = np.zeros(len(d_data))
j_data = np.column_stack((jin_length, jin_height))
j_label = np.ones(len(j_data))

newdata1 = [[60, 40]]
newdata2 = [[40, 29]]
newdata3 = [[55, 42]]
newdata4 = [[39, 45]]
newdata5 = [[65, 59]]

groups = np.concatenate((d_data, j_data))
labels = np.concatenate((d_label, j_label))

group_classes = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}

print('n_neighbor = 1인 경우')
n_neighbor = 1
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(group, labels)
y_pred = knn.predict(newdata1)
print('데이터', newdata1, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata2)
print('데이터', newdata2, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata3)
print('데이터', newdata3, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata4)
print('데이터', newdata4, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata5)
print('데이터', newdata5, ', 판정 결과:', group_classes[y_pred[0]])

print('n_neighbor = 2인 경우')
n_neighbor = 2
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(group, labels)
y_pred = knn.predict(newdata1)
print('데이터', newdata1, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata2)
print('데이터', newdata2, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata3)
print('데이터', newdata3, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata4)
print('데이터', newdata4, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata5)
print('데이터', newdata5, ', 판정 결과:', group_classes[y_pred[0]])

print('n_neighbor = 3인 경우')
n_neighbor = 3
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(group, labels)
y_pred = knn.predict(newdata1)
print('데이터', newdata1, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata2)
print('데이터', newdata2, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata3)
print('데이터', newdata3, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata4)
print('데이터', newdata4, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata5)
print('데이터', newdata5, ', 판정 결과:', group_classes[y_pred[0]])

print('n_neighbor = 4인 경우')
n_neighbor = 4
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(group, labels)
y_pred = knn.predict(newdata1)
print('데이터', newdata1, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata2)
print('데이터', newdata2, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata3)
print('데이터', newdata3, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata4)
print('데이터', newdata4, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata5)
print('데이터', newdata5, ', 판정 결과:', group_classes[y_pred[0]])

print('n_neighbor = 5인 경우')
n_neighbor = 5
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(group, labels)
y_pred = knn.predict(newdata1)
print('데이터', newdata1, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata2)
print('데이터', newdata2, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata3)
print('데이터', newdata3, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata4)
print('데이터', newdata4, ', 판정 결과:', group_classes[y_pred[0]])
y_pred = knn.predict(newdata5)
print('데이터', newdata5, ', 판정 결과:', group_classes[y_pred[0]])