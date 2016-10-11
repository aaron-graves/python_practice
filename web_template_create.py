import datetime, time

date = datetime.datetime.now()
date = date.strftime("%m-%d-%y.%H%M")

newHTML=open(date+".html","w")
newHTML.write("<body style='background-color:#D2B48C;'>" +
              "<center><h1>This was created by Python!</h1><br>" + 
              "<img src='http://weknowyourdreams.com/images/python/python-05.jpg'><br><br>"+
              "This will be fancier <em>later</em>...</center>")

print("File created!")