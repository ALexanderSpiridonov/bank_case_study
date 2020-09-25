import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])  # 
def upload():
    file = request.files['inputFile']
    
    data = pd.read_csv(file, index_col=0)

    return data.to_html()

if __name__ == "__main__":
    app.run(debug=True)