import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.producto import *
from models.usuario import *
from models.compra import *
from models.detalle_compra import *
