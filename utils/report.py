import subprocess
from _pytest.main import Session


def run_report():
    """Generates reports and show them in a browser"""
    subprocess.call(['allure', 'serve', 'reports'])
