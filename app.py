from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return('''
        <html>
            <head>
                <title> Dog Breed Identifier </title>
            </head>
            <body>
                <h1> Dog Breed Identifier </h1>
                <p> This app identifies images. It can distinguish between 1) human, dog and other and 2) dog breed </p>
                <p> Please paste path to an image below and press run... </p> 

                <form action="/result" method="GET"> <input name="text"><input type="submit" value="RUN"></form>
            </body>
        </html>
    ''')



@app.route("/result")
def result():
    result = request.args.get('text', '')

    return("The result is: " + result * 2)


if __name__ == "__main__":
    app.run()
