from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import yaml

# Load MySQL configuration from YAML file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)["mysql"]

app = Flask(__name__)
app.config["MYSQL_HOST"] = config["host"]
app.config["MYSQL_USER"] = config["user"]
app.config["MYSQL_PASSWORD"] = config["password"]
app.config["MYSQL_DB"] = config["database"]

mysql = MySQL(app)

@app.route('/health')
def health_check():
    return jsonify({'status': 'ok'})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the demo app"})


@app.route("/users", methods=["GET"])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()
    users = []
    for row in rows:
        user = {"id": row[0], "name": row[1], "email": row[2]}
        users.append(user)
    cur.close()
    return jsonify(users)


@app.route("/users", methods=["POST"])
def add_user():
    name = request.json["name"]
    email = request.json["email"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User added successfully"})


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({"message": "User not found"}), 404
    user = {"id": row[0], "name": row[1], "email": row[2]}
    cur.close()
    return jsonify(user)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    name = request.json["name"]
    email = request.json["email"]
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User updated successfully"})


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)

