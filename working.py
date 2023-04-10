from flask import Flask, render_template
import json
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    # Define variables for the topology
    df = pd.read_csv('global_table.csv')
    json_file = 'topology.json'

    try:
        with open(json_file) as f:
            topology = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {json_file} does not contain valid JSON data.")

    print(topology["nodes"])
    # Render the HTML template and pass in the topology data as arguments
    return render_template('index.html', nodes=topology['nodes'], edges=topology["edges"],  data=df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
