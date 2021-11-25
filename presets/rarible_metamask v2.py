###IMPORTANT####    Only works with MetaMask and RARI collections on the Rarible   ###IMPORTANT###

#make sure to set your variables below for this script, examples provided

#####VARIABLE START####### (FILL BEFORE STARTING) ####
start_num = 8707
listing_option='Open for bids' ### 'Timed auction' ### 'Fixed price' ###change 'Open for bids' as desired##
loop_price = 0.075
loop_title = "#"
loop_file_format = "png"
loop_description = "My personal collection of planets from the Cryptoverse Planets series."
royalties = "10"
#####VARIABLES END########



while loop_amount != 0:
	while True:
		try:
			print("Uploading: " + str(start_num) + "  -  " + str(loop_amount) + " to go...")
			driver.switch_to.window(driver.window_handles[0])
			go_to("https://rarible.com/create")
			css_and_click("button[id='create-single']")
			css_and_click("button[data-marker='restore-modal/discardButton']")
			break
		except Exception as wtf:
			#print(wtf)
			#print("----- retrying uploading -----")
			break

	while True:
		try:
			if opsys == "Windows":
				imagePath = os.path.abspath(file_folder + "\\" + str(start_num) + "." + loop_file_format)
			elif opsys == "Darwin":
				imagePath = os.path.abspath(file_folder + "/" + str(start_num) + "." + loop_file_format)
			else:
				imagePath = os.path.abspath(file_folder + "\\" + str(start_num) + "." + loop_file_format)
			css_and_key("input[name='primary-attachment']", imagePath)
			css_and_click("img[alt='{list_op}']".format(list_op = listing_option)) 

			if listing_option == "Fixed price":
				css_and_key("input[data-marker='root/appPage/create/form/price/input/priceInput']", loop_price)
			elif listing_option == "Timed auction":
				print("please contact @cloudmaking on twitter or instagram to request a custom preset for this listing option")
			elif listing_option == "Open for bids":
				pass
			else:
				print("please pick listing option")

			css_and_key("input[data-marker='root/appPage/create/form/nameInput']", loop_title+str(start_num))
			css_and_key("textarea[data-marker='root/appPage/create/form/descriptionInput']", loop_description)
			x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "input[inputmode='decimal']")))
			x.send_keys(Keys.BACKSPACE)
			x.send_keys(Keys.BACKSPACE)
			x.send_keys(royalties)  
			main_page = driver.current_window_handle
			css_and_click("button[data-marker='root/appPage/create/form/createButton']")
			break
		except Exception as wtf:
			print(wtf)
			print("----- retrying uploading -----")
			continue

	main_page = driver.current_window_handle
	while True:
		try:
			time.sleep(10) ###adjust this depending on your uplaod speed
			for handle in driver.window_handles:
				if handle != main_page:
					login_page = handle
			driver.switch_to.window(login_page)
			css_and_click("button[class='button btn--rounded btn-primary btn--large']")
			driver.switch_to.window(main_page)
			break
		except Exception as wtf:
			#print(wtf)
			print("----- Waiting for metamask sign window -----")
			continue

	while True:
		try:
			if listing_option == "Fixed price":
				time.sleep(3)
				driver.switch_to.window(driver.window_handles[1])
				css_and_click("button[class='button btn--rounded btn-primary btn--large']")
				time.sleep(1)
				break
			else:
				time.sleep(3)
				driver.switch_to.window(driver.window_handles[1])
				xpath_and_click("//*[@id='app-content']/div/div[2]/div/div[3]/button[2]")
				time.sleep(1)
				break
		except Exception as wtf:
			#print(wtf)
			print("----- Waiting for second metamask sign window -----")
			continue

	driver.switch_to.window(main_page)
	start_num = start_num + 1
	loop_amount = loop_amount - 1
