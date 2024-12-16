from flask import Flask, jsonify, send_file
import yfinance as yf
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def serve_chart():
    return send_file('index.html')

@app.route('/data')
def serve_data():
    try:
        ticker = "NQ=F"
        interval = "1d"
        displayForDays = 365

        end_date = datetime.now()
        start_date = end_date - timedelta(days=displayForDays)

        data = yf.download(
            tickers=ticker,
            start=start_date,
            end=end_date,
            interval=interval,
            progress=False,
            threads=False
        )

        chart_data = [
            {
                "time": date.strftime("%Y-%m-%dT%H:%M:%S"),
                "open": float(row['Open']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "close": float(row['Close'])
            }
            for date, row in data.iterrows()
        ]

        if not chart_data:
            return jsonify({"error": "No data available"}), 404

        return jsonify(chart_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
