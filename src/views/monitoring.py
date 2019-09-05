# coding=utf-8

from flask import Blueprint, current_app, jsonify

mod_monitoring = Blueprint('monitoring', __name__)

@mod_monitoring.route('ping', methods=['GET', 'POST'])
def ping():
    """
    A simple ping call to test that the app it's still up
    :return:
    """
    return "pong"

@mod_monitoring.route('redis-status', methods=['GET', 'POST'])
def app_status():
    redis_connector = current_app.config['redis_connector']
    status = dict()
    status['db'] = "OK" if redis_connector.ping() else "FAIL"
    return jsonify(redis_connectivity=status["db"])
