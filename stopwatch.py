import time


print("ストップウォッチを開始します。Enterを押すと開始されます。")
input()
start_time = time.time()
print("計測を開始しました。")

lap_times = []
split_times = []

while True:
    print("計測中... Enterを押すとラップタイムを計測できます。")
    print("sを押すとストップします。")
    print("pを押すとスプリットタイムを計測できます。")
    input_str = input()
    if input_str == "s":
        end_time = time.time()
        total_time = end_time - start_time
        print(f"計測終了。総時間: {total_time:.2f}秒")
        break
    elif input_str == "p":
        split_time = time.time() - start_time
        split_times.append(split_time)
        print(f"スプリットタイム: {split_time:.2f}秒")
    else:
        lap_time = time.time() - start_time
        lap_times.append(lap_time)
        print(f"ラップタイム: {lap_time:.2f}秒")

print("ラップタイム一覧:")
for i, lap_time in enumerate(lap_times):
    print(f"Lap {i+1}: {lap_time:.2f}秒")

print("スプリットタイム一覧:")
for i, split_time in enumerate(split_times):
    print(f"Split {i+1}: {split_time:.2f}秒")
