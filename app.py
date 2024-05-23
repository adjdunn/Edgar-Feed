from flask import Flask, jsonify, render_template
from main import get_feed 
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)



@app.route('/api/data')
def get_data():
    data = get_feed()
    print(data)
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)