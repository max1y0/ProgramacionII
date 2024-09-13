from flask import *
from tamagotchi import *

app = Flask(__name__)

bicho = Tamagotchi(30,30,30)


@app.route('/')
def index():
    return render_template('index.html', hambre=bicho.hambre, salud=bicho.salud, higiene=bicho.higiene)

@app.route('/comida')
def comida():
    global bicho
    bicho.alimentar()
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
