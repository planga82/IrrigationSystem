import os


def initialice(base_folder = "logs"):
    dirs = os.listdir()
    if not base_folder in dirs:
        os.mkdir(base_folder)

# Files go from out.log1 to out.log5
def rotate_file(base_folder = "logs", base_file_name = "out.log", num_max_files = 5):
    dirs = os.listdir(base_folder)
    file_base = base_folder + "/" + base_file_name
    num_files = len(dirs)
    if num_files >= num_max_files:
        os.remove(file_base + str(num_max_files))
        num_files = num_files - 1
    for i in range(num_files + 1, 1, -1):
        os.rename(file_base + str(i - 1), file_base + str(i))
    open(file_base + str(1), 'a').close()   
        
def write_log_line(line, base_folder = "logs", base_file_name = "out.log", max_bytes_file = 1000):
    initialice()
    file_base = base_folder + "/" + base_file_name
    open(file_base + str(1), 'a').close()
    byte_size = os.stat(file_base + str(1))[6]
    if (byte_size > max_bytes_file):
        rotate_file()
    file = open(file_base + str(1), 'a')
    file.write(line + "\n")
    file.flush()
    file.close()
    
for x in range(210):
    write_log_line("0123456789")