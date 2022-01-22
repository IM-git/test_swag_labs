from enum import Enum


# MESSAGES FOR ASSERTS IN TEST FILES

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected!!'
    WRONG_TITLE_PAGE = 'Another page is open!!'
    WRONG_IS_DISPLAYED = 'The page is not loaded!!'
    