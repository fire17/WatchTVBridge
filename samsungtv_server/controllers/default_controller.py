import connexion
import six

from samsungtv_server.models.error_response import ErrorResponse  # noqa: E501
from samsungtv_server.models.status_response import StatusResponse  # noqa: E501
from samsungtv_server import util
from samsungtv_server.controllers import SamsungTV

def get_status():  # noqa: E501
    """get_status

    Checks the configuration and gets the status of the TV # noqa: E501


    :rtype: StatusResponse
    """
    return 'do some magic!', 202

def send(key, rep = 1)
    for a in range(rep):
        t = Thread(target = post_key, args = [key,])
        t.start()

def post_key(key):  # noqa: E501
    """post_key

    Sends a remote control key to the TV # noqa: E501

    :param key:
    :type key: str

    :rtype: None
    """

    key = key.upper()
    if (key.find('KEY_') != 0):
        key = 'KEY_' + key

    tv = SamsungTV('192.168.43.144')
    tv.send_key(key, 1)
    tv.close()

    return 'Sent {}'.format(key), 202
