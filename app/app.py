from flask import Flask, jsonify, render_template, request
import sqlite3
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "testforge.db"

app = Flask(__name__, template_folder="templates")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
    """)

    conn.execute(
        "INSERT OR IGNORE INTO users(email, password) VALUES (?, ?)",
        ("test@example.com", "Test@123")
    )

    products = [
        ("Wireless Mouse", 799.0),
        ("Mechanical Keyboard", 2499.0),
        ("USB-C Hub", 1499.0),
    ]

    for name, price in products:
        conn.execute(
            "INSERT OR IGNORE INTO products(name, price) VALUES (?, ?)",
            (name, price)
        )

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")

    conn = get_db()
    user = conn.execute(
        "SELECT id, email FROM users WHERE email=? AND password=?",
        (email, password)
    ).fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({
        "message": "Login successful",
        "token": secrets.token_hex(16),
        "user": {"id": user["id"], "email": user["email"]}
    }), 200


@app.get("/api/products")
def products():
    conn = get_db()
    rows = conn.execute(
        "SELECT id, name, price FROM products ORDER BY id"
    ).fetchall()
    conn.close()

    return jsonify([
        {"id": row["id"], "name": row["name"], "price": row["price"]}
        for row in rows
    ])


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
