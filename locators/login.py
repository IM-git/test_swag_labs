class Login:
    LINK = "https://www.saucedemo.com"
    USERNAME_FIELD = "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    ELEMENT_IMG = "//div[@class='bot_column']"
    LIST_NAMES = ['standard_user',
                  'locked_out_user',
                  'problem_user',
                  'performance_glitch_user']
    PASSWORD = "secret_sauce"
    BUTTON = "//input[@id='login-button']"
    CHECK_LIST_FOR_HEADERS = {'X-GitHub-Request-Id': 'E6B2:F2EB:2F5DF2:309750:61EF4B35',
                              'X-Served-By': 'cache-hhn4081-HHN',
                              'X-Fastly-Request-ID': '5a68eec9ff890c987538cd600d216a02086ed72b',
                              'Last-Modified': 'Mon, 19 Apr 2021 09:51:46 GMT'}
