from passwd_check import passwd_check

class Password_check_test():

    def __init__(self):
        pass

    def test_goodPassword(self, toCheck : passwd_check()):
        if toCheck.check_passwd("sK7@v45") == True :
            print ("This password should work and works\n")
        else :
            print ("This password should work but we get the following message : " + toCheck.get_error())
    
    def test_badPassword(self, passwrdCheck : passwd_check) :
        passwrdlist = ["Dc4V_", "Dcfkv_Dqt", "fgt_47_st", "FTG&4FRM0", "gs45HTA4l", "Azertyuiop"]
        for x in passwrdlist :
            if passwrdCheck.check_passwd(passwrdlist) == False :
                print ("Ok for : " + x + "\nWe have this error : \n"+ passwrdCheck.get_error())
            else :
                print ("This password should not work")

    