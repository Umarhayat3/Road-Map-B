import ftplib
import pathlib
ftp = ftplib.FTP('tgftp.nws.noaa.gov')
msg = ftp.login()
print(msg)
msg = ftp.cwd('data')
print(msg)

file_list = ftp.nlst('observations/metar/decoded/')
ARCHIVE = pathlib.Path('Archive')

for file in file_list:
    file_name = pathlib.Path(file).name
    x = ftp.retrbinary('RETR observations/metar/decoded/'+str(file_name),
                        open(ARCHIVE.joinpath(file_name), 'wb').write)

