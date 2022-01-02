import os
import requests, json
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
from linebot.models import *
import pyimgur

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

imgurClientID = os.getenv("IMGUR_CLIENT_ID", None)
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

def upload_to_imgur(localpath):
    im = pyimgur.Imgur(imgurClientID)
    title = localpath[localpath.rfind('/')+1:localpath.rfind('.')]
    print(title)
    uploaded_image = im.upload_image(localpath, title=title)
    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.size)
    print(uploaded_image.type)
    return uploaded_image.link

def uploadSMMS(localpath):
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

if __name__ == '__main__':
    url = uploadSMMS('./output/map/Taiwan_All.png')
    print(url)
