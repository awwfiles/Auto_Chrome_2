####Recommended wait_amount = 5 seconds

###IMPORTANT####    Only works with MetaMask and Ethereum/Polygon collections on the Opensea  ###IMPORTANT###

#make sure to set your variables below for this script, examples provided and rename and put the metadata.json file int eh metadata folder provided
#####VARIABLE START####### (FILL BEFORE STARTING) ####
collection_link = "https://opensea.io/collection/instories"
start_num = 1
loop_price = .008
loop_title = "#"
loop_file_format = "jpg"
loop_external_link = ""
loop_description = ""
number_of_properties = 7 #this will only work with a hashlibs generated json _metadata.json file, 
#please put the metadata file in the folder and name it "metadata.json" 
Collection_type = "polygon" #pick "polygon" or "ethereum"
#####VARIABLES END########

import json
if opsys == "Windows":
	with open('metadata\\metadata.json') as f:
		data = json.load(f)
elif opsys == "Darwin":
	with open('metadata/metadata.json') as f:
		data = json.load(f)
else:
	with open('metadata\\metadata.json') as f:
		data = json.load(f)
print("metadata file found")

while loop_amount != 0:
	print("starting main loop")
	while True:
		try:
			go_to(collection_link+"/assets/create")
			wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main/div/div/section/div[2]/header/h1")))
			break
		except Exception as wtf:
			#print(wtf)
			print("----- Network error, waiting eo seconds before restarting -----")
			time.sleep(30)
			continue

	print("Uploading: " + str(start_num) + "  -  " + str(loop_amount) + " to go...")
	while True:
		try:
			if opsys == "Windows":
				imagePath = os.path.abspath(file_folder + "\\" + str(start_num) + "." + loop_file_format)
			elif opsys == "Darwin":
				imagePath = os.path.abspath(file_folder + "/" + str(start_num) + "." + loop_file_format)
			else:
				imagePath = os.path.abspath(file_folder + "\\" + str(start_num) + "." + loop_file_format)
			xpath_and_key('//*[@id="media"]', imagePath)
			xpath_and_key('//*[@id="name"]', loop_title + str(start_num))
			xpath_and_key('//*[@id="external_link"]', loop_external_link)
			xpath_and_key('//*[@id="description"]', loop_description)
			driver.execute_script("window.scrollTo(0, 1000);")
			css_and_click("button[aria-label='Add properties']")
			time.sleep(2)
			break
		except Exception as wtf:
			#print(wtf)
			print("----- Retrying uploading -----")
			continue

	print("adding properties for " + str(start_num))
	for x in range(1, 11):
		try:
			print(f"trying {x} div")
			for i in range(1, number_of_properties + 1):
				current_trait = data[start_num - 1]["attributes"][i - 1]["trait_type"]
				current_value = data[start_num - 1]["attributes"][i - 1]["value"]
				xpath_and_key(f'/html/body/div[{x}]/div/div/div/section/table/tbody/tr[{i}]/td[1]/div/div/input', current_trait)
				xpath_and_key(f'/html/body/div[{x}]/div/div/div/section/table/tbody/tr[{i}]/td[2]/div/div/input', current_value)
				xpath_and_click(f"/html/body/div[{x}]/div/div/div/section/button")

			xpath_and_click(f"/html/body/div[{x}]/div/div/div/footer/button")
			break
		except Exception as wtf:
			print(wtf)
			print("----- {x} not found -----")
			continue

	print("clicking create")
	while True:
		try:
			#click create
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			xpath_and_click("/html/body/div[1]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button")
			break
			break
		except Exception as wtf:
			#print(wtf)
			print("----- click nto found, retrying -----")
			continue

	print("waiting for upload confirmation")
	while True:
		try:
			css_and_click("i[aria-label='Close']")
			time.sleep(1)
			break
		except Exception as wtf:
			#print(wtf)
			print("----- upload complete, No upload confirmation, reloading page to start listing -----")
			#current_page=driver.current_url
			#go_to(current_page)
			break

	print("listing for sale")
	###LISTING####
	current_page=driver.current_url
	main_page = driver.current_window_handle

	if Collection_type == "polygon":
		while True:
			try:
				go_to(f"{current_page}/Sell")
				css_and_key("input[placeholder='Amount']", str(loop_price))
				css_and_click("button[type='submit']")
				####click sign to open metamask
				xpath_and_click("/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button") ###change this code if the script doesn't press the sign button
				time.sleep(2)
				for handle in driver.window_handles:
					if handle != main_page:
						login_page = handle
				driver.switch_to.window(login_page)
				css_and_click("button[data-testid='request-signature__sign']")
				time.sleep(1)
				driver.switch_to.window(main_page)
				css_and_click("i[aria-label='Close']")
				break
			except Exception as wtf:
				#print(wtf)
				print("----- refreshing and retrying ----- if this occurs alot you might have to change the class code for the sign button")
				go_to(current_page)
				continue
	elif Collection_type == "ethereum":
		while True:
			try:
				linktext_click("Sell")
				css_and_key("input[placeholder='Amount']", str(loop_price))
				css_and_click("button[type='submit']")
				time.sleep(15) #change this depending on how quickly the metamask notification comes up
				driver.switch_to.window(driver.window_handles[1])
				xpath_and_click("//*[@id='app-content']/div/div[2]/div/div[3]/button[2]")
				time.sleep(1)
				driver.switch_to.window(main_page)
				time.sleep(1)
				break
			except Exception as wtf:
				print(wtf)
				print("----- refreshing and trying -----")
				go_to(current_page)
				continue
	else:
		print("Please pick either 'polygon' or 'ethereum' / no caps, make sure the spelling is correct")
		break
		
	start_num = start_num + 1
	loop_amount = loop_amount - 1





