from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# 模擬資料庫
messages_db = []


@app.route("/")
def index():
  """首頁：包含簡單的輸入介面供 E2E 測試使用"""
  html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker 微服務系統儀表板</title>
    </head>
    <body>
        <h1>HW7 測試儀表板</h1>
        <input type="text" id="msgInput" placeholder="請輸入訊息...">
        <button onclick="submitMsg()">送出</button>
        <ul id="msgList">
            {% for m in messages %}
                <li>{{ m }}</li>
            {% endfor %}
        </ul>
        <script>
            function submitMsg() {
                const val = document.getElementById('msgInput').value;
                fetch('/api/messages', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({content: val})
                }).then(res => location.reload());
            }
        </script>
    </body>
    </html>
    """
  return render_template_string(html, messages=messages_db)


@app.route("/api/messages", methods=["GET", "POST"])
def api_messages():
  """Web API 路由"""
  if request.method == "POST":
    data = request.get_json()
    content = data.get("content", "")
    messages_db.append(content)
    return jsonify({"status": "success", "content": content}), 201
  return jsonify(messages_db)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)