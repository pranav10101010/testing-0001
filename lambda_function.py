import random

def generate_random_number():
    return random.randint(1, 100)

# Example usage
random_number = generate_random_number()
print(f'Random number: {random_number}')


        # Display the result from the Lambda function on the webpage
        result_message = data['message']
        return render_template('result.html', result=result_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
