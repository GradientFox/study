import os, shutil

# curent_path = os.getcwd() - вернет рабочую директорию, которая открыта в консоли
# у меня запускаемый файл находится на в рабочей директории VSC, поэтому такой вариант не подходит

file_location = os.path.dirname(os.path.abspath(__file__))

print(file_location)
new_dir = os.path.join(file_location, "Управление_файлами")
os.mkdir(new_dir)
file1 = os.path.join(new_dir, "file1.txt")
file2 = os.path.join(new_dir, "file2.txt")
with open(file1, "w", encoding="utf-8") as f:
    f.write("Привет")
with open(file2, "w", encoding="utf-8") as f:
    f.write("Пока")
print(os.listdir(new_dir))

temp = input("Press Enter to continue...")

os.remove(file2)
inner = os.path.join(new_dir, "Секретно")
os.mkdir(inner)
shutil.move(file1, inner)

temp = input("Press Enter to continue...")

shutil.rmtree(new_dir)