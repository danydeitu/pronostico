from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pronostico', methods=['POST'])
def pronostico():
    ciudad = request.form.get('ciudad')
    command = f'C:/Python310/python.exe c:/Users/miria/pronostico/weather_app.py {ciudad}'
    resultado = subprocess.check_output(command, shell=True, text=True)
    return resultado

if __name__ == '__main__':
    app.run(debug=True)
