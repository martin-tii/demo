from flask import Flask, render_template
import json
import pandas as pd
import time

app = Flask(__name__)

def read_topology():
    json_file = 'topology.json'

    try:
        with open(json_file) as f:
            topology = json.load(f)
        return topology
    except json.JSONDecodeError:
        print(f"Error: {json_file} does not contain valid JSON data.")
        return None

@app.route('/')
def index():
    # Define variables for the topology
    df = pd.read_csv('global_table.csv')

    # Read the topology data every 5 seconds
    topology = read_topology()
    highlighted_row_index = 99999
    for co in range(len(topology["nodes"])):
        color = topology["nodes"][co]["color"]
        if  color != "green":
            highlighted_row_index = co


    # Render the HTML template and pass in the topology data as arguments
    return render_template('index.html', nodes=topology['nodes'], edges=topology["edges"],  data=df, highlighted_row_index=highlighted_row_index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
