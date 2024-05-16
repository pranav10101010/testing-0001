def lambda_handler(event, context):
    body = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homepage</title>
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
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease-in-out;
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
            .blog-link {
                display: inline-block;
                padding: 10px 20px;
                background-color: #007BFF;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .blog-link:hover {
                background-color: #0056B3;
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
                margin: 20px auto;
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
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://i.ibb.co/m4PNrG8/devopslogo.jpg" alt="DevOps Logo" class="logo" />
            <h1>Home</h1>
            <p>Hi! My name is Pranav. Welcome to my website.</p>
            <p>I'm passionate about DevOps, a set of practices that combines software development (Dev) and IT operations (Ops) to shorten the systems development life cycle and provide continuous delivery with high software quality.</p>
            <img src="https://i.ibb.co/q5PDgNy/2202-i402-018-S-m004-c13-Devops-engineer-flat-composition.jpg" alt="DevOps Engineer" style="max-width: 100%; border-radius: 12px;" />
            <p>Feel free to share!</p>
            <p>Check out some <a href="/development/blog" class="blog-link">DevOps questions</a>.</p>
            <img src="https://media.giphy.com/media/3oEjHTXfh8Qa2o5E3u/giphy.gif" alt="Rotating Earth" />
        </div>
    </body>
    </html>'''
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html"},
        'body': body
    }
    return response


