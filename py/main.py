# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/greet', methods=['POST'])
# def greet():
#     name = request.form.get('name')
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, Stranger!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)





# from flask import Flask
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return f"""
#     <html>
#         <head>
#             <title>Hello World with Date and Time</title>
#         </head>
#         <body>
#             <h1>Hello, World from Google App Engine!</h1>
#             <p>Current Date and Time: {current_time}</p>
#         </body>
#     </html>
#     """

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)








# from flask import Flask
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return f"""
#     <html>
#         <body style="text-align: center; background-color: #f0f0f0; padding: 50px;">
# 			<h1 style="color: #333;">Hello, World from Google App Engine!</h1>
#             <h1 style="color: #333; margin-top: 20px; border: 1px solid #333; padding: 10px;">Hello world</h1>
#         </body>
#     </html>
#     """

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)