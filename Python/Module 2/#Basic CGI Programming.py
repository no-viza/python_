#Basic CGI Programming

#Step 1: Download a web server 
#havent done it but will make notes on how to do it

#!/usr/bin/python (this is python directory)

print ("Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<title>My first CGI App</title>")
print("</head>")
print("<body>")
print("<h3>This is html </h3>")
print("</body>")
print("</html>")

#< = start
#</ = end
#the above is how to design a web page in html using python

#Get method
#Method used to handle a get request using any form using python

#!/usr/bin/python (this is python directory)

import cgi, cgitb

form = cgi.FieldStorage

username = form["username"].value
emailaddress = form["emailaddress"].value

print ("Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<title>My first CGI App</title>")
print("</head>")
print("<body>")
print("<h3>This is html </h3>")
print(username)
print(emailaddress)
print("</body>")
print("</html>")

#Make a separate file for this get method to work
#format below

<html>
    <head>
        <meta charset="UTF-8">
        <title>Epic Title</title>
    </head>

    <body>
        <form action="File.py" method="GET">
            Username: <input type="text" name="username" />
            <br />

            Email Address: <input type ="email" name="emailaddress" />

            <input type="submit" value="Submit" />
        </form>
    </body>
</html>

#Post Method
#Both the Get method and Post method are essentially the same
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Epic Title</title>
    </head>

    <body>
        <form action="File.py" method="POST">
            Username: <input type="text" name="username" />
            <br />

            Email Address: <input type ="email" name="emailaddress" />

            <input type="submit" value="Submit" />
        </form>
    </body>
</html>

#GET and POST Method Differences
#i) Values stay in the URL hence, is great for bookmarking/history
#NOT the same case for POST

#ii)Get requests can be re-executed but may NOT be re-submitted 
#POST method warns the user that the data might need to be re-submitted

#iii)Coding type is slightly different

#iv)GET is very easy to hack. POST is NOT

#v)GET has restriction in the data type (ASCII ONLY) that can be submitted. POST does NOT

#vi)GET is less secure. POST is more secure

#vii)Form length: GET (Less). POST (more)

#viii) GET NOT for passwords or such info. POST is suitable

#ix)all info is displayed on GET. in POST, its hidden

#x)GET can be cached. POST is NOT
