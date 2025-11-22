from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
@app.route("/web-app")
def index():
    # Color from query (?color=red) or env var, default skyblue
    color = request.args.get("color") or os.getenv("PAGE_COLOR", "skyblue")
    text = os.getenv("PAGE_TEXT", "Hello from Color Page on K8s!")

    return f"""
    <html>
      <head>
        <title>Color Page</title>
        <style>
          body {{
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: {color};
            font-family: Arial, sans-serif;
          }}
          .card {{
            background: rgba(255,255,255,0.85);
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
          }}
          .meta {{
            margin-top: 10px;
            font-size: 12px;
            color: #555;
          }}
        </style>
      </head>
      <body>
        <div class="card">
          <h1>{text}</h1>
          <div class="meta">
            Color: <b>{color}</b><br/>
            Pod: <b>{os.getenv("HOSTNAME", "unknown")}</b>
          </div>
        </div>
      </body>
    </html>
    """

@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
