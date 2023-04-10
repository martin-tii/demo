import subprocess
import json

def get_macs():
    macs = []
    proc = subprocess.Popen(['batctl', 'n'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i, x in enumerate(proc.stdout, start=1):
        if i > 2:
            aux = x.split()
            macs.append(aux[1].decode("utf-8"))
    return macs

def get_my_mac_address(interface='wlp1s0'):
    output = subprocess.check_output(['ifconfig', interface])
    for line in output.split(b'\n'):
        if b'ether ' in line:
            mac_address = line.split()[1]
            return mac_address.decode('utf-8')
    return None


macs = get_macs()
my_mac = get_my_mac_address()
macs.append(my_mac)
nodes = []
edges = []
colors = []
for i, mac in enumerate(macs):
    node = {"id": mac, "label": mac, "color": 'green'}
    nodes.append(node)
    if i > 0:
        edge = {"from": macs[0], "to": mac, "label": "mesh"}
        edges.append(edge)


data = {"nodes": nodes, "edges": edges}

json_data = json.dumps(data)
print(json_data)

# Write JSON data to a file
with open("topology.json", "w") as json_file:
    json_file.write(json_data)
