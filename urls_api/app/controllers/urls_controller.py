from flask import jsonify, request
from models import url_model


def create_url():
    data = request.json
    new_url = url_model.create_url(data['url'])
    return jsonify({'id': new_url['id'], 'url': new_url['url']}), 201

def get_all_urls():
    urls = url_model.get_all_urls()
    return jsonify([{'id': url['id'], 'url': url['url']} for url in urls]), 200

def update_url(url_id):
    data = request.json
    new_url = data['url']
    url_model.update_url(url_id, new_url)
    return jsonify({'message': 'URL updated successfully'}), 200

def delete_url(url_id):
    url_model.delete_url(url_id)
    return jsonify({'message': 'URL deleted successfully'}), 200