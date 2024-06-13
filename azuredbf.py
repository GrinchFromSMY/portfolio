from AzureDB import AzureDB


with AzureDB() as a:
    data = a.azureGetData()
    for result in data:
        print("%s napisał : \"%s\"" % (result['name'], result['text']))
