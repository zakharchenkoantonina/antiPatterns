import shutil

output_dir = 'Output'
shutil.rmtree(output_dir)
print("Deleted '%s' directory successfully" % output_dir)
