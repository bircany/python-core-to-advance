email = "info@sadikturan.com" #from db
parola = "12345"
if(email == "info@sadikturan.com"):
    if(parola == "12345"):
        print("Kullanıcı Giriş Yaptı")
    else:
        print("Parola Hatalı")
else:
    print("Email Hatalı")


if(email != "info@sadikturan.com"):
    print("Email Hatalı")
elif(parola != "12345"):
    print("parola yanlış")
else:
    print("Login olundu")

x = 10
y = 20
if(x < y):
    print("x y'den küçük")
elif(x == y):
    print("x ve y eşit")
else:
    print("x y'den büyük")