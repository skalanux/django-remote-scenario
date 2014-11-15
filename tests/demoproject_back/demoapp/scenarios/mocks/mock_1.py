from demoapp import utils

to_mock = utils
to_mock_attr = 'get_current_date'

def mock():
    from datetime import date
    return date(2000,1,1)
