#get method
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