import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare sample training data (X = input hours studied, y = exam score)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 60, 70, 80, 90])

# 2. Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# 3. Predict score for 6 hours of study
hours = [[6]]
predicted_score = model.predict(hours)

print(f"Predicted score for studying 6 hours: {predicted_score[0]:.2f}")