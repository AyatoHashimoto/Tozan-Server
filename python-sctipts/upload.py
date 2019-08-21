import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

drive= GoogleDrive()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

f = drive.CreateFile({'title': 'TEST.TXT'})
f.SetContentString('Hello')
f.Upload()

