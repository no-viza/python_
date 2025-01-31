#Cookies

import Cookie
#Cookies allow you to set data and are stoed with one's browser session
#cookies save data for future use

#!/usr/bin/python (this is python directory)

cook = Cookie.SimpleCookie()
cook["UserID"] = "picko"
cook["UserID"]["expires"] = 60 * 60 * 24 
#Time should be in seconds hence the conversion above
#setting it for a year (*365)

#how to delete a cookie
#cook["UserID"]["expires"] = "Thu, 01, Jan 1970 
#00:00:00 GMT"
#set an expire date before the current date

print (cook)

print ("Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<title>My first CGI App</title>")
print("</head>")
print("<body>")
print("<h3>This is html </h3>")
print(cook["UserID"].value)
#To retrieve the cookie data
print("</body>")
print("</html>")

