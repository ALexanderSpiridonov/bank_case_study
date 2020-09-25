import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# load the model
model = pickle.load(open('catboost.ai', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])  # 
def upload():
    file = request.files['inputFile']
    data = pd.read_csv(file, index_col=0)
    le = LabelEncoder()
    X = data.copy()
    dtps = X.dtypes
    # not numeric values
    nonnumericcols = dtps[dtps == 'object'].index
    # label incode
    for col in nonnumericcols:
        X[col] = le.fit_transform(df[col])
    
    # load the scaler
    # scaler = load(open('scaler.pkl', 'rb'))
    # X = scaller.transform(X)

    predictions = model.predict(X)
    predictions_table = pd.DataFrame(predictions, columns = ['Predicted results'])

    return predictions_table.to_html()

if __name__ == "__main__":
    app.run(debug=True)