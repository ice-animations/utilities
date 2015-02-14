import pymel.core as pc
import re
import site
import sys
import logging

version = int(re.search('\\d{4}', pc.about(v=True)).group())
if version in range(2011, 2016):
    site.addsitedir(r"\\vnas\storage\Technical_Backup\Python_Scripts\maya"+str(version)+r"\PyQt")
    import sip
    API_NAMES = ["QDate", "QDateTime", "QString", "QTextStream", "QTime", "QUrl", "QVariant"]
    API_VERSION = 2
    for name in API_NAMES:
        sip.setapi(name, API_VERSION)
    from PyQt4 import uic
else:
    import PySide as PyQt4
    sys.modules["PyQt4"] = PyQt4
    import uiLoader
    import pysideuic as uic
    uic.loadUiType = uiLoader.loadUiType
    import shiboken as sip
    sip.wrapinstance = sip.wrapInstance
    sys.modules['sip'] = sip

for uic_subm in ['.properties', '.uiparser']:
    logger = logging.getLogger(uic.__name__ + uic_subm)
    logger.setLevel(logging.INFO)
