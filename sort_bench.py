import x68k
import time
import random
x68k.loadfnc('SORT.FNC')

MAX_DATA_NUM = 5000
BENCH_DATA_NUM = 5000

def get_input(prompt, lower_limit, upper_limit, default_value=None):
    if default_value is not None:
        prompt = f"{prompt} [{default_value}]: "
    while True:
        input_str = input(prompt)
        if input_str.strip() == "":
            if default_value is not None:
                return default_value
            else:
                print("�l�����͂���Ă��܂���B")
                continue
        if not input_str.isdigit():
            print("��������͂��Ă��������B")
            continue
        input_num = int(input_str)
        if input_num < lower_limit or input_num > upper_limit:
            print("�͈͊O�̐����ł��B������x���͂��Ă��������B")
            continue
        break
    return input_num

def measure(fn, name, sort_data_org):
    sort_data = x68k.xarray_int(BENCH_DATA_NUM, sort_data_org)
    time1 = time.ticks_ms()
    print(name + "���s��...")
    fn(sort_data, len(sort_data), 0)
    time2 = time.ticks_ms()
    print(name + "���s���� : {}�b".format((time2 - time1) / 1000))


mode = get_input("���s���[�h(0:�\�[�g�P�Ǝ��s 1:�x���`�}�[�N )", 0, 1, 0)
if mode == 0:
    sort_kind = get_input("�\�[�g�̎��(0:�N�C�b�N�\�[�g 1:�R���\�[�g 2:�o�u���\�[�g)", 0, 2, 0)
    data_num = get_input("�\�[�g�Ώۂ̗v�f��(2�`" + str(MAX_DATA_NUM) + ")", 2, MAX_DATA_NUM, 100)
    rnd_max = get_input("�����̏���l(1�`" + str(MAX_DATA_NUM) + ")", 1, MAX_DATA_NUM, 100)
    order = get_input('�\�[�g�̕���(0:���� 1:�~��)', 0, 1, 0)
    needs_show_data = get_input('�\�[�g�O��̗v�f�̕\��(0:�\������ 1:�\�����Ȃ�)', 0, 1, 0)
    print("")
    random.seed(int(time.time()))
    sort_data = x68k.xarray_int(data_num, [random.randint(0, rnd_max) for i in range(data_num)])

    if needs_show_data == 0:
        print("�\�[�g�O:" + str(sort_data.list()))
    time1 = time.ticks_ms()
    print("�\�[�g���s��...")
    if sort_kind == 0:
        quick_sort(sort_data, len(sort_data), order)
    elif sort_kind == 1:
        comb_sort(sort_data, len(sort_data), order)
    elif sort_kind == 2:
        bubble_sort(sort_data, len(sort_data), order)
    time2 = time.ticks_ms()
    if needs_show_data == 0:
        print("�\�[�g��:" + str(sort_data.list()))

    print("�\�[�g���s���� : {}�b".format((time2 - time1) / 1000))
elif mode == 1:
    print("")
    random.seed(int(time.time()))
    sort_data_org = x68k.xarray_int(BENCH_DATA_NUM, [random.randint(0, BENCH_DATA_NUM) for i in range(BENCH_DATA_NUM)])
    print("�\�[�g�Ώۂ̗v�f��: " + str(len(sort_data_org)))
    measure(bubble_sort, "�o�u���\�[�g", sort_data_org)
    measure(comb_sort, "�R���\�[�g", sort_data_org)
    measure(quick_sort, "�N�C�b�N�\�[�g", sort_data_org)
