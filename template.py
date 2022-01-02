mainMenu={
	"type": "bubble",
	"body": {
		"type": "box",
		"layout": "vertical",
		"contents": [{
			"type": "text",
			"text": "主選單",
			"weight": "bold",
			"size": "xl"
		}]
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
				"height": "md",
				"color": "#ff9900"
			},
			{
				"type": "button",
				"action": {
					"type": "message",
					"label": "顯示視覺化資料",
					"text": "視覺資料"
				},
				"height": "md",
				"color": "#ff9900"
			},
			{
				"type": "button",
				"action": {
					"type": "message",
					"label": "複合資料分析",
					"text": "複合分析"
				},
				"height": "md",
				"color": "#ff9900"
			},
			{
				"type": "button",
				"action": {
					"type": "message",
					"label": "功能介紹與說明",
					"text": "功能說明"
				},
				"height": "md",
				"color": "#000000"
			},
			{
				"type": "spacer",
				"size": "sm"
			}
		],
		"flex": 0
	}
}