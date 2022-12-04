# import importlib.util as ilu
#
# folder = '/Users/aylingyoren/Desktop/IT/Python/Apps'
# file = 'odd'
#
# spec = ilu.spec_from_file_location(file, folder)
# my_lib = ilu.module_from_spec(spec)
# spec.loader.exec_module(my_lib)
#
# my_lib

# import sys, os
# my_dir = "/Users/aylingyoren/Desktop/IT/Python/Apps/untitled"
# new_dir = os.path.abspath(os.path.join(my_dir, ".."))
# print(os.listdir(new_dir))
# sys.path.append(new_dir)
# import odd

# import sys
# sys.path.insert(0, "/Users/aylingyoren/Desktop/IT/Python/Apps")
# import odd
