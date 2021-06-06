import dropbox
import os

from dropbox.files import WriteMode

class TransferFiles:
    def __init__(self,accessToken):
       self.accessToken = accessToken

    def uploadSomething(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.accessToken)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

                    
def main():
    accessToken = 'sl.AyMb6YcrVv-1UNg-aPPxPRznQv7xWNJe3SfRRGdmI5HYhh37GUctllVXM7iDPjy1fZ-ZuUCU1yplxbOxKC_BHby8rL_sXdC6G58ovrL95sOHu1QI5Wi6r2RV4G34KBynKjwu-mQ'                    
    transferFiles = TransferFiles(accessToken)
    file_from = input('Enter file path to tranfer')
    file_to = input('Enter dropbox path')
    transferFiles.uploadSomething(file_from,file_to)
    print('Files moved to dropbox')

main()    