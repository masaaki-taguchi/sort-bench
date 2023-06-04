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
                print("値が入力されていません。")
                continue
        if not input_str.isdigit():
            print("数字を入力してください。")
            continue
        input_num = int(input_str)
        if input_num < lower_limit or input_num > upper_limit:
            print("範囲外の数字です。もう一度入力してください。")
            continue
        break
    return input_num

def measure(fn, name, sort_data_org):
    sort_data = x68k.xarray_int(BENCH_DATA_NUM, sort_data_org)
    time1 = time.ticks_ms()
    print(name + "実行中...")
    fn(sort_data, len(sort_data), 0)
    time2 = time.ticks_ms()
    print(name + "実行時間 : {}秒".format((time2 - time1) / 1000))


mode = get_input("実行モード(0:ソート単独実行 1:ベンチマーク )", 0, 1, 0)
if mode == 0:
    sort_kind = get_input("ソートの種類(0:クイックソート 1:コムソート 2:バブルソート)", 0, 2, 0)
    data_num = get_input("ソート対象の要素数(2～" + str(MAX_DATA_NUM) + ")", 2, MAX_DATA_NUM, 100)
    rnd_max = get_input("乱数の上限値(1～" + str(MAX_DATA_NUM) + ")", 1, MAX_DATA_NUM, 100)
    order = get_input('ソートの方向(0:昇順 1:降順)', 0, 1, 0)
    needs_show_data = get_input('ソート前後の要素の表示(0:表示する 1:表示しない)', 0, 1, 0)
    print("")
    random.seed(int(time.time()))
    sort_data = x68k.xarray_int(data_num, [random.randint(0, rnd_max) for i in range(data_num)])

    if needs_show_data == 0:
        print("ソート前:" + str(sort_data.list()))
    time1 = time.ticks_ms()
    print("ソート実行中...")
    if sort_kind == 0:
        quick_sort(sort_data, len(sort_data), order)
    elif sort_kind == 1:
        comb_sort(sort_data, len(sort_data), order)
    elif sort_kind == 2:
        bubble_sort(sort_data, len(sort_data), order)
    time2 = time.ticks_ms()
    if needs_show_data == 0:
        print("ソート後:" + str(sort_data.list()))

    print("ソート実行時間 : {}秒".format((time2 - time1) / 1000))
elif mode == 1:
    print("")
    random.seed(int(time.time()))
    sort_data_org = x68k.xarray_int(BENCH_DATA_NUM, [random.randint(0, BENCH_DATA_NUM) for i in range(BENCH_DATA_NUM)])
    print("ソート対象の要素数: " + str(len(sort_data_org)))
    measure(bubble_sort, "バブルソート", sort_data_org)
    measure(comb_sort, "コムソート", sort_data_org)
    measure(quick_sort, "クイックソート", sort_data_org)
