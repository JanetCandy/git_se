from js import Response, Headers, JSON

async def on_fetch(request, env):
    url = request.url
    method = request.method
    
    # API 路由範例：/api/hello
    if "/api/hello" in url:
        data = {
            "status": "success",
            "message": "Hello from Python Worker on Cloudflare!",
            "method": method
        }
        headers = Headers.new({"content-type": "application/json; charset=utf-8"})
        return Response.new(JSON.stringify(data), headers=headers)
        
    # API 路由範例：/api/info
    if "/api/info" in url:
        info = {
            "app_name": "Cloudflare Python App",
            "week": 9,
            "runtime": "Pyodide / Cloudflare Workers Python"
        }
        headers = Headers.new({"content-type": "application/json; charset=utf-8"})
        return Response.new(JSON.stringify(info), headers=headers)

    # 預設回傳 HTML 前端頁面
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cloudflare Python App - 第9週作業</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }
            .card { border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            button { background-color: #f6821f; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
            button:hover { background-color: #e06d10; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 4px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Cloudflare Python 網站應用</h1>
            <p>這是部署在 Cloudflare 上的 Python Worker 應用程式。</p>
            <button onclick="fetchApi()">測試 API 請求 (/api/hello)</button>
            <h3>API 回傳結果：</h3>
            <pre id="output">點擊上方按鈕測試...</pre>
        </div>

        <script>
            async function fetchApi() {
                const res = await fetch('/api/hello');
                const data = await res.json();
                document.getElementById('output').textContent = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """
    
    headers = Headers.new({"content-type": "text/html; charset=utf-8"})
    return Response.new(html_content, headers=headers)