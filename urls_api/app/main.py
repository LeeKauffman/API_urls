from flask import Flask
from controllers.urls_controller import create_url, get_all_urls, update_url, delete_url

app = Flask(__name__)

app.route('/urls', methods=['POST'])(create_url)
app.route('/urls', methods=['GET'])(get_all_urls)
app.route('/urls/<int:url_id>', methods=['PUT'])(update_url)
app.route('/urls/<int:url_id>', methods=['DELETE'])(delete_url)

if __name__ == '__main__':
    app.run(debug=True)