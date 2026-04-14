from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 🔥 shared state (simple version)
latest_data = {}

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>AI Trading Dashboard</title>
        <script>
            async function loadData() {
                const res = await fetch('/data');
                const data = await res.json();

                document.getElementById('asset').innerText = data.asset;
                document.getElementById('signal').innerText = data.signal;
                document.getElementById('agent').innerText = data.agent;
                document.getElementById('balance').innerText = data.balance;
                document.getElementById('winrate').innerText = data.winrate;
            }

            setInterval(loadData, 2000);
        </script>
    </head>
    <body>
        <h1>🤖 AI Trading Dashboard</h1>
        <p>Asset: <span id="asset"></span></p>
        <p>Signal: <span id="signal"></span></p>
        <p>Agent: <span id="agent"></span></p>
        <p>Balance: <span id="balance"></span></p>
        <p>Winrate: <span id="winrate"></span></p>
    </body>
    </html>
    """

@app.route('/data')
def data():
    return jsonify(latest_data)


def update_dashboard(data):
    global latest_data
    latest_data = data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
