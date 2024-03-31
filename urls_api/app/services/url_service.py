import re
from models import URL

class URLService:
    @staticmethod
    def create_url(url):
        if not url:
            raise ValueError('URL não pode estar vazia')

        if not URLService.validate_url_format(url):
            raise ValueError('Formato de URL inválido')
        
        existing_urls = URL.get_all_urls()
        for existing_url in existing_urls:
            if existing_url.url == url:
                raise ValueError('URL já existe')

        return URL.create_url(url)

    @staticmethod
    def update_url(url_id, new_url):
        if not new_url:
            raise ValueError('Nova URL não pode estar vazia')

        if not URLService.validate_url_format(new_url):
            raise ValueError('Formato da nova URL inválido')

        URL.update_url(url_id, new_url)

    @staticmethod
    def delete_url(url_id):
        URL.delete_url(url_id)

    @staticmethod
    def validate_url_format(url):
        url_pattern = re.compile(
            r'^(?:http|ftp)s?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        return bool(re.match(url_pattern, url))
