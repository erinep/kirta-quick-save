# makeZIP.py v0.1
# Purpose: Utility script to create zip archieve of a plugin
# Params: @plugin_folder_name


import os
import sys
from datetime import datetime
import zipfile

cwd = os.getcwd()


def makeZip(plugin_folder_name):
    # create new zip archieve with .desktop and plugin folder contents


    cwd = os.getcwd()
    psrc = os.path.join(cwd, 'src', plugin_folder_name)
    pmeta = os.path.join(cwd, 'src', '{}{}'.format(plugin_folder_name, '.desktop'))

    
    if os.path.exists(psrc) and os.path.exists(pmeta):
        
        zipname = '{}{}.zip'.format(plugin_folder_name, datetime.now().strftime(" %Y_%m_%d %H%M%S"))

        with  zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as zipper:

            zipper.write(pmeta, arcname=os.path.basename(pmeta))

            for _, _, files in os.walk(psrc):
                for file in files:
                    new_file = os.path.join(psrc, file)
                    if(os.path.exists(new_file)):
                        zipper.write(new_file, arcname=f'{plugin_folder_name}/{file}')
    else:
        print('Required files not found. Please make sure your have the following files/folders: \n{} \n{}'.format(psrc,pmeta))



if __name__=="__main__":

    for i in range(1, len(sys.argv)):
        makeZip(sys.argv[i])