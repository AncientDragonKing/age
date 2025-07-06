# raise 觸發系統錯誤
# SystemExit 系統離開

driving = input("你有開過車嗎?")
if driving != "有" and driving != "沒有":
	print("只能輸入 有/沒有")
	raise SystemExit # 不讓下面的程式繼續跑
age = input("你幾歲?")
age = int(age)
if driving == "有":
	if age >= 18:
		print("你可能有考過駕照了")
	else:
		print("你不應該開過車")
elif driving == "沒有": # 沒有的可能
	if age >= 18:
	    print("你可以考駕照啦，怎麼還不去考")
	else:
		print("再等幾年就可以去考了")
else:
	print("只能輸入 有/沒有")