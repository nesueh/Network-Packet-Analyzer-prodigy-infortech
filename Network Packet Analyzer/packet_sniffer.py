from scapy.all import sniff
from flask import Flask, render_template, jsonify

app = Flask(__name__)
packets = []

def packet_callback(packet):
    packet_info = {
        'src': packet[0][1].src,
        'dst': packet[0][1].dst,
        'proto': packet[0][1].proto,
        'payload': str(packet[0][1].payload)
    }
    packets.append(packet_info)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packets')
def get_packets():
    return jsonify(packets)

if __name__ == '__main__':
    sniff(prn=packet_callback, store=0)
    app.run(debug=True)
