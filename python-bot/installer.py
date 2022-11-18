import pip
packages = ['selenium','requests','pyzmail36','beautifulsoup4','pyautogui','send2trash','pillow','imapClient','openpyxl','twilio','PyPDF2']

for pkg in packages:
    pip.main(['install',pkg])