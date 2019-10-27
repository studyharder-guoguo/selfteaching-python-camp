from mymodule import stats_word
import traceback
import logging
logger=logging.getlogger(__name__)

def test_traceback():
    try:
        states_word.stats_text(1)
    except Exception as e:
        print('text_traceback =>',e)
        print(traceback.format_exc())

def test_logger():
    try:
        states_word.stats_text(1)
    except Exception as e:
        #print('text_logger =>',e)
        logger.exception(e)

if  __name__=='__main__':
    states_word.stats_text(1)
    test_traceback()
    test_logger()

