from urllib import request
import json
respon = request.urlopen('http://www.baidu.com')
# respon = json.loads(respon.read(0))
print(respon.getcode())


def liv(a,b,c):
    """

    :rtype: object
    :param a: 
    :param b: 
    :param c: 
    """
    