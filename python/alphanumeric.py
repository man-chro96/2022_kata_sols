def alphanumeric(psw):
    if psw=="": return False
    for i in psw:
        if not (i.isdigit() or i.isalpha()):
            return False
    return True