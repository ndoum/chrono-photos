import datetime
import os

photo_dir = 'C:\\Users\\Nia\\Desktop\\Photos\\'


def time_from_name(name):
    """
    Creates datetime object
    The file name format is expected to be:
    IMG_20201206_141838585.jpg
     - first 4 characters are IMG_ or VID_
     - next 8 are year, month, date
     - next 1 is _
     - next 6 are hour, min, seconds
     - the rest are ignored
    :param name: As described above
    :return: float POSIX timestamp similar to time.time()
    """
    date_string = name[4:19]
    dt_obj = datetime.datetime.strptime(date_string, '%Y%m%d_%H%M%S')
    time_taken = dt_obj.timestamp()
    return time_taken


for filename in os.listdir(photo_dir):
    photo_path = photo_dir + filename
    file_time = time_from_name(filename)
    os.utime(photo_path, (file_time, file_time))

