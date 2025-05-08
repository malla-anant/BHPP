import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load cleaned data and trained model
data = pd.read_csv('Cleaned_data.csv')
model = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route('/')
def index():
    # Pass unique locations to the template
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        location = request.form.get('location')
        bhk = int(request.form.get('bhk') or 0)
        bath = int(request.form.get('bath') or 0)
        sqft = float(request.form.get('total_sqft') or 0)

        # Prepare input for model
        input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                                columns=['location', 'total_sqft', 'Bath', 'BHK'])

        # Make prediction
        prediction = model.predict(input_df)[0] * 1e5  # Convert lakhs to rupees

        return jsonify({'prediction': f"₹{prediction:,.2f}"})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)
