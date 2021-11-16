import wget
###VARIABLE###PLEASE FILL BEFORE STARITNG####
profile_name= input("Insert account name: ") #without the @ sign
profile_adress= "https://www.instagram.com/{}/".format(profile_name.lower())

go_to(profile_adress)



####(thanks to @Cuong Tran)######
print("\n Scrolling to the bottom \n")
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


##thank you Mariya for this code###her github ### https://github.com/MariyaSha/ ####

#scroll down to scrape more imagess
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]
print('Number of scraped images: ', len(images))
out_of=len(images)
path = os.getcwd()
path = os.path.join(path, profile_name + "s_Pictures")
confirmation=input("\nWould you like to download all the images? Y/N\n")


if confirmation == "Y":
    #create the directory
    if not os.path.exists(path):
        print("making folder")
        os.makedirs(path)

    counter = 0
    for image in images:
        print(str(counter) + "out of " + str(out_of))
        save_as = os.path.join(path, profile_name[0:] + " #" + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1
elif confirmation == "N":
    print("----Stoping main loop----")
else:
    print("You can only confirm with capital Y or N \n ----Restarting----")
    

