from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Replace 'YOUR_API_ENDPOINT' with your actual API Gateway endpoint URL
API_ENDPOINT = 'YOUR_API_ENDPOINT'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's input number from the form
        user_number = int(request.form['user_number'])

        # Send a POST request to your Lambda function API endpoint
        response = requests.post(API_ENDPOINT, json={'number': user_number})
        data = response.json()

        # Display the result from the Lambda function on the webpage
        result_message = data['message']
        return render_template('result.html', result=result_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
