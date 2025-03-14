###IMPORTANT####    Only works with MetaMask and Ethereum/Polygon collections on the Opensea  ###IMPORTANT###

#make sure to set your variables below for this script, examples provided
#####VARIABLE START####### (FILL BEFORE STARTING) ####
collection_link = "https://opensea.io/collection/cryptoverse-lone-wanderer"
start_num = 9331
loop_price = 0.1
loop_title = "#"
loop_file_format = "png"
loop_external_link = "https://linktr.ee/Cloudmaking"
loop_description = "Lone wanderer is a series of 10000 collectible planets. The Rarity of the planets increases as we reach out max storage limit of 10000."
Collection_type = "polygon" #pick "polygon" or "ethereum"
#####VARIABLES END########

while loop_amount != 0:
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


	while True:
		try:
			####UPLOADING####
			print("Uploading: " + str(start_num) + "  -  " + str(loop_amount) + " to go...")
			#linktext_click("Add item")
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
			###ADD PROPERTIES CODE HERE###
			xpath_and_click('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button')
			break
		except Exception as wtf:
			#print(wtf)
			print("----- Retrying uploading -----")
			continue

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


	###LISTING####
	current_page=driver.current_url
	main_page = driver.current_window_handle

	if Collection_type == "polygon":
		while True:
			try:
				linktext_click("Sell")
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
		print("Please pick either 'polygon' or 'ethereum' / no caps, make sure the spellign is correct")
		break
		
	start_num = start_num + 1
	loop_amount = loop_amount - 1




