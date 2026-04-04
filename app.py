from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os
app = Flask(__name__)
metrics = PrometheusMetrics(app, path="/metrics")


@app.route("/")
def home():
    return "Welcome toCICD pipeline on AWS with codepipline trigger"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)