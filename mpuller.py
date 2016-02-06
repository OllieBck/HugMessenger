#!/usr/bin/python

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
soundList = []
timeList = []
playFile = []
fileName = '/home/pi/Google/CodeFiles/message.m4a'

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    if file1['mimeType'] == 'audio/mp4' or file1['mimeType'] == 'audio/mpeg' or file1['mimeType'] == 'audio/x-wav':
        soundFile = drive.CreateFile({'id': file1['id']})
        playFile.append(soundFile['id'])
        soundList.append(soundFile['createdDate'])

for i in range(0, len(soundList)):
    soundList.append(i)
    timeList.append(datetime.strptime(soundList[i], '%Y-%m-%dT%H:%M:%S.%fZ'))
    if max(timeList) == timeList[i]:
        playSong = drive.CreateFile({'id': playFile[i]})
        playSong.GetContentFile(fileName)
        print 'song: %s' % (playSong['title'])

