import os

def save_dict(dict_to_save, file_path):
    f = open(file_path, "w")
    f.write(dict_to_save)
    f.close()


def load_dict(file_path):
    f = open(file_path, "r")
    f.read()


if __name__ == '__main__':
  if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
  f = open("myfile.txt", "x")
  save_dict({'name': 'hi'}, f)