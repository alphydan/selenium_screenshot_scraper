from selenium import webdriver

list_of_websites = [
'http://www.google.com',
'https://www.yahoo.com/',
'https://duckduckgo.com/'
]


# Create the webdriver
br = webdriver.PhantomJS()

# loop over the websites
for web in list_of_websites:
    br.get(web)
    #name the output picture
    file_name = web.split('www.')
    if len(file_name) > 1:
        file_name = file_name[1].split('/')[0]
    else:
        file_name = file_name[0].split('://')[1].split('/')[0]

    # Save each file to the /img/ directory
    br.save_screenshot('./img/'+file_name+'.png')
    print web, 'saved as:', file_name+'.png'

br.quit
