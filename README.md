🏡 Bangalore House Price Predictor

This web application predicts the price of a house in Bangalore based on user inputs such as location, BHK (bedrooms), number of bathrooms, and total square footage. It uses machine learning models including Linear Regression, Lasso Regression, and Ridge Regression (final model selected).

🚀 Features

Accurate price prediction based on historical housing data
Clean web interface using Bootstrap
Built with Flask for backend and AJAX for real-time results
Uses cleaned and preprocessed housing data
Trained and tested with multiple regression models

🧠 Machine Learning Models Used

The project explores and compares:
✅ Linear Regression
✅ Lasso Regression
✅ Ridge Regression (Selected for deployment due to best generalization performance)

🖼️ Screenshots

🔹 Home Page
![Screenshot 2025-05-07 164407](https://github.com/user-attachments/assets/d3fc0bb7-619a-4c4e-b448-c5618c32683f)

🔹 Prediction Output
![Screenshot 2025-05-07 164455](https://github.com/user-attachments/assets/97da33b1-4289-44b0-8893-c8acae38da27)

📁 Project Structure
.
├── Bengaluru_House_Data.csv       # Original raw dataset
├── Cleaned_data.csv               # Preprocessed and cleaned dataset
├── Predictor.ipynb                # Jupyter notebook: EDA, preprocessing, training
├── RidgeModel.pkl                 # Trained Ridge Regression model
├── main.py                        # Flask app with endpoints
├── templates/
│   └── index.html                 # Frontend HTML page
├── static/                        # For custom styles/scripts (optional)
├── Screenshot 2025-05-07 164407.png
├── Screenshot 2025-05-07 164455.png
└── README.md

🧪 How to Run Locally

Step 1: Clone the repository
git clone https://github.com/yourusername/bangalore-house-price-predictor.git
cd bangalore-house-price-predictor

Step 2: Install dependencies
pip install -r requirements.txt

Example requirements.txt:
flask
pandas
numpy
scikit-learn

Step 3: Run the app
python main.py

Step 4: Open in browser
Go to: http://localhost:5001

💻 How It Works

User fills in form details: location, BHK, bathrooms, square footage
Data is sent to Flask backend via AJAX
Trained Ridge Regression model predicts the price
Result is dynamically shown on the same page in ₹

📊 Example Prediction

Location	BHK	Bathrooms	Sqft	Predicted Price
6th Phase JP Nagar	4	3	2000	₹14,352,010.74

🙌 Acknowledgements

Kaggle Housing Dataset
Flask
Bootstrap

🙋‍♂️ Author

Malla Anant 📧 mallaanant2003@gmail.com

⭐️ Show Your Support If you like this project, give it a ⭐ on GitHub!
