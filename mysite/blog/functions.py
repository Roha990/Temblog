from django.conf.global_settings import MEDIA_ROOT


# Функция сохранения изображения
def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
