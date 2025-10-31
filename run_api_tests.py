import os
import sys
import subprocess

# Configurar la variable de entorno
os.environ['BASE_URL'] = 'http://127.0.0.1:5000'

# Ejecutar pytest
result = subprocess.run([
    sys.executable, '-m', 'pytest',
    'test/rest/',
    '--junit-xml=results/api_result.xml',
    '-v',
    '-m', 'api'
])

sys.exit(result.returncode)
