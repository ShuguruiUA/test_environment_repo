import os
import re
import shutil
import sys

name_dir = []
path_dir = []
name_file = []
path_file = []
new_name_file = []
trans_map = {}
images_obj = []
video_obj = []
doc_obj = []
audio_obj = []
arh_obj = []
ident_ext = set()
unident_ext = set()

images_file = ['jpeg', 'png', 'jpg', 'svg', 'JPEG', 'PNG', 'JPG', 'SVG']
video_file = ['avi', 'mp4', 'mov', 'mkv', 'AVI', 'MP4', 'MOV', 'MKV']
doc_file = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
audio_file = ['mp3', 'ogg', 'wav', 'amr', 'MP3', 'OGG', 'WAV', 'AMR']
arh_file = ['zip', 'gz', 'tar', 'ZIP', 'GZ', 'TAR']
cyril_sym = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
transl_sym = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


# метод пошуку всіх файлів і папок у заданій папці
def search_dir(path):
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            name_dir.append(i)
            path_dir.append(path)
            search_dir(path + '\\' + i)
        else:
            name_file.append(i)
            path_file.append(path)
    return name_dir, path_dir, name_file, path_file

# метод створення мапи для транскипції з киоилиці на латиницю
def create_trans_dict():
    for c, l in zip(cyril_sym, transl_sym):
        trans_map[ord(c)] = l
        trans_map[ord(c.upper())] = l.upper()
    return trans_map

# метод виконання транскрипції  
def normalize():
    file_in_list = []
    for i, value in enumerate(name_file):
        file_in_list = value.split('.')
        file_in_list[0] = file_in_list[0].translate(trans_map)
        file_in_list[0] = re.sub('\W', '_', file_in_list[0])
        new_name_file.append('.'.join(file_in_list[i] for i in range(len(file_in_list))))
        os.rename(os.path.join(path_file[i], value), os.path.join(path_file[i], new_name_file[i]))
    return new_name_file

# метод розміщення файлів у папки відповідно до їх розширень
def move_file(path):
    for i, value in enumerate(new_name_file):
        file_in_list = value.split('.')
        ident_ext.add(file_in_list[-1])
        if file_in_list[-1] in images_file:
            if not os.path.exists(os.path.join(path, 'images')):
                os.mkdir(os.path.join(path, 'images'))
            shutil.move(os.path.join(path_file[i], value), os.path.join(path, 'images', value))
            images_obj.append(value)
        elif file_in_list[-1] in video_file:
            if not os.path.exists(os.path.join(path, 'video')):
                os.mkdir(os.path.join(path, 'video'))
            shutil.move(os.path.join(path_file[i], value), os.path.join(path, 'video', value))
            video_obj.append(value)
        elif file_in_list[-1] in doc_file:
            if not os.path.exists(os.path.join(path, 'documents')):
                os.mkdir(os.path.join(path, 'documents'))
            shutil.move(os.path.join(path_file[i], value), os.path.join(path, 'documents', value))
            doc_obj.append(value)
        elif file_in_list[-1] in audio_file:
            if not os.path.exists(os.path.join(path, 'audio')):
                os.mkdir(os.path.join(path, 'audio'))
            shutil.move(os.path.join(path_file[i], value), os.path.join(path, 'audio', value))
            audio_obj.append(value)
        elif file_in_list[-1] in arh_file:
            if not os.path.exists(os.path.join(path, 'archives')):
                os.mkdir(os.path.join(path, 'archives'))
            if not os.path.exists(os.path.join(path, 'archives', file_in_list[0])):
                os.mkdir(os.path.join(path, 'archives', file_in_list[0]))
            shutil.unpack_archive(os.path.join(path_file[i], value), os.path.join(path, 'archives', file_in_list[0]))
            arh_obj.append(value)
            os.remove(os.path.join(path_file[i], value))
        else:
            unident_ext.add(file_in_list[-1])
    return images_obj, video_obj, doc_obj, audio_obj, arh_obj, ident_ext, unident_ext

# видалення пустих директорій
def clean_dir():
    for i, value in enumerate(name_dir):
        try:    
            os.rmdir(os.path.join(path_dir[i], value))
        except OSError:
            print

# мето виводу результатів 
def rezult_hw():
    if len(name_file):
        print(F'Number of files found:{len(name_file)}')
        if len(images_obj):
            print(f'Images: {images_obj}')
        if len(video_obj):
            print(f'Video: {video_obj}')
        if len(doc_obj):
            print(f'Doc: {doc_obj}')
        if len(audio_obj):
            print(f'Audio: {audio_obj}')
        if len(arh_obj):
            print(f'Archives: {arh_obj}')
        print(f'Identified files: {len(ident_ext) - len(unident_ext)} {ident_ext ^ unident_ext if ident_ext ^ unident_ext else ""}')
        print(f'Unidentified files: {len(unident_ext)} {unident_ext if unident_ext else ""}')

# метод запуску сортування папки
def run_func(path):
    try:
        os.listdir(path)
    except OSError:
        print('Make sure the path to the folder you want to sort is correct!')
    else:
        if os.listdir(path):
            search_dir(path)
            create_trans_dict()
            normalize()
            move_file(path)
            clean_dir()
            rezult_hw()
        else:
            print("No objects found to sort.")
            