from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit()

# Route to handle GET and POST requests for items
@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        name = request.json['name']
        with sqlite3.connect('database.db') as conn:
            conn.execute('INSERT INTO items (name) VALUES (?)', (name,))
            conn.commit()
        return jsonify({'status': 'Item added'}), 201
    else:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.execute('SELECT * FROM items')
            items = cursor.fetchall()
        return jsonify(items)

# Route to handle GET, PUT, DELETE requests for specific items
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        with sqlite3.connect('database.db') as conn:
            cursor = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,))
            item = cursor.fetchone()
            return jsonify(item) if item else ('Not Found', 404)

    elif request.method == 'PUT':
        name = request.json['name']
        with sqlite3.connect('database.db') as conn:
            conn.execute('UPDATE items SET name = ? WHERE id = ?', (name, item_id))
            conn.commit()
        return jsonify({'status': 'Item updated'})

    elif request.method == 'DELETE':
        with sqlite3.connect('database.db') as conn:
            conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
            conn.commit()
        return jsonify({'status': 'Item deleted'})

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True,port=0000)  # Start the Flask application