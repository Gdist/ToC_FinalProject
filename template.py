mainMenu = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "主選單",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "查詢投票數據",
          "text": "投票數據"
        },
        "color": "#EA5C2B",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "顯示視覺化資料",
          "text": "視覺資料"
        },
        "color": "#FF7F3F",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "複合資料分析",
          "text": "複合分析"
        },
        "color": "#F6D860",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "功能介紹與說明",
          "text": "功能說明"
        },
        "color": "#95CD41",
        "style": "secondary"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}

image_map = {
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "分層設色圖",
        "weight": "bold",
        "size": "xl",
        "color": "#000000FF",
        "align": "center",
        "margin": "none",
        "wrap": True,
        "decoration": "underline",
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://s2.loli.net/2022/01/02/653Tf8PEgaUwjCI.png",
    "align": "center",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "1:1",
    "aspectMode": "cover",
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "若要查詢其他縣市，請直接繼續輸入",
        "contents": []
      },
      {
        "type": "text",
        "text": "若要返回主目錄，請點擊返回鍵",
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "查看圖片",
          "uri": "https://linecorp.com"
        },
        "color": "#F6D860",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回",
          "text": "返回"
        },
        "color": "#95CD41",
        "style": "primary"
      }
    ]
  }
}

carousel = {
  "type": "carousel",
  "contents": []
}

intro = {
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能介紹與說明",
        "weight": "bold",
        "size": "xl",
        "color": "#000000FF",
        "align": "center",
        "contents": []
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查詢投票數據",
        "weight": "bold",
        "size": "lg",
        "align": "start",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "查詢各縣市、鄉鎮市區、村里於2021年公投的公投投票同意率、投票率等數據",
        "wrap": True
      },
      {
        "type": "text",
        "text": "顯示視覺化資料",
        "weight": "bold",
        "size": "lg",
        "align": "start",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "顯示全國或各縣市公投各案的投票率之分層設色圖",
        "wrap": True
      },
      {
        "type": "text",
        "text": "複合資料分析",
        "weight": "bold",
        "size": "lg",
        "align": "start",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "將公投結果與各村里收入做複合分析",
        "wrap": True
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回",
          "text": "返回"
        },
        "color": "#95CD41",
        "style": "primary"
      }
    ]
  }
}

text = {
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能介紹與說明",
        "weight": "bold",
        "size": "xl",
        "color": "#000000FF",
        "align": "center",
        "wrap": True
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": []
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回",
          "text": "返回"
        },
        "color": "#95CD41",
        "style": "primary"
      }
    ]
  }
}

text_text = {
    "type": "text",
    "text": "顯示全國或各縣市公投各案的投票率之分層設色圖",
    "wrap": True
    }
text_subtitle = {
    "type": "text",
    "text": "複合資料分析",
    "weight": "bold",
    "size": "lg",
    "wrap": True,
    }

if __name__ == '__main__':
    image_map['header']['contents'][0]['text'] = "標題"
    image_map['hero']['url'] = "LINK"
    image_map['footer']['contents'][0]['action']['uri']  = "LINK"
    print(image_map['footer']['contents'][0]['action']['uri'])