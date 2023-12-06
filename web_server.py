import os
from flask import Flask, jsonify, request, render_template, send_from_directory
from util.file_walk import file_walk

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/start', methods=['GET'])
def start():
    n = request.args.get('n')
    AS7341 = request.args.get('AS7341')
    AS7262 = request.args.get('AS7262')
    AS7265x = request.args.get('AS7265x')

    sensors_to_run = []
    n_run = 1 if n == '' else int(n)
    sensors_to_run.append('AS7341') if AS7341 == '1' else None
    sensors_to_run.append('AS7262') if AS7262 == '1' else None
    sensors_to_run.append('AS7265x') if AS7265x == '1' else None

    sensors_shell = ','.join(sensors_to_run)

    os.system(f'python3 main.py -n {n_run} --sensor {sensors_shell}')

    return 'started'


@app.route('/api/files', methods=['GET'])
def get_files():
    files = file_walk('data')
    files_json = jsonify(files)

    return files_json


@app.route('/api/download/<path:filename>')
def download_file(filename):
    directory = 'data'

    return send_from_directory(directory, filename, as_attachment=True)


@app.route('/api/file/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    os.remove(f'data/{filename}')

    return 'deleted'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
