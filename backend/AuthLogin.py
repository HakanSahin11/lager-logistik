from contextlib import nullcontext
import bcrypt

from backend.DBConnections import GetLoginUser

def loginMethod(passw, username):
    SavedUser = GetLoginUser(username)
    if(SavedUser):
        # index 0 = username
        # index 1 = passw
        pwMatch = bcrypt.checkpw(passw.encode('utf-8'), SavedUser[1].encode('utf-8') )
        return pwMatch
    return False