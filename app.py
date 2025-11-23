from flask import Flask, jsonify
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/run-tests', methods=['GET'])
def run_tests():
    """Execute the Selenium test suite using pytest and return the result.
    The command is run in a subprocess so that any stdout/stderr from the test
    execution is captured and returned as JSON. This endpoint is intended for
    local or internal use; it does not perform authentication.
    """
    # Ensure the working directory is the project root
    cwd = os.path.abspath(os.path.dirname(__file__))
    # Run pytest with -s to allow prints and capture output
    result = subprocess.run([sys.executable, '-m', 'pytest', '-s', 'tests'], cwd=cwd,
                            capture_output=True, text=True)
    return jsonify({
        'returncode': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr
    })

if __name__ == '__main__':
    # Run the Flask development server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
