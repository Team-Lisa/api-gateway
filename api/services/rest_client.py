from fastapi import HTTPException
from json import JSONDecodeError

import requests


class RestClient:

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            status = response.status_code

            if status >= 500:
                raise HTTPException(status_code=status, detail="internal server error")
            elif status >= 400:
                json = response.json()
                raise HTTPException(status_code=status, detail=json.get("message", "Not Found"))
            else:
                json = response.json()

            return json
        except JSONDecodeError:
            raise HTTPException(status_code=500, detail="internal server error")

