from passwd_check import passwd_check
import password_check_test

test = password_check_test.Password_check_test()
password = passwd_check()
test.test_goodPassword(password)
test.test_badPassword(password)