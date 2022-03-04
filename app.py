from flask import *

app = Flask(__name__)  # creating the Flask class object


# @app.route('/')  # decorator drfines the
# def home():
#     return "hello, this is our first flask website";

@app.route('/')
def message():
      return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)