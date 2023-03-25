import requests
from typing import Type
from src.settings import settings
from collections import namedtuple
from requests import Request, Response
from src.infra.geradorbrasileiro.exceptions import (
    GeradorBrasileiroException,
    GeradorBrasileiroRequestException,
)


class GeradorBrasileiroClient:
    def __init__(self) -> None:
        self._url_prefix = settings.GB_API_URL
        self._header = {"Content-type": "application/json"}
        self._default_return = namedtuple(
            "GeradorBrasileiroClient", "status_code request response"
        )

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def get_person(self, limit: int = None) -> any:
        url = (
            f"{self._url_prefix}/pessoa?limit={limit}"
            if limit
            else f"{self._url_prefix}/pessoa"
        )
        request = Request(
            method="GET",
            url=url,
            headers=self._header,
        )
        response = self.__send_http_request(req_prepared=request.prepare())

        if 400 <= response.status_code < 500:
            raise GeradorBrasileiroRequestException(
                error=response.reason,
                message=response.text,
                status_code=response.status_code,
            )

        elif response.status_code >= 500:
            raise GeradorBrasileiroException(
                message=response.text, status_code=response.status_code
            )

        else:
            return self._default_return(
                status_code=response.status_code,
                request=request,
                response=response.text,
            )
