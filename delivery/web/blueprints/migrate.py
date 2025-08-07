from flask import Blueprint, request, jsonify
from domain.services.edge_migration import migrate_edge
from infrastructure.vcloud_api.client import VCloudClient

migrate_bp = Blueprint("migrate", __name__)

@migrate_bp.route("/migrate", methods=["POST"])
def migrate():
    data = request.get_json()
    source = VCloudClient(data["source_url"], data["source_token"])
    dest = VCloudClient(data["dest_url"], data["dest_token"])
    edge_id = data["edge_id"]

    result = migrate_edge(source, dest, edge_id)
    return jsonify({"success": True, "result": result})

@migrate_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
