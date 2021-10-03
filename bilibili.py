import requests
import json

url = r'https://api.bilibili.com/x/web-interface/ranking/region?rid=13&day=7'
headers = {
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    'cookie':'_zap=2fda77ed-6b72-4ea9-a35d-a130cfb04d65; d_c0="APBeok75rhOPTpFjTDKO2KSCf6EDjl5DNrI=|1630939811"; _xsrf=M6nu2mjasjFYoELaJsh9MEpYCRAPiDks; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1632571256,1632575173,1632575926,1632629343; captcha_session_v2="2|1:0|10:1632629378|18:captcha_session_v2|88:bEdkNVpsTDBpZERZeHFsTkVqUkhKUnAyV2VCaW9JM2dKd1ZXSFQ5eFMrN0lyMU02OVc2ZVJmNGk0NFdmMElpZA==|9d140d0b5122de325635ce4d097deade9ca19eda9c6999211a5e629c6213dcdd"; l_n_c=1; r_cap_id="MTBjZTA0MDViN2U3NDZlYWI4M2JkODkwNjlmYTRiZjk=|1632629501|d34c43cfade1e872918b56157ab62c5759500d82"; cap_id="MjljZWZkN2M1N2U5NDRiZWJmZDQwZmI3YTE4NzUxZmY=|1632629501|636eaa9ed2a7fdaa9f7bbe79b50b90c26b648522"; l_cap_id="YzEzZTY0OWM4OWY2NGVkM2I0NmIxY2FiMzBmY2FmNGY=|1632629501|24720408c70c7e4b7c38a922e540b2906a06797d"; n_c=1; z_c0=Mi4xUnFmckJ3QUFBQUFBOEY2aVR2bXVFeGNBQUFCaEFsVk5BVUU5WWdCZHpFUFk2cVg5eWRVdElVaVVBRkdWZG54aFRn|1632629505|d24b235541eb0e1d46533fcdf850b7b60f28119c; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1632629479; KLBRSID=ca494ee5d16b14b649673c122ff27291|1632629508|1632629370'
}
bil_data_str = requests.get(url=url, headers=headers).text
data =  json.loads(bil_data_str)
title_dongmans = data['data']
titles = [title_dongman['title'] for title_dongman in title_dongmans]
print(titles)