import environ
import requests

from requests.exceptions import HTTPError, RequestException

env = environ.Env()
environ.Env.read_env('./Gateway/.env')


def is_property_valid(property_id: int)->bool:
    property_service_url = f"{env('PROPERTY_HOST')}/property/{property_id}"

    try:
        response = requests.get(property_service_url)

        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False

        response.raise_for_status()

    except HTTPError as http_err:
        raise http_err

    except RequestException as req_err:
        raise req_err

def favorite_property(username:str, property_id: int)->dict:
    favorite_service_url = f"{env('FAVORITE_HOST')}/favorite-property/"

    try:
        response = requests.post(favorite_service_url, data={'username': username, 'property_id': property_id})

        if response.status_code == 200:
            return response.json()

        response.raise_for_status()

    except HTTPError as http_err:
        raise http_err

    except RequestException as req_err:
        raise req_err

def list_properties(query_params:dict = None)->dict:
    property_service_base_url = f"{env('PROPERTY_HOST')}/properties"

    if query_params:
        property_service_url = f"{property_service_base_url}/?{'&'.join(f'{key}={value}' for key, value in query_params.items())}"
    else:
        property_service_url = property_service_base_url

    try:
        response = requests.get(property_service_url)

        if response.status_code == 200:
            response_json = response.json()
            response_json['next'] = response_json['next'].replace('/properties/', '/api/properties') if response_json['next'] else 'null'
            response_json['previous'] = response_json['previous'].replace('/properties/', '/api/properties') if response_json['previous'] else 'null'
            return response_json
        elif response.status_code == 404:
            return {
                "count": 0,
                "next": "null",
                "previous": "null",
                "results": []
            }

        response.raise_for_status()

    except HTTPError as http_err:
        raise http_err

    except RequestException as req_err:
        raise req_err
