from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import base64
import datetime
import hashlib
import hmac
import json
import random
import string

reply = {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "replied_message_id": "1702969262-9de157f2-cd73-4551-b386-8d937f8a8f06",
  "to": "6281210028232",
  "type": "text",
  "data": {
    "preview_url": False,
    "body": "iya mba.."
  }
}

send_message = {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "6281210028232",
  "type": "text",
  "data": {
    "preview_url": False,
    "body": "hai sayang"
  }
}


broadcast = {
  "template_id": "885574976303478",
  "data": [
    {
        "to": "6281237615158",
        "template": {
            "name": "call_action_butto",
            "language": {
                "code": "en_US"
                },
            "components": []
        }
    }
  ]
}

{
    "system_id": "1234567890abcdef",
    "unique_id": "1234567890abcdef",
    "param": "cI8QT+80PxHxnKNtGElyaxReeLOAEYEw1PDylTL8YWg=",
    "auth_token": "0c4702ac97ecf07b980d98636d1c270ccdcdd517869103ee40adc19c2f131d8b",
    "iv": "abcdefghijklmnop",
    "op": "greeting",
    "timestamp": "2023-09-27T16:51:30.927208Z"
}

uniq = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

now = datetime.datetime.now(datetime.timezone.utc)
tstamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

system_id = "i4DV8jX45PSOiulf"
secret_key = "5Amr6IBP3r24SKTh"
salt = "vUrm0rCEjWZUTn4j"

request_param = {"data":[{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Pemetaan Tenaga Kesehatan","type":"HEADER"},{"example":{"body_text":[["Febri Iqbal","Perawat"]]},"text":"Yth. {{1}}\nProfesi: {{2}}\n\nKTKI mengundang Anda untuk berpartisipasi dalam survei pemetaan tenaga kesehatan yang akan membantu peningkatan mutu praktik kesehatan di Indonesia. Survei ini meliputi aspek registrasi, standarisasi, dan pembinaan. Hasil survei akan sangat berharga dalam merancang dan mengimplementasikan program peningkatan mutu praktik tenaga kesehatan di masa mendatang.\n\nPartisipasi Anda sangat berharga. Silakan kunjungi tautan ini untuk mengisi survei: https://ktki.go.id/berita/pemetaan-tenaga-kesehatan.\n\nTerima kasih atas dukungan Anda.\n\nSalam Sehat,\nKonsil Tenaga Kesehatan Indonesia","type":"BODY"},{"buttons":[{"text":"Pemetaan Tenaga Kesehatan","type":"URL","url":"https://ktki.go.id/berita/pemetaan-tenaga-kesehatan"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"408681425308901","template_name":"ktki_template_return_case","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"body_text":[["Login","25OFF"]]},"text":"Token {{1}} : {{2}}","type":"BODY"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"REJECTED","template_id":"975923414209825","template_name":"template_coba_token","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"body_text":[["TCK001","12:00","NCR 001"]]},"text":"Hallo maniss {{1}}, lagi apa? {{2}}. kamu sangat {{3}}","type":"BODY"},{"buttons":[{"example":["https://dev-ncr.g4sindonesia.com/p/TT-2024-0001"],"text":"Ticket Link","type":"URL","url":"https://dev-ncr.g4sindonesia.com/p/{{1}}"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"1597155424458500","template_name":"iss_dispatch_response_team_v2","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Hi Pelanggan yang terhormat","type":"HEADER"},{"text":"Selamat datang di pusat bantuan chatlive kami. Saya senang anda memilih untuk berkomunikasi dengan kami secara langsung. Bagaimana saya bisa membantu anda hari ini ?😊","type":"BODY"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"3590943241122281","template_name":"macro_greetingtesting","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"text":"This is a test for action button","type":"BODY"},{"buttons":[{"text":"website","type":"URL","url":"https://iohwaba.com/"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"239231312136754","template_name":"action_button","type":"STATIC","updated_tstamp":1716372180},{"category":"AUTHENTICATION","company_id":114,"components":[{"example":{"body_text":[["123456"]]},"text":"*{{1}}* adalah kode verifikasi Anda. Demi keamanan, jangan bagikan kode ini.","type":"BODY"},{"text":"Kode ini kedaluwarsa dalam 10 menit.","type":"FOOTER"},{"buttons":[{"example":["https://www.whatsapp.com/otp/code/?otp_type=COPY_CODE\u0026code_expiration_minutes=10\u0026code=otp123456"],"text":"Salin kode","type":"URL","url":"https://www.whatsapp.com/otp/code/?otp_type=COPY_CODE\u0026code_expiration_minutes=10\u0026code=otp{{1}}"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","message_send_ttl_seconds":600,"previous_category":"","status":"APPROVED","template_id":"1062295811718366","template_name":"test_otp_pandey_1","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_text":["Lunar Year Sale"]},"format":"TEXT","text":"Our {{1}} is on!","type":"HEADER"},{"example":{"body_text":[["the end of February","25OFF","25%"]]},"text":"Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.","type":"BODY"},{"text":"Use the buttons below to manage your marketing subscriptions","type":"FOOTER"},{"buttons":[{"text":"Unsubscribe from Promos","type":"QUICK_REPLY"},{"text":"Unsubscribe from All","type":"QUICK_REPLY"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"1535274317310810","template_name":"lunar_year_event","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_text":["[Gratis]"]},"format":"TEXT","text":"Registrasi member {{1}}","type":"HEADER"},{"text":"Please daftar member untuk dapetin promo ya!","type":"BODY"},{"text":"yukk join","type":"FOOTER"},{"buttons":[{"flow_action":"NAVIGATE","flow_id":890142682481894,"navigate_screen":"REPORT_FORM","text":"Klik ini cepat!!","type":"FLOW"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"1275655869786020","template_name":"coba_flow_1","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"UTILITY","company_id":114,"components":[{"format":"TEXT","text":"Pemberitahuan Tagihan Rekening Air","type":"HEADER"},{"example":{"body_text":[["Ridzhal","0123456789","Sendangharjo","75,000","2 bulan"]]},"text":"Diberitahukan dengan Hormat Kepada Pelanggan Perumda Air Minum Tirta Lestari Kabupaten Tuban \n\n*NAMA : {{1}}* \n*NO SAMB : {{2}}* \n*ALAMAT : {{3}}* \n\nDimohon untuk segera melunasi kewajiban pembayaran rekening air sebesar *Rp. {{4}} ({{5}}) sebelum tanggal 20* di Kantor Perumda Air Minum Tirta Lestari atau loket pembayaran terdekat. *Apabila lebih dari tanggal 20* belum dilakukan pembayaran, maka akan dilakukan penutupan sementara tanpa pemberitahuan. \n\nTerima Kasih atas perhatian dan kerjasamanya. \n\n*Note: Abaikan pesan ini apabila sudah melakukan pembayaran.*\n\nKunjungi web kami pada link dibawah untuk :\n1. Cek Tagihan Air\n2. Aduan Gangguan\n3. Daftar Sambungan Baru","type":"BODY"},{"buttons":[{"text":"Info Pelanggan","type":"URL","url":"https://info.perumdaairminumtuban.co.id/"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"355254767362886","template_name":"tagihan_air","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"text":"Tolong daftar G4S aja!","type":"BODY"},{"buttons":[{"text":"Klik ini cepat!!","type":"URL","url":"http://34.101.84.34:8080/login.html"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"311281735082693","template_name":"register_aja_4","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"text":"Tolong daftar disana!","type":"BODY"},{"buttons":[{"text":"Klik Link ini aja","type":"URL","url":"http://165.22.62.197/"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"885574976303478","template_name":"register_aja_3","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"text":"Tolong daftar disini!","type":"BODY"},{"buttons":[{"text":"Klik Link berikut","type":"URL","url":"https://collection-bot.tel-access.com/smartagent/uploadform.html"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"756642746285379","template_name":"register_aja_2","type":"STATIC","updated_tstamp":1716372180},{"category":"UTILITY","company_id":114,"components":[{"text":"Tolong daftar disini!","type":"BODY"},{"buttons":[{"text":"Klik Link berikut","type":"URL","url":"https://collection-bot.tel-access.com/smartagent/uploadform.html"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"REJECTED","template_id":"732069244944984","template_name":"register_aja_1","type":"STATIC","updated_tstamp":1716372180},{"category":"UTILITY","company_id":114,"components":[{"text":"Please register here","type":"BODY"},{"buttons":[{"text":"Contact Support","type":"URL","url":"https://collection-bot.tel-access.com/smartagent/uploadform.html"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"REJECTED","template_id":"1580148136149448","template_name":"register_aja","type":"STATIC","updated_tstamp":1716372180},{"category":"UTILITY","company_id":114,"components":[{"text":"Please register here","type":"BODY"},{"buttons":[{"text":"Contact Support","type":"URL","url":"https://collection-bot.tel-access.com/smartagent/uploadform.html"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"REJECTED","template_id":"1412523602698375","template_name":"order_confirmation","type":"STATIC","updated_tstamp":1716372180},{"category":"UTILITY","company_id":114,"components":[{"format":"LOCATION","type":"HEADER"},{"text":"This is the location : https://goo.gl/maps/VJqPrspq7qcy1qF78","type":"BODY"}],"created_tstamp":1716372180,"language":"id","previous_category":"MARKETING","status":"APPROVED","template_id":"208762105420503","template_name":"location","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_handle":["https://scontent.whatsapp.net/v/t61.29466-34/311558632_444052494307419_7589624727525337921_n.jpg?ccb=1-7\u0026_nc_sid=8b1bef\u0026_nc_ohc=R0pkpc0qOo8Q7kNvgEgmk-6\u0026_nc_ht=scontent.whatsapp.net\u0026edm=AH51TzQEAAAA\u0026oh=01_Q5AaIOuJzZClNa9ILQ4s0U5c6L9yfPy31TkImftAf4PFUqHv\u0026oe=66753414"]},"format":"IMAGE","type":"HEADER"},{"example":{"body_text":[["20%","30 Oktober","Rp 60.000"]]},"text":"Hi, Ada spesial promo untuk kamu nih!\n\nDapatkan cashback {{1}} hingga tanggal {{2}}, promo cashback Setiap pembelian minimal {{3}}. \n\nBuruan order sekarang, jangan sampai terlambat!","type":"BODY"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"APPROVED","template_id":"444052490974086","template_name":"promo_test","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"body_text":[["TCK001","12:00","INDOSAT","Burglary Alarm","001","01"]]},"text":"New Event Alarm [{{1}}]\n[{{2}}] | A new event Alarm has been occurs on [{{3}}]\nHere are some details about the alarm :\nEvent Name : {{4}}\nZone : Zone {{5}}\nPartition : {{6}}\nThe NCR team is in the process of investigating the cause of the triggered alarm to ensure your safety and security.\nRegards,\nG4S Security Services","type":"BODY"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"2028950400797214","template_name":"iss_alarm_trigger_test007","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"text":"Halo!! \n {{1}} How are you today?","type":"BODY"},{"text":"team salam","type":"FOOTER"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"REJECTED","template_id":"2415154598667048","template_name":"salam001","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"text":"Halo!! \n {{1}} How are you today?","type":"BODY"},{"text":"marketing team","type":"FOOTER"}],"created_tstamp":1716372180,"language":"id","previous_category":"","status":"REJECTED","template_id":"2183506158668558","template_name":"salam","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"text":"sale at {{1}} and use code {{2}}","type":"BODY"},{"text":"marketing team","type":"FOOTER"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"340236768742841","template_name":"panic_alarm174","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_text":["winter sale"]},"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"example":{"body_text":[["end of november","ABC123"]]},"text":"sale at {{1}} and use code {{2}}","type":"BODY"},{"text":"marketing team","type":"FOOTER"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"307446612170052","template_name":"panic_alarm7","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_text":["human traficking"]},"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"example":{"body_text":[["pandey","jelek"]]},"text":"hello {{1}} test data {{2}}.","type":"BODY"},{"text":"sample footer","type":"FOOTER"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"REJECTED","template_id":"726320729543754","template_name":"panic_alarm1","type":"DYNAMIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"format":"TEXT","text":"Our sale is {{1}} on!","type":"HEADER"},{"text":"hello {{1}} test data {{2}}.","type":"BODY"},{"text":"sample footer","type":"FOOTER"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"REJECTED","template_id":"183424758169233","template_name":"panic_alarm","type":"STATIC","updated_tstamp":1716372180},{"category":"MARKETING","company_id":114,"components":[{"example":{"header_text":["Summer Sale"]},"format":"TEXT","text":"Our {{1}} is on!","type":"HEADER"},{"example":{"body_text":[["the end of August","25OFF","25%"]]},"text":"Shop today through {{1}} and use code {{2}} to get {{3}} off of all merchandise.","type":"BODY"},{"text":"Use the buttons below to manage your marketing subscriptions","type":"FOOTER"},{"buttons":[{"text":"Unsubscribe from Promos","type":"QUICK_REPLY"},{"text":"Unsubscribe from All","type":"QUICK_REPLY"}],"type":"BUTTONS"}],"created_tstamp":1716372180,"language":"en_US","previous_category":"","status":"APPROVED","template_id":"715750853768353","template_name":"promo99","type":"DYNAMIC","updated_tstamp":1716372180}]}

op = "broadcast"
unique_id = str(uniq)
timestamp = tstamp
iv = "abcdefghijklmnop"

# param = Base64(AES256_CBC(message = JSON(request_param), secret = key, iv = iv))

# key = SHA256(HEX(HMACSHA256(secret = salt, message = secret_key)) + unique_id + timestamp + op)

salted_secret_key = hmac.new(key=salt.encode("utf-8"), msg=secret_key.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()

unhashed_key = salted_secret_key + unique_id + timestamp + op

key_raw = hashlib.sha256(unhashed_key.encode())
key = key_raw.digest()

json_req_param = json.dumps(request_param)

cipher = AES.new(key, AES.MODE_CBC, iv.encode())
ciphertext = cipher.encrypt(pad(json_req_param.encode("utf-8"), AES.block_size))
param = base64.b64encode(ciphertext).decode("utf-8")

# auth_token = HEX(SHA256(salted_secret_key + unique_id + timestamp + op + param))

input_hash = salted_secret_key + unique_id + timestamp + op + param

auth_token = hashlib.sha256(input_hash.encode()).hexdigest()

request_payloads = {
    "system_id": system_id,
    "unique_id": unique_id,
    "param": param,
    "auth_token": auth_token,
    "iv": iv,
    "op": op,
    "timestamp": timestamp
}

print(json.dumps(request_payloads, indent=4))

############################################################ DECRYPT

# JSON(response_param) = AES256_CBC_decrypt(cipher_text = Base64_decode(param), secret = key, iv = iv)

response = {
    
}

salted_secret_key = '1a5182f32d820ceb8b7c9fc7203ca0f451eb1d8235533c38647d1569b7978bf6'

unhashed_key = salted_secret_key + response['unique_id'] + response['timestamp'] + response['op']
key_raw = hashlib.sha256(unhashed_key.encode())
key = key_raw.digest()

param = response['param']
key_hex = key_raw.hexdigest()
iv = response['iv']

cipher = AES.new(bytes.fromhex(key_hex), AES.MODE_CBC, iv.encode())
decrypted = cipher.decrypt(base64.b64decode(param))
response_param_json = unpad(decrypted, AES.block_size).decode("utf-8")
print(f"JSON(response_param): {response_param_json}")