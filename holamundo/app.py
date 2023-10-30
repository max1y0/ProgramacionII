from flask import *

app = Flask(__name__)

hola = "hola mundo"

@app.route('/')
def index():
    return render_template('index.html', hola=hola)

if __name__ == '__main__':
    app.run(debug=True)