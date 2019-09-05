## director base to append to python path
from src.app import create_app
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
import sys
sys.path.append(BASE_DIR)