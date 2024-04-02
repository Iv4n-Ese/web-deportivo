from flask import Flask, render_template, redirect, url_for, flash


app = Flask (__name__)



@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/nosotros')
def Nosotros():
    return render_template('nosotros.html')

@app.route('/planes')
def Planes():
    return render_template('planes.html')

@app.route('/horarios')
def Horarios():
    return render_template('horarios.html')
    
@app.route('/consejos')
def Consejos():
    return render_template('consejos.html')

if __name__ == '__main__':
    app.run(port = 3050, debug = True)