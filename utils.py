import os
import requests, json
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
from linebot.models import *

load_dotenv()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

smms_token = os.getenv("SMMS_API_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_image_url(reply_token, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_image_carousel_message(reply_token, url): #不能顯示完整圖片，棄用
    message = TemplateSendMessage(
        alt_text='Image Carousel template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url=url,
                action=PostbackTemplateAction(
                    label='返回',
                    text='返回',
                )
            ),
            ImageCarouselColumn(
                image_url=url,
                action=URIImagemapAction(
                    label='查看原圖',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
    )

    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_flex_message(reply_token, alt_text, message):
    flex_message = FlexSendMessage(alt_text, message)
    line_bot_api.reply_message(reply_token, flex_message)
    return "OK"

def readJson(filepath='./output/upload.json'):
    data = {}
    if os.path.exists(filepath):
        with open(filepath, encoding='utf-8') as f:
            data = json.load(f)
    return data

def saveJson(data, filepath='./output/upload.json'):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def uploadSMMS(localpath):
    print(f"Uploading {localpath} to sm.ms")
    headers = {'Authorization': smms_token}
    files = {'smfile': open(localpath, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    if not res['success']:
        if res['code'] == "image_repeated":
            return res['images']
        else:
            print(json.dumps(res, indent=4))
            return False
    else:
        return res['data']['url']

def uploadIMGUR2(localpath):
    print(f"Uploading {localpath} to imgur.com, use method2")
    name = os.path.basename(localpath)
    client_id = "546c25a59c58ad7" # 網頁端的 client_id ?
    url = f"https://api.imgur.com/3/image?client_id={client_id}"
    headers = {'referer': 'https://imgur.com/'}
    data = {'name': name, 'title': name}
    files = {'name': name,'image': open(localpath, 'rb'), 'type': 'file'}
    res = requests.post(url, headers=headers, data=data, files=files).json()
    if res['success']:
        return res['data']['link']
    elif smms_token:
        return uploadSMMS(localpath)
    else:
        return uploadCC(localpath)
    print(res)

def uploadTUMY(localpath):
    print(f"Uploading {localpath} to tu.my")
    files = {'image': open(localpath, 'rb')}
    data = {'token': 'f56e876f5cc8088b0db7a8c91d8e7914'}
    res = requests.post(url="https://tu.my/api/upload", files=files, data=data).json()
    if res['msg'] == 'success':
        return res['data']['url']
    print(res)
    
def uploadCC(localpath): #很慢，上傳速度不到500Kbps
    print(f"Uploading {localpath} to upload.cc")
    files = {'uploaded_file[]': open(localpath, 'rb')}
    headers = {'referer': 'https://upload.cc/'}
    res = requests.post("https://upload.cc/image_upload", files=files, headers=headers).json()
    if res['total_success']:
        return f"https://upload.cc/{res['success_image'][0]['url']}"
    print(res)

if __name__ == '__main__':
    url = uploadIMGUR2('./output/wah/03.png')
    print(url)
