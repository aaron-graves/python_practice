import datetime, time

#get date and modify it to label the new file
date = datetime.datetime.now()
date = date.strftime("%m-%d-%y.%H%M")

#creates html file named with date and writes some content
newHTML=open(date+".html","w")
newHTML.write("<body style='background-color:#D2B48C;'>" +
              "<center><h1>This was created by Python!</h1><br>" + 
              "<img src='http://weknowyourdreams.com/images/python/python-05.jpg'><br><br>"+
              "This will be fancier <em>later</em>...</center>")

#end
print("File created!")