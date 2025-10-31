import sys
import os

# Añadir el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.api import api_application

if __name__ == "__main__":
    api_application.run(host='127.0.0.1', port=5000, debug=False)
