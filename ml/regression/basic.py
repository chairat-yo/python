import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

x_data = [1.0, 1.8, 3.0, 4.1, 5.2, 6.0]
y_data = [1, 1.3, 2.2, 2.5, 2.8, 3.6]

x = np.array(x_data)
y = np.array(y_data)

# plt.scatter(x, y)
# plt.grid()
# plt.show() #show data relationship

x = x.reshape(-1, 1) #reshape to matrix, vertical x (col)
print(x)

#Model & Train
model = LinearRegression()
model.fit(x, y) #train

#Predict
new_input = 2.5
y_predict = model.predict(x)

print("Predict y when x = ",new_input, model.predict([[new_input]]))
print("model score:", model.score(x, y))
print("r2_score: ", r2_score(y, y_predict))