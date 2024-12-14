from flask import Flask, request, jsonify, render_template
import networkx as nx
import random

app = Flask(__name__)

# Example graph (replace with your own graph or load from file)
G = nx.Graph()

# Add nodes (cities instead of numeric node IDs)
cities = [
    "Agiripalli", "Avanigadda", "Challapalli", "Gannavaram", "Gudivada", "Gudlavalleru",
    "Jaggayyapeta", "Kankipadu", "Koduru", "Kondapalli", "Machilipatnam", "Movva", 
    "Mudinepalli", "Nandigama", "Nuzvid", "Pamarru", "Pedana", "Penamaluru", 
    "Thotlavalluru", "Tiruvuru", "Vuyyuru", "Vissannapet", "Ibrahimpatnam", "Paritala", 
    "Kaikaluru", "Mandavalli", "Bantumilli", "Kruthivennu", "Kalidindi", "Mopidevi", 
    "Nagayalanka", "Veerullapadu", "Vijayawada (Rural)", "Kanchikacherla", "Mopidevi", 
    "Pamidimukkala", "Avutapalli Peda", "Avutapalli Machilipatnam (Rural)", "Edupugallu", 
    "Kanuru", "Ramavarappadu", "Tadanki", "Gollapudi", "Gunadala", "Penuganchiprolu", 
    "Musunuru", "Vallurupalem", "Pedaprolu"
]

# Add some random edges with random weights
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        if random.random() < 0.3:  # 30% chance of an edge
            weight = random.randint(1, 10)  # Random weight
            G.add_edge(cities[i], cities[j], weight=weight)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html', cities=cities)

# Endpoint to find the shortest path between source and destination cities
@app.route('/find_shortest_path', methods=['POST'])
def find_shortest_path():
    data = request.get_json()
    source = data.get('source')
    destination = data.get('destination')

    # Validate if the source and destination cities are in the graph
    if source not in G.nodes or destination not in G.nodes:
        return jsonify({'error': 'Source or Destination city not found in the graph'}), 400

    # Try to find the shortest path
    try:
        path = nx.shortest_path(G, source=source, target=destination, weight='weight')
        distance = nx.shortest_path_length(G, source=source, target=destination, weight='weight')
        return jsonify({'path': path, 'distance': distance})  # Return the path and distance as JSON
    except nx.NetworkXNoPath:
        return jsonify({'error': 'No path exists between the source and destination cities'}), 404

if __name__ == "__main__":
    app.run(debug=True)
