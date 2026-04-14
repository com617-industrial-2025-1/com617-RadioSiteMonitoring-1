# api_server.py

from flask import Flask, jsonify
from extract_stats import docker_exec, MUX_CONTAINER, MOD_CONTAINER, MUX_QUERY, MOD_QUERY

app = Flask(__name__)

@app.route("/stats", methods=["GET"])
def stats():
    mux = docker_exec(MUX_CONTAINER, MUX_QUERY)
    mod = docker_exec(MOD_CONTAINER, MOD_QUERY)

    return jsonify({
        "mux": mux,
        "mod": mod
    })


@app.route("/stats/mux", methods=["GET"])
def stats_mux():
    return jsonify(docker_exec(MUX_CONTAINER, MUX_QUERY))


@app.route("/stats/mod", methods=["GET"])
def stats_mod():
    return jsonify(docker_exec(MOD_CONTAINER, MOD_QUERY))


@app.route("/health", methods=["GET"])
def health():
    mux = docker_exec(MUX_CONTAINER, MUX_QUERY)
    mod = docker_exec(MOD_CONTAINER, MOD_QUERY)

    if "error" in mux or "error" in mod:
        return jsonify({"status": "critical"}), 500

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)