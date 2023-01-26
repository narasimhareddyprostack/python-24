def LoginRequired(f1):
    def innerFun(name,is_Login):
        if is_Login == False:
            print("Login is Required")
        else:
            return f1
    return innerFun
    
    
def homePage(name, is_Login):
    print("Home Page")
    
@LoginRequired    
def orderPage(name, is_Login):
    print("Order Page Page")
@LoginRequired
def productPage(name, is_Login):
    print("Product Page")

homePage("Rahul", True)
orderPage("Rahul", True)
productPage("Rahul", False)