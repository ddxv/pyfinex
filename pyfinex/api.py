# Import Built-Ins
import base64
import hashlib
import hmac
import json
import requests
import time

class API(object):
    def __init__(self, environment='live', key=None, secret_key=None):
        self._key = key
        self._secret_key = secret_key
        self.client = requests.Session()
        self.version = 0
        if environment == 'live':
            self.api_url = 'https://api.bitfinex.com/'
        else:
            # for future, access to a demo account.
            pass

    def request(self, endpoint, method='GET', auth=True, params=None, payload_params=None):
        """ Returns dict of response from Bitfinex's open API """
        method = method.upper()
        url = '%s/v%s/%s' % (self.api_url,self.version, endpoint)
        request_args = {'params': params}

        if auth:
            payload_object = {
                "request": "/v%s/%s" % (self.version,endpoint),
                "nonce": str(time.time() * 1000000)  # update nonce each POST request
            }
            if payload_params is not None:
                payload_object.update(payload_params)
            payload = base64.b64encode(bytes(json.dumps(payload_object), "utf-8"))
            signature = hmac.new(self._secret_key, msg=payload, digestmod=hashlib.sha384).hexdigest()
            request_args['headers'] = {
                'X-BFX-APIKEY': self._key,
                'X-BFX-PAYLOAD': payload,
                'X-BFX-SIGNATURE': signature
            }
            # request_args['data'] = {}

        try:
            response = self.client.request(method, url, **request_args)
            content = response.json()
        except Exception as e:
            print("Failed to get the response because %s. \
                   The request url is %s" % (str(e), url))

        # error message
        if response.status_code >= 400:
            print("%s error_response : %s" % (str(response.status_code), content))
            raise BitfinexError(response.status_code, content)

        return content

# Contains BITFINEX exception
class BitfinexError(Exception):
    """ Generic error class, catches bitfinex response errors
    """

    def __init__(self, status_code, error_response):
        msg = "BITFINEX API returned error code %s (%s)" % (status_code, error_response['error'])

        super(BitfinexError, self).__init__(msg)