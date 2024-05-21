def lambda_handler(event, context):
    body = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Our Online Bookstore</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: url('https://images.unsplash.com/photo-1707904437338-f43375a10d8a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed;
                background-size: cover;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 40px; /* Increased padding */
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border: 1px solid #ccc; /* Added border */
            }
            .container:hover {
                transform: translateY(-5px);
            }
            h1 {
                color: #007BFF;
                text-align: center;
                margin-bottom: 20px;
            }
            p {
                line-height: 1.6;
                margin-bottom: 15px;
            }
            img {
                display: block;
                margin: 20px auto;
                max-width: 90%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease-in-out;
            }
            img:hover {
                transform: scale(1.05);
            }
            .book-link {
                display: inline-block;
                padding: 10px 20px;
                background-color: #000; /* Changed background color to black */
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .book-link:hover {
                background-color: #333; /* Darker background color on hover */
                transform: translateY(-2px);
            }
            @keyframes spin {
                from {
                    transform: rotate(0deg);
                }
                to {
                    transform: rotate(360deg);
                }
            }
            .logo {
                display: block;
                width: 100px;
                height: 100px;
                margin: 20px auto;
                border-radius: 50%;
                background-image: url('https://i.ibb.co/vvRPKFZ/logo.png');
                background-size: cover;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                animation: spin 20s linear infinite;
            }
            @media only screen and (max-width: 600px) {
                .container {
                    padding: 15px;
                }
                img {
                    margin: 10px auto;
                    max-width: 80%;
                }
                .logo {
                    width: 80px;
                    height: 80px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo"></div>
            <h1>Welcome to Our Online Bookstore</h1>
            <p>Explore a wide range of books covering various genres and topics.</p>
            <a href="https://ibb.co/fDD6b68"><img src="https://i.ibb.co/LNNjMjQ/bookgenre.jpg" alt="bookgenre" style="max-width: 100%; border-radius: 12px;" /></a>
            <p>Check out some <a href="/prod/blog" class="book-link">books</a>.</p>
            <p>Stay tuned for upcoming posts where we'll delve deeper into these topics and more!</p>
        </div>
    </body>
    </html>'''
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html"},
        'body': body
    }
    return response
