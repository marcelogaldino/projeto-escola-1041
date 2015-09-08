
import webapp2

import hashlib


mainForm = """

<html>
<head>
<title>Cadastro</title>
</head>

<body>
<h1>Cadastro</h1>
<form method="post">
    
<label>
Nome do usuario 
<input type="text" name="login">
</label>  
<br>
<br>
    
<label>
E-mail 
<input type="text" name="email">
</label>
<br>
<br>
    
<label>
Senha 
<input type="text" name="password">
</label>    
<br>
<br>

<input type="submit" value="Cadastrar">

</form>
</body>
</html>

"""


responseForm = """

<html>

  <head>

    <title>BashWiki</title>

  </head>

  <body>

    <p>%(password)s criptografado usando sha512: %(cypher)s</p>

  </body>

</html>

"""



class MainHandler(webapp2.RequestHandler):

    def get(self):

        self.response.out.write( mainForm )

    def post(self):

        password = self.request.get('password')

        self.response.out.write( responseForm % 

            { 'password': password, 'cypher': hashlib.sha512( password ).hexdigest() } )



app = webapp2.WSGIApplication([

    ('/', MainHandler)

], debug=True)



