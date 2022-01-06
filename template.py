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

itemMenu = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇分析項目",
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
        "type": "text",
        "text": "收入",
        "size": "lg",
        "weight": "bold",
        "align": "center",
        "gravity": "bottom"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "平均數",
              "text": "收入-平均數"
            },
            "color": "#DEFCF9",
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "中位數",
              "text": "收入-中位數"
            },
            "color": "#E3FDFD",
            "style": "secondary"
          }
        ]
      },
      {
        "type": "text",
        "text": "年齡",
        "size": "lg",
        "weight": "bold",
        "align": "center",
        "gravity": "bottom"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "平均數",
              "text": "年齡-平均數"
            },
            "style": "secondary",
            "color": "#E3FDFD"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "中位數",
              "text": "年齡-中位數"
            },
            "style": "secondary",
            "color": "#DEFCF9"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "30歲以下",
              "text": "年齡-30歲以下比例"
            },
            "color": "#DEFCF9",
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "40歲以下",
              "text": "年齡-40歲以下比例"
            },
            "style": "secondary",
            "color": "#E3FDFD"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "70歲以上",
              "text": "年齡-70歲以上比例"
            },
            "style": "secondary",
            "color": "#E3FDFD"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "80歲以上",
              "text": "年齡-80歲以上比例"
            },
            "style": "secondary",
            "color": "#DEFCF9"
          }
        ]
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
        "text": "若要返回主目錄，請點擊返回目錄鍵",
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
          "label": "返回目錄",
          "text": "返回目錄"
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
        "text": "將公投結果與各村里收入與年齡做複合分析",
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
          "label": "返回目錄",
          "text": "返回目錄"
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
          "label": "返回目錄",
          "text": "返回目錄"
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

btn = {
  "type": "button",
  "action": {
    "type": "message",
    "label": "重新選擇分析項目",
    "text": "重新選擇分析項目"
    },
  "color": "#F6D860",
  "style": "primary"
  }

if __name__ == '__main__':
    image_map['header']['contents'][0]['text'] = "標題"
    image_map['hero']['url'] = "LINK"
    image_map['footer']['contents'].insert(1, btn)
    print(image_map['footer']['contents'][0]['color'])
    #print(image_map)