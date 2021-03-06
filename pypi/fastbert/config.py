# coding: utf-8
import os


__version__ = "0.0.0"


LIB_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(LIB_DIR, 'files/')
TMP_DIR = '/tmp/'


MODEL_CONFIG_FILE = {
        'google_bert_base_en': os.path.join(FILES_DIR, 'google_bert_base_en.json'),
        'google_bert_base_zh': os.path.join(FILES_DIR, 'google_bert_base_zh.json')
    }

DEFAULT_SEQ_LENGTH = 128
DEFAULT_DEVICE = 'cpu'

