# src/controllers/history_controller.py

from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/history", methods=["GET"])
def list_history():
    try:
        history_list = HistoryModel.list_as_json()
        return jsonify(history_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
