class passwd_check():
    """Check if the password is valid.

    This function checks the following conditions
    if its length is greater than 6
    if it has at least one uppercase letter
    if it has at least one lowercase letter
    if it has at least one numeral
    if it has any of the required special symbols
    """
    def __init__(self) :
        self.__specialSym=['$','@','#','*','_','-','&']
        self.__digits =['1','2','3','4','5','6','7','8','9','0']
        self.__error = ""
        self.optionPrint = False
    
    def option_print(self, status : bool) :
        self.optionPrint = status
        
    
    def get_error(self) :
        return self.__error

    def check_passwd(self, passwd : str) :

        return_val=True
        self.__error = "Error, This password don't fulfill the expected criteria :\n"

        if len(passwd) < 6:
            self.__error = 'the length of password should be at least 6 char long\n'
            return_val=False

        if not any(self.__digits for char in passwd):
            self.__error = 'the password should include digits\n'
            return_val=False

        if not any(char.isupper() for char in passwd):
            self.__error = 'the password should include uppercase characters\n'
            return_val=False
        

        if not any(char.islower() for char in passwd):
            self.__error = 'the password should include lowercase characters\n'
            return_val=False
        
        if not any(self.__specialSym for char in passwd):
            self.__error = 'the password should include these special characters $  @ # * _ - &\n'
            return_val=False
        
        if return_val == True:
            self.__error ='Ok'
        if self.optionPrint == True :
            print(self.__error)
        return return_val
    
