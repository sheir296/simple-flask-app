from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Train a simple model
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(np.array([data['input']]).reshape(-1, 1))
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
