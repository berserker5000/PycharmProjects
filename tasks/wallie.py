#coding:windows-1251
import random


def get_wallie_action():
    possible_actions = [
        '������� ����� �������������',
        '������� ����� ������',
        '���-�� ���������',
        '����������� ����� ������',
        '��������� ���-�� ������',
        '����������� ������ � ������������',
        '���������� ������',
        '���� ���������� ��� ���������',
    ]
    return '����� ' + random.choice(possible_actions)


if __name__ == '__main__':
    action = get_wallie_action()
    print (action)

