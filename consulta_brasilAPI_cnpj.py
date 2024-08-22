import re
import requests


class ConsultarCNPJ:
    def __init__(self):
        self.url = ''
        self.cnpj = ''

    def clean_cnpj(self):
        try:
            self.cnpj = re.sub(r'\D', '', self.cnpj)
        except:
            pass

    def mount_url(self):
        self.url = f"https://brasilapi.com.br/api/cnpj/v1/{self.cnpj}"

    def get_url_with_cnpj(self, cnpj_in):
        self.cnpj = cnpj_in
        self.clean_cnpj()
        self.mount_url()
        response = requests.get(self.url)
        if response.status_code == 200:
            result = [self.cnpj, response.json()]
        else:
            result = [self.cnpj, response.status_code]
        return result
