import os


def initialice(base_folder = "logs"):
    dirs = os.listdir()
    if not base_folder in dirs:
        os.mkdir(base_folder)

# Files go from out.log1 to out.log5
def rotate_file(base_folder = "logs", base_file_name = "out.log", num_max_files = 5, max_bytes_file = 1000):
    dirs = os.listdir(base_folder)
    file_base = base_folder + "/" + base_file_name
    if len(dirs) >= num_max_files:
        os.remove(file_base + str(num_max_files))
    for i in range(num_max_files, 1, -1):
        os.rename(file_base + str(i-1), file_base + str(i))
    open(file_base + str(1), 'a').close()   
        
    