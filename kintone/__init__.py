__version__ = "0.1.0"

from typing import Union, List

from .http_request import HttpRequest
from .commands.space import Space
from .commands.app import App
from .commands.form import Form
from .commands.record import Record
from .commands.records import Records


class Kintone:
    def __init__(self, domain: str, user: str = None, password: str = None, token: Union[str, List[str]] = None):
        if (user and password) == token:
            raise ValueError("Either user and password or token must be provided.")
        self.http_request = HttpRequest(domain, user, password, token)
        self.space = Space(self.http_request)
        self.app = App(self.http_request)
        self.form = Form(self.http_request)
        self.record = Record(self.http_request)
        self.records = Records(self.http_request)
