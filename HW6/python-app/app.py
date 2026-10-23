import os
from flask import Flask, jsonify, render_template, request
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASS = os.getenv("DB_PASS", "mypassword")


def get_db_connection():
  return psycopg2.connect(
      host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
  )


def init_db():
  try:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()
    cur.close()
    conn.close()
  except Exception as e:
    print(f"DB init error: {e}")


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/api/messages", methods=["GET"])
def get_messages():
  try:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, content, created_at FROM messages ORDER BY created_at DESC;"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"id": r[0], "content": r[1], "created_at": str(r[2])} for r in rows
    ])
  except Exception as e:
    return jsonify({"error": str(e)}), 500


@app.route("/api/messages", methods=["POST"])
def add_message():
  data = request.get_json()
  content = data.get("content")
  if not content:
    return jsonify({"error": "Content required"}), 400
  try:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (content) VALUES (%s) RETURNING id;", (content,)
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "content": content, "status": "success"}), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
  init_db()
  app.run(host="0.0.0.0", port=5000)