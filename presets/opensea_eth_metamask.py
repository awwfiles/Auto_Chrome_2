#####VARIABLE START####### (FILL BEFORE STARTING) ####
file_path = "K:\\2021 Backups\\Blender\\projects\\Crypto-Verse\\Gen Season\\5001_6000"     #keep the ##\\##
collection_link = "https://opensea.io/collection/cryptoverse-lone-wanderer"
start_num = 5635
loop_price = 0.075
loop_title = "#"
loop_file_format = "png"
loop_external_link = "https://linktr.ee/Cloudmaking"
loop_description = "Lone wanderer is a series of 10000 collectible planets. The Rarity of the planets increases as we reach out max storage limit of 10000."
#####VARIABLES END########

while loop_amount != 0:
	while True:
		try:
			####UPLOADING####
			print("Uploading: " + str(start_num) + "  -  " + str(loop_amount) + " to go...")
			go_to(collection_link)
			linktext_click("Add item")
			imagePath = os.path.abspath(file_path + "\\" + str(start_num) + "." + loop_file_format)
			xpath_and_key('//*[@id="media"]', imagePath)
			xpath_and_key('//*[@id="name"]', loop_title + str(start_num))
			xpath_and_key('//*[@id="external_link"]', loop_external_link)
			xpath_and_key('//*[@id="description"]', loop_description)
			###ADD PROPERTIES CODE HERE###
			xpath_and_click('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button')
			css_and_click("i[aria-label='Close']")
			break
		except Exception as wtf:
			print(wtf)
			print("----- retrying uploading -----")
			continue

    main_page = driver.current_window_handle
    current_page=driver.current_url
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


    start_num = start_num + 1
    loop_amount = loop_amount - 1
