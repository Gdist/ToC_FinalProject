import os
from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_flex_message, uploadSMMS
from utils import *
import template
import vote, choropleth
import copy

voteData = vote.readDataFromJson()

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # Conditions
    def is_going_to_menu(self, event):
        return event.type == "follow" or event.message.text in ["menu", "主選單"]
        #return event.type == "follow" or event.message.text

    def is_going_to_showFSM(self, event):
        text = event.message.text
        return "fsm" in text.lower()

    def is_going_to_voteStats(self, event):
        return event.message.text == "投票數據"

    def is_going_to_voteStatsRegion(self, event):
        text = event.message.text
        text = text.replace("總計", "合計")
        for sep in "-,_ ":
            splits = text.split(sep)
            if len(splits)==3:
                city, dept, li = splits
                if city in voteData[17] and dept in voteData[17][city] and li in voteData[17][city][dept]:
                    return True
            elif len(splits)==2:
                city, dept = splits
                if city in voteData[17] and dept in voteData[17][city]:
                    return True
            else: 
                if text in voteData[17]:
                    return True
        return False

    def is_going_to_visualData(self, event):
        return event.message.text == "視覺資料"

    def is_going_to_visualDataRegion(self, event):
        text = event.message.text
        if text in ["全國", "臺灣", "台灣"]:
            return True
        elif text in voteData[17]:
            return True
        return False

    def is_going_to_multiAnalysis(self, event):
        return event.message.text == "複合分析"

    def is_going_to_selectItem(self, event):
        text = event.message.text
        if text in ["中位數", "平均數"]:
            return True
        return False

    def is_going_to_funcIntro(self, event):
        return event.message.text == "功能說明"

    def is_go_back_to_menu(self, event):
        text = event.message.text
        return "返回" in text

    # Enter states
    def on_enter_menu(self, event):
        print("I'm entering menu")
        send_flex_message(event.reply_token, "開啟主選單", template.mainMenu)

    def on_enter_showFSM(self, event):
        print("I'm entering showFSM")
        send_image_url(event.reply_token, "https://raw.githubusercontent.com/Gdist/ToC_FinalProject/master/fsm.png")
        self.go_back()
  
    def on_enter_voteStats(self, event):
        print("I'm entering voteStats")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入想查詢的地區")

    def on_enter_voteStatsRegion(self, event):
        print("I'm entering voteStatsRegion")
        reply_token = event.reply_token
        text = event.message.text
        text = text.replace("總計", "合計")

        for sep in "-,_ ":
            splits = text.split(sep)
            if len(splits)==3:
                city, dept, li = splits
                region = f"{city}{dept}{li}"
                if city in voteData[17] and dept in voteData[17][city] and li in voteData[17][city][dept]:
                    break
            elif len(splits)==2:
                city, dept, li = splits + ['合計']
                region = f"{city}{dept}"
                if city in voteData[17] and dept in voteData[17][city]:
                    break
            else: 
                if text in voteData[17]:
                    region = text
                    city, dept, li = text, '合計', '合計'
                    break
        message = copy.deepcopy(template.text)
        message['header']['contents'][0]['text'] = f"{region}投票數據"
        for themeId in range(17, 21):
            votes = voteData[themeId][city][dept][li]

            cur_subtitle = copy.deepcopy(template.text_subtitle)
            cur_subtitle['text'] = f"第{themeId}案"
            message['body']['contents'].append(cur_subtitle)

            cur_text = copy.deepcopy(template.text_text)
            cur_text['text'] = f"有效票數：{votes['valid_ticket']}\n"
            cur_text['text'] += f"同意票數：{votes['agree_ticket']}\n"
            cur_text['text'] += f"投票率：{votes['vote_to_votable']}%\n"
            agree_rate = round(100 * votes['agree_ticket']/votes['valid_ticket'], 2)
            cur_text['text'] += f"同意率：{agree_rate}%"
            message['body']['contents'].append(cur_text)
        text1 = {"type": "text", "text": "\n若要查詢其他地區，請直接繼續輸入\n若要返回主目錄，請點擊返回鍵", "wrap": True}
        message['body']['contents'].append(text1)

        send_flex_message(event.reply_token, "顯示投票數據", message)

        # 繼續輸入或輸入「返回」返回目錄（要多做按鈕）

    def on_enter_visualData(self, event):
        print("I'm entering visualData")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入想查詢的地區（全國或縣市）")

    def on_enter_visualDataRegion(self, event):
        print("I'm entering visualDataRegion")
        reply_token = event.reply_token
        text = event.message.text
        city = 'Taiwan' if text in ["全國", "臺灣", "台灣"] else text

        message = copy.deepcopy(template.carousel)
        imgLinks = []
        for themeId in ['All'] + list(range(17,21)):
            localpath = f'./output/map/{city}_{themeId}.png'
            if not os.path.exists(localpath):
                choropleth.plotCity(themeId=themeId, cityName=city)
            imgLink = uploadSMMS(localpath)
            imgLinks.append(imgLink)
            cur_image_map = copy.deepcopy(template.image_map)
            title = f"{text}第{themeId}案同意率" if isinstance(themeId, int) else f"{text}四案同意率"
            cur_image_map['header']['contents'][0]['text'] = title
            cur_image_map['hero']['url'] = imgLink
            cur_image_map['footer']['contents'][0]['action']['uri'] = imgLink
            message['contents'].append(cur_image_map)
        #print(message)
        #send_image_url(event.reply_token, imgLinks[0])
        send_flex_message(event.reply_token, "顯示分層設色圖", message)

    def on_enter_multiAnalysis(self, event):
        print("I'm entering multiAnalysis")
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇項目（收入中位數／平均數）")

    def on_enter_selectItem(self, event):
        print("I'm entering selectItem")
        reply_token = event.reply_token
        text = event.message.text

        message = copy.deepcopy(template.carousel)
        imgLinks = []
        for order in "前後":
            localpath = f'./output/{text}{order}100.png'
            if not os.path.exists(localpath):
                ascending = False if order == "前" else True
                vote.main(byData=text, numData=100, ascending=ascending)
            imgLink = uploadSMMS(localpath)
            imgLinks.append(imgLink)
            cur_image_map = copy.deepcopy(template.image_map)
            title = f"收入{text}{order}100村里同意率"
            cur_image_map['header']['contents'][0]['text'] = title
            cur_image_map['hero']['url'] = imgLink
            cur_image_map['hero']['aspectRatio'] = "1.3:1"
            cur_image_map['body']['contents'][0]['text'] = "若要查詢其他項目，請直接繼續輸入"
            cur_image_map['footer']['contents'][0]['action']['uri'] = imgLink
            message['contents'].append(cur_image_map)
        #print(message)
        send_flex_message(event.reply_token, "顯示複合分析圖", message)

    def on_enter_funcIntro(self, event):
        print("I'm entering funcIntro")
        reply_token = event.reply_token
        send_flex_message(event.reply_token, "功能介紹", template.intro)

'''
    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()
'''
if __name__ == '__main__':
    print()