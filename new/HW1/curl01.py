import sys
import argparse
import urllib.request
import urllib.error
import json

def main():
    # 1. 設定命令列參數解析
    parser = argparse.ArgumentParser(description="A simple curl-like CLI tool in Python.")
    parser.add_argument("url", help="The target URL to request")
    parser.add_argument("-X", "--method", default="GET", help="HTTP method (GET, POST, etc.)")
    parser.add_argument("-H", "--header", action="append", help="Custom headers in 'Key: Value' format")
    parser.add_argument("-d", "--data", help="Data to send in POST/PUT request (JSON or form)")

    args = parser.parse_args()

    # 2. 處理 Headers
    headers = {}
    if args.header:
        for h in args.header:
            if ":" in h:
                key, val = h.split(":", 1)
                headers[key.strip()] = val.strip()

    # 3. 處理 Data (若有帶入 -d 參數)
    data_bytes = None
    if args.data:
        data_bytes = args.data.encode("utf-8")
        if "Content-Type" not in headers:
            headers["Content-Type"] = "application/x-www-form-urlencoded"

    # 4. 建立 Request 物件
    req = urllib.request.Request(args.url, data=data_bytes, headers=headers, method=args.method.upper())

    try:
        # 5. 發送請求並接收回應
        with urllib.request.urlopen(req) as response:
            print(f"< HTTP/1.1 {response.status} {response.reason}")
            for header, value in response.getheaders():
                print(f"< {header}: {value}")
            print("-" * 40)
            
            body = response.read().decode("utf-8")
            print(body)
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        body = e.read().decode("utf-8")
        print(body)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

if __name__ == "__main__":
    main()
    