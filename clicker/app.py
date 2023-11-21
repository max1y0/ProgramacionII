from flask import *
import threading
import time

app = Flask(__name__)

panchos = 23
carritos = 0

#completar
@app.route('/')
def index():
    return render_template('index.html', panchos=panchos, carritos=carritos)

@app.route('/click')
def click_pancho():
    global panchos
    panchos += 1
    return redirect(url_for('index'))

@app.route('/comprar_carrito')
def comprar_carrito():
    global panchos, carritos
    if panchos >= 15:
        panchos -= 15
        carritos += 1
    return redirect('/')

def cursor():
    global panchos, carritos
    while True:
        time.sleep(1)
        panchos += carritos * 1

if __name__ == '__main__':
    auto_clicker_thread = threading.Thread(target=cursor)
    auto_clicker_thread.daemon = True
    auto_clicker_thread.start()
    app.run(debug=True)