from selenium import webdriver
import time
import json
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/hp/AppData/Local/Google/Chrome/UserData')
browser=webdriver.Chrome(options=options)
browser.get("https://web.whatsapp.com")
action=ActionChains(browser)
browser.maximize_window()
time.sleep(80)

first_message_box=browser.find_element(By.CSS_SELECTOR, '#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div')
first_message_box.click()
time.sleep(30)

ContactNumber=browser.find_element(By.CSS_SELECTOR, '#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 > span')
Number=ContactNumber.text
time.sleep(40)

message=browser.find_element(By.CSS_SELECTOR,"#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
mess=message.text
time.sleep(20)
if mess=="Hi":
	class Phone():
		def __init__(self,input):
			self.phone = input
		def __str__(self):
			return self.phone
		def to_int(self):
			return int((self.phone).replace("+","").replace(" ","").replace(" ",""))

	test = Phone(Number)
	contact = test.to_int()
	print (contact)
	print("Contact number...")
time.sleep(40)

Data=[]
f=open("data.txt")
from_file = f.read()
Content = from_file.split("\n")
for x in Content:
	if x != " ":
		d=json.loads(x)
		Data.append(d)
print(Data)

def BusThaneToPune():
	Time="please choose from given timings- 7:00/12:00/20:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 270/-  Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:00":
		Pay="total Pay = 280/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:30":
		Pay="total Pay = 300/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)



def BusKalwaToPune():
	Time="please choose from given timings- 7:15/12:15/20:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 250/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:15":
		Pay="total Pay = 270/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:45":
		Pay="total Pay = 390/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusVitawaToPune():
	Time="please choose from given timings- 7:30/12:30/21:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 240/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:30":
		Pay="total Pay = 260/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:00":
		Pay="total Pay = 380/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusKalwaToDhule():
	Time="please choose from given timings- 9:15/13:15/23:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:15":
		Pay="total Pay = 540/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:15":
		Pay="total Pay = 558/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:45":
		Pay="total Pay = 580/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusThaneToDhule():
	Time="please choose from given timings- 9:00/13:00/23:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:00":
		Pay="total Pay = 560/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:00":
		Pay="total Pay = 578/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:30":
		Pay="total Pay = 600/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusVitawaToDhule():
	Time="please choose from given timings- 9:30/13:30/24:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:30":
		Pay="total Pay = 535/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:30":
		Pay="total Pay = 553/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="24:00":
		Pay="total Pay = 575/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusKalwaToBeed():
	Time="please choose from given timings- 7:15/15:15/21:55"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 505/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:15":
		Pay="total Pay = 523/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:55":
		Pay="total Pay = 545/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusThaneToBeed():
	Time="please choose from given timings- 7:00/15:00/21:40"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 525/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:00":
		Pay="total Pay = 543/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:40":
		Pay="total Pay = 565/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusVitawaToBeed():
	Time="please choose from given timings- 7:30/15:30/22:10"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 500/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:30":
		Pay="total Pay = 513/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="22:10":
		Pay="total Pay = 535/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusFromVitawa():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		BusVitawaToPune()
	elif fourth_reply=="Dhule":
		BusVitawaToDhule()
	elif fourth_reply=="Beed":
		BusVitawaToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)





def BusFromKalwa():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		BusKalwaToPune()
	elif fourth_reply=="Dhule":
		BusKalwaToDhule()
	elif fourth_reply=="Beed":
		BusKalwaToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusFromThane():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		BusThaneToPune()
	elif fourth_reply=="Dhule":
		BusThaneToDhule()
	elif fourth_reply=="Beed":
		BusThaneToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusOn19():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		BusFromThane()
	elif third_reply=="Kalwa":
		BusFromKalwa()
	elif third_reply=="Vitawa":
		BusFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusOn20():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		BusFromThane()
	elif third_reply=="Kalwa":
		BusFromKalwa()
	elif third_reply=="Vitawa":
		BusFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def BusOn21():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		BusFromThane()
	elif third_reply=="Kalwa":
		BusFromKalwa()
	elif third_reply=="Vitawa":
		BusFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def BusRoute():
	Date="Booking for Bus!! Enter the Date: dd/mm/yyyy"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Date)
	time.sleep(10)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(10)

	second_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	second_reply=second_message.text
	if second_reply=="19/03/2022":
		BusOn19()	
	elif second_reply=="20/03/2022":
		BusOn20()	
	elif second_reply=="21/03/2022":
		BusOn21()
	else: 
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
		



		
	





def TrainDadarToKarnataka():
	Time="please choose from given timings- 7:00/12:00/20:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 2700/-  Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:00":
		Pay="total Pay = 2800/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:30":
		Pay="total Pay = 3000/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)



def TrainCSTToKarnataka():
	Time="please choose from given timings- 7:15/12:15/20:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 2500/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:15":
		Pay="total Pay = 2700/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:45":
		Pay="total Pay = 3900/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainKurlaToKarnataka():
	Time="please choose from given timings- 7:30/12:30/21:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 2400/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:30":
		Pay="total Pay = 2600/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:00":
		Pay="total Pay = 3800/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainDadarToKashmir():
	Time="please choose from given timings- 9:15/13:15/23:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:15":
		Pay="total Pay = 5400/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:15":
		Pay="total Pay = 5580/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:45":
		Pay="total Pay = 5800/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainCSTToKashmir():
	Time="please choose from given timings- 9:00/13:00/23:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:00":
		Pay="total Pay = 5600/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:00":
		Pay="total Pay = 5780/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:30":
		Pay="total Pay = 6000/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainKurlaToKashmir():
	Time="please choose from given timings- 9:30/13:30/24:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:30":
		Pay="total Pay = 5350/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:30":
		Pay="total Pay = 5530/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="24:00":
		Pay="total Pay = 5750/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainDadarToDelhi():
	Time="please choose from given timings- 7:15/15:15/21:55"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 5050/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:15":
		Pay="total Pay = 5230/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:55":
		Pay="total Pay = 5450/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainCSTToDelhi():
	Time="please choose from given timings- 7:00/15:00/21:40"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 5250/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:00":
		Pay="total Pay = 5430/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:40":
		Pay="total Pay = 5650/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainKurlaToDelhi():
	Time="please choose from given timings- 7:30/15:30/22:10"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 5000/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:30":
		Pay="total Pay = 5130/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="22:10":
		Pay="total Pay = 5350/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainFromKurla():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Delhi":
		TrainKurlaToDelhi()
	elif fourth_reply=="Kashmir":
		TrainKurlaToKashmir()
	elif fourth_reply=="Karnataka":
		TrainKurlaToKarnataka()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)





def TrainFromDadar():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Delhi":
		TrainDadarToDelhi()
	elif fourth_reply=="Kashmir":
		TrainDadarToKashmir()
	elif fourth_reply=="Karnataka":
		TrainDadarToKarnataka()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainFromCST():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Delhi":
		TrainCSTToDelhi()
	elif fourth_reply=="Kashmir":
		TrainCSTToKashmir()
	elif fourth_reply=="Karnataka":
		TrainCSTToKarnataka()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainOn19():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="CST":
		TrainFromCST()
	elif third_reply=="Dadar":
		TrainFromDadar()
	elif third_reply=="Kurla":
		TrainFromKurla()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainOn20():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="CST":
		TrainFromCST()
	elif third_reply=="Dadar":
		TrainFromDadar()
	elif third_reply=="Kurla":
		TrainFromKurla()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def TrainOn21():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="CST":
		TrainFromCST()
	elif third_reply=="Dadar":
		TrainFromDadar()
	elif third_reply=="Kurla":
		BusFromKurla()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def TrainRoute():
	Date="Booking for Train!!! Enter the Date: dd/mm/yyyy"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Date)
	time.sleep(10)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(10)

	second_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	second_reply=second_message.text
	if second_reply=="19/03/2022":
		TrainOn19()	
	elif second_reply=="20/03/2022":
		TrainOn20()	
	elif second_reply=="21/03/2022":
		TrainOn21()
	else: 
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
			
		

	



def CarThaneToPune():
	Time="please choose from given timings- 7:00/12:00/20:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 270/-  Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:00":
		Pay="total Pay = 280/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:30":
		Pay="total Pay = 300/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)



def CarKalwaToPune():
	Time="please choose from given timings- 7:15/12:15/20:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 250/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:15":
		Pay="total Pay = 270/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="20:45":
		Pay="total Pay = 390/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarVitawaToPune():
	Time="please choose from given timings- 7:30/12:30/21:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 240/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="12:30":
		Pay="total Pay = 260/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:00":
		Pay="total Pay = 380/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarKalwaToDhule():
	Time="please choose from given timings- 9:15/13:15/23:45"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:15":
		Pay="total Pay = 540/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:15":
		Pay="total Pay = 558/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:45":
		Pay="total Pay = 580/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarThaneToDhule():
	Time="please choose from given timings- 9:00/13:00/23:30"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:00":
		Pay="total Pay = 560/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:00":
		Pay="total Pay = 578/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="23:30":
		Pay="total Pay = 600/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarVitawaToDhule():
	Time="please choose from given timings- 9:30/13:30/24:00"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="9:30":
		Pay="total Pay = 535/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="13:30":
		Pay="total Pay = 553/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="24:00":
		Pay="total Pay = 575/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarKalwaToBeed():
	Time="please choose from given timings- 7:15/15:15/21:55"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:15":
		Pay="total Pay = 505/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:15":
		Pay="total Pay = 523/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:55":
		Pay="total Pay = 545/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarThaneToBeed():
	Time="please choose from given timings- 7:00/15:00/21:40"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:00":
		Pay="total Pay = 525/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:00":
		Pay="total Pay = 543/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="21:40":
		Pay="total Pay = 565/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarVitawaToBeed():
	Time="please choose from given timings- 7:30/15:30/22:10"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Time)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)
	fifth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fifth_reply=fifth_message.text
	if fifth_reply=="7:30":
		Pay="total Pay = 500/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="15:30":
		Pay="total Pay = 513/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	elif fifth_reply=="22:10":
		Pay="total Pay = 535/- Please send CONFIRMED message, once done payment."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Pay)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarFromVitawa():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		CarVitawaToPune()
	elif fourth_reply=="Dhule":
		CarVitawaToDhule()
	elif fourth_reply=="Beed":
		CarVitawaToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)





def CarFromKalwa():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		CarKalwaToPune()
	elif fourth_reply=="Dhule":
		CarKalwaToDhule()
	elif fourth_reply=="Beed":
		CarKalwaToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarFromThane():
	ToLoc=" location To? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(ToLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	fourth_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	fourth_reply=fourth_message.text
	if fourth_reply=="Pune":
		CarThaneToPune()
	elif fourth_reply=="Dhule":
		CarThaneToDhule()
	elif fourth_reply=="Beed":
		CarThaneToBeed()	
	else :
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarOn19():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		CarFromThane()
	elif third_reply=="Kalwa":
		CarFromKalwa()
	elif third_reply=="Vitawa":
		CarFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarOn20():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		CarFromThane()
	elif third_reply=="Kalwa":
		CarFromKalwa()
	elif third_reply=="Vitawa":
		CarFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)

def CarOn21():
	FromLoc=" location From? "
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(FromLoc)
	time.sleep(15)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(15)

	third_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	third_reply=third_message.text
	if third_reply=="Thane":
		CarFromThane()
	elif third_reply=="Kalwa":
		CarFromKalwa()
	elif third_reply=="Vitawa":
		CarFromVitawa()
	else:
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)


def CarRoute():
	Date="Booking for Car!! Enter the Date: dd/mm/yyyy"
	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(Date)
	time.sleep(10)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(10)

	second_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	second_reply=second_message.text
	if second_reply=="19/03/2022":
		CarOn19()	
	elif second_reply=="20/03/2022":
		CarOn20()	
	elif second_reply=="21/03/2022":
		CarOn21()
	else: 
		end_message="Sorry no allotment available..."
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(end_message)
		time.sleep(15)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(15)
	time.sleep(30)


def AskRoute():
	New_message=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
	reply_message=New_message.text

	if reply_message=="Bus":
		BusRoute()
	elif reply_message=="Train":
		TrainRoute()
	elif reply_message=="Car":
		CarRoute()
	else:
		print("Exiting the program....")		

	time.sleep(20)

def Choice():
	text="Choose one route from Car/Train/Bus"

	type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
	reply=type_message.send_keys(text)
	time.sleep(10)
	send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
	send=send_button.click()
	time.sleep(10)
	AskRoute()

IntNumber= contact
for i in Data:
	if i['Contact']==IntNumber:
		print("number exixts")
		VerifyPass= " Welcome Back to MakeMyTrip!!!Enter the Password"
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(VerifyPass)
		time.sleep(20)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(20)
		Pass=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
		VPass_reply=Pass.text
		time.sleep(15)
		if i['Password'] == VPass_reply:
			print("Password found")
			Choice()
		

	else:
		print("no...")
		Email= "Welcome to MakeMyTrip!!!Enter your email-id for registration"
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Email)
		time.sleep(30)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(30)
		EmailInfo=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
		Email_reply=EmailInfo.text
		print("Email...")

		Password= "Enter the Password"
		type_message=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
		reply=type_message.send_keys(Password)
		time.sleep(30)
		send_button=browser.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k")
		send=send_button.click()
		time.sleep(30)
		PassInfo=browser.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(3) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span > span")
		Pass_reply=PassInfo.text
		Choice()


		d={
			"Contact": contact,
			"Email": Email_reply,
			"Password": Pass_reply

		}
		f=open("data.txt", "a")
		f.write("\n")
		json.dump(d, f)
f.close()
