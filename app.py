from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import json

app = Flask(__name__)

# Se realiza la carga del json con toda la informacion de las vulnerabilidades 
with open('vulnerabilities.json') as f:
    data = json.load(f)

# Funcion para la apertura de la pagina principal
@app.route('/')
def index():
    return render_template('base.html')

# Funcion para listar todas las vulnerabilidades
@app.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    return render_template('vulnerabilities.html', vulnerabilities=data['vulnerabilities'])

# Funcion que muestra una vulnerabilidad especifica por su ID
@app.route('/vulnerabilities/<int:vulnerability_id>', methods=['GET'])
def get_vulnerability(vulnerability_id):
    vulnerability = next((v for v in data['vulnerabilities'] if v['id'] == vulnerability_id), None)
    if vulnerability is None:
        abort(404)
    return render_template('vulnerability.html', vulnerability=vulnerability)

# Funcion para agregar una nueva vulnerabilidad
@app.route('/vulnerabilities/add', methods=['GET', 'POST'])
def add_vulnerability():
    if request.method == 'POST':
        new_vulnerability = {
            'id': data['vulnerabilities'][-1]['id'] + 1,
            'name': request.form['name'],
            'description': request.form.get('description', ""),
            'impact': request.form.get('impact', ""),
            'remediation': request.form.get('remediation', ""),
            'mitre': request.form.get('mitre', "")
        }
        data['vulnerabilities'].append(new_vulnerability)
        with open('vulnerabilities.json', 'w') as f:
            json.dump(data, f, indent=4)
        return redirect(url_for('get_vulnerabilities'))

    return render_template('add_vulnerability.html')

# Funcion para eliminar vulnerabilidades del archivo json
@app.route('/vulnerabilities/<int:vulnerability_id>/delete', methods=['POST'])
def delete_vulnerability(vulnerability_id):
    vulnerability = next((v for v in data['vulnerabilities'] if v['id'] == vulnerability_id), None)
    if vulnerability is None:
        abort(404)
    data['vulnerabilities'].remove(vulnerability)
    with open('vulnerabilities.json', 'w') as f:
        json.dump(data, f, indent=4)
    return redirect(url_for('get_vulnerabilities'))

if __name__ == '__main__':
    app.run(debug=True)