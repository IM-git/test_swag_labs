class Login:
    USERNAME_FIELD = "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    ELEMENT_IMG = "//div[@class='bot_column']"
    LIST_NAMES = ['standard_user',
                  'locked_out_user',
                  'problem_user',
                  'performance_glitch_user']
    PASSWORD = "secret_sauce"
    BUTTON = "//input[@id='login-button']"
