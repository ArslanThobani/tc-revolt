import numpy as np
from sklearn.linear_model import LinearRegression

# Generate synthetic dataset
np.random.seed(0)

X = np.array([[5.48813504, 2.3, 1.7, 8.9],
              [7.15189366, 3.1, 2.6, 5.4],
              [6.02763376, 1.5, 4.2, 6.7],
              [3.48813504, 2.3, 1.7, 1.9],
              [7.15189366, 3.1, 2.6, 5.4],
              [6.02763376, 1.5, 4.2, 0.7],
              [5.48813504, 2.3, 1.7, 8.9],
              [7.15189366, 6.1, 2.6, 5.4],
              [6.02763376, 1.5, 8.2, 1.7],
              [6.02763376, 1.5, 4.2, 2.7],
              [5.48813504, 3.3, 1.7, 8.9],
              [7.15189366, 3.1, 2.6, 5.4],
              [6.02763376, 1.5, 4.2, 6.7],
              [5.48813504, 6.3, 1.7, 8.9],
              [7.15189366, 3.1, 2.6, 5.4],
              [3.02763376, 1.5, 4.2, 6.7],
              [5.48813504, 2.3, 1.7, 8.9],
              [2.15189366, 3.1, 2.6, 5.4],
              [6.02763376, 1.5, 4.2, 6.7],
              [7.02763376, 1.5, 4.2, 6.7],])

y = [12.74032243,
     14.70394453, 
     13.0340055,   
     9.21716328, 
     16.17134531, 
     11.07798964,
     11.9263585,
     14.15243011,
     11.95204867,
     12.46586602,
     11.12031365,
     15.75806083,
     12.81630525, 
     11.0979451,  
     14.74765055, 
     6.38894185, 
     12.47034915, 
     4.09862906,
     12.36833522, 
     13.20117178]

print("Training parameters:")
print(X)
print("Training target variables:")
print(y)

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions on new data
# next 12 month for example
new_data = np.array([[5.3, 1.1, 2.4, 3.7],
                     [7.8, 2.2, 3.5, 4.8],
                     [9.1, 3.3, 4.6, 5.6],
                     [6.3, 1.4, 2.4, 3.7],
                     [7.1, 2.4, 3.5, 4.8],
                     [1.9, 3.3, 4.6, 5.9],
                     [4.3, 1.9, 2.4, 3.3],
                     [3.8, 2.8, 3.5, 2.8],
                     [8.1, 3.4, 4.6, 5.2],
                     [9.9, 3.6, 2.6, 4.9],
                     [4.5, 2.7, 4.9, 3.8],
                     [6.5, 3.1, 1.7, 5.3]])

predictions = model.predict(new_data)

# Print the coefficients and predictions
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:")
for prediction in predictions:
    print(prediction)
