import json
import requests
from typing import Type
from src.settings import settings
from collections import namedtuple
from requests import Request, Response
from src.schemas.invoice import InvoiceSchemaReq
from src.infra.starkbank.exceptions import StarkBankException, StarkbankRequestException


class StarkbankClient:
    def __init__(self) -> None:
        self._url_prefix = settings.SB_API_URL
        self._header = {"Content-type": "application/json"}
        self._default_return = namedtuple(
            "StarkbankClient", "status_code request response"
        )

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def create_invoice(self, invoice: InvoiceSchemaReq) -> any:
        url = f"{self._url_prefix}/invoice"
        request = Request(
            method="POST",
            url=url,
            data=json.dumps(invoice),
            headers=self._header,
        )
        response = self.__send_http_request(req_prepared=request.prepare())

        if 400 <= response.status_code < 500:
            raise StarkbankRequestException(
                error=response.reason,
                message=response.text,
                status_code=response.status_code,
            )

        elif response.status_code >= 500:
            raise StarkBankException(
                message=response.text, status_code=response.status_code
            )

        else:
            return self._default_return(
                status_code=response.status_code,
                request=request,
                response=response.text,
            )
