from db import connect_db

class URL:
    
    @staticmethod
    def create_url(url):
        connection = connect_db()
        query = """INSERT INTO urls (url) VALUES (%s) RETURNING id;"""
        cursor = connection.cursor()
        cursor.execute(query, (url,))
        id = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return {'id': id, 'url': url}

    @staticmethod
    def get_all_urls():
        connection = connect_db()
        query = """SELECT * FROM urls;"""
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return [{'id': row[0], 'url': row[1]} for row in results]

    @staticmethod
    def update_url(url_id, new_url):
        connection = connect_db()
        query = """UPDATE urls SET url = %s WHERE id = %s;"""
        cursor = connection.cursor()
        cursor.execute(query, (new_url, url_id))
        cursor.close()
        connection.commit()
        connection.close()

    @staticmethod
    def delete_url(url_id):
        connection = connect_db()
        query = """DELETE FROM urls WHERE id = %s;"""
        cursor = connection.cursor()
        cursor.execute(query, (url_id,))
        cursor.close()
        connection.commit()
        connection.close()
