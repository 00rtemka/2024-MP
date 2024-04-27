import random
import math

# ������ ����� ����� �� 0 �� 999999
integers = []
for i in range(100000):
    integers.append(i)
# random.shuffle(integers)

# ������ �� 99999 ��������� ������������ ����� � ��������� [-1, 1]
real_numbers = []
for i in range(10000):
    real_numbers.append(random.uniform(-1, 1))

# 42000 ������ ����� ����������� ���������, ������� ������ ���������� ������� r = birth_day / birth_month
# (����� ���������, ����� ���������� �������������), ����������� �� ������ �����


birth_day = 15
birth_month = 6
max_module = birth_day / birth_month
complex_points = []
while len(complex_points) != 42000:
    radius = random.uniform(0, max_module)
    angle = random.uniform(0, 2 * math.pi)
    complex_points.append([radius * math.cos(angle),
                           radius * math.sin(angle)])

# ������� �� ����� (�����, �� ���� �����) �� ����� 10000 ����, �������� � ������ �� ������
words = []
with open('������� �� �����.txt', encoding='utf-8') as book:
    for line in book:
        for i in (line.split(" ")):
            if i != '\n' and len(words) < 10000:
                words.append(str(i))


# ������ �������� ��� ����������:
# 4 ���������� ��������
# 7 ������ ����������
# 12 ���������� ���������
# 13 ������� (���������) ����������


# ������� ���������� �������� ��� �������������� �����

def insertion(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        # ����� ����������� ������� ���� �� �� ������� �� ������ �����
        while ((j >= 0) and (list[j] > value)):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = value


# ������� ��� ���������� ������ ������������ �����
def module(complex):
    return math.sqrt((complex[0] * complex[0]) + (complex[1] * complex[1]))


# ������� ���������� �������� ��� ���������� �����(����� �������������� �����)
def complex_insertion(list):
    for i in range(1, len(list)):
        value = module(list[i])
        j = i - 1
        while ((j >= 0) and (module(list[j]) > value)):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = list[j]


insertion(real_numbers)
print("���������� �������� ��� �������������� �����", "\n")


# print(real_numbers)

# ������ ���������� ��� ������ ����
def Gnome_sort(list):
    index = 1
    i = 0
    n = len(list)
    while i < n - 1:
        # ���� ��������� ������� ������ �� ���� ������
        if len(list[i]) <= len(list[i + 1]):
            i = index
            index = index + 1
        # ���� ��������� ������ �� ������ ������� � ���������� �����
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i = index
                index = index + 1


Gnome_sort(words)
print("������ ����������")
print("��������������� ������ ����", words)


# ���������� ��������� ��� ������ ����� �����


def counting_sort(list):
    list_count = [0] * len(list)
    for i in list:
        list_count[i] += 1
    list.clear()
    for i in range(len(list_count)):
        for a in range(list_count[i]):
            list.append(i)


counting_sort(integers)
print("���������� ��������� ��� ������ ����� �����", "\n")
print(integers)


# print(integers)


# ��������� ���������� ��� ����������� �����

def Bucket_sort(list):
    buckets = []
    # �������� ������ ������ ������� �� ������� � ���������� � ����������� ������
    for i in range(len(list)):
        buckets.append([])
    # ������ ���������� �� ������������ ������ ������� � ���� �������
    for i in list:
        buckets[int((module(i)) // (max_module / 42000))].append(i)
    # ������ ������� ����������� ��������
    for i in buckets:
        complex_insertion(i)
    # ������� ������ � �������� ��� ���������� �� ������
    list.clear()
    for i in buckets:
        for number in i:
            list.append(number)


Bucket_sort(complex_points)
print("��������� ���������� ��� ����������� �����", "\n")
print(complex_points)