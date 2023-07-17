import os

def delete_files_and_folders(destination):
  """
  Function that deletes files and folder in destination folder path
  :param destination: str
  :return: None
  """
  if os.path.isdir(destination):
    for file in os.listdir(destination):
      p = os.path.join(destination, file)
      if os.path.isdir(p):
        delete_files_and_folders(p)
      else:
        try:
          os.remove(p)
        except:
          print("Could not remove file {}".format(p))
    try:
      os.rmdir(destination)
    except:
      print ("Could not remove directory {}".format(destination))