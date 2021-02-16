import shutil, os, errno

os.chdir('C:\\youpath')


# Source path
srca = 'C:\\yourpath'

# Destination path
desti = 'C:\\Users\stratos\Desktop\wer\wer2'

# Copy the content of
# source to destination
try:
    shutil.copytree(srca, desti)
except OSError as err:

    # error caused if the source was not a directory
    if err.errno == errno.ENOTDIR:
        shutil.copy2(srca, desti)
    else:
        print("Error: % s" % err)
