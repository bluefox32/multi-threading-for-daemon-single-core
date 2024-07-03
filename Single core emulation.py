import threading

# シングルコアとして動作させるタスク
def single_core_task(task_id):
    print(f"Running task {task_id} on single core")

# メイン関数
def main():
    num_tasks = 24  # 実行するタスクの数
    core_to_use = 0  # 使用するコア番号（例として0番目のコア）

    # 各タスクをシングルコアで実行
    for i in range(num_tasks):
        # CPUアフィニティを設定して特定のコアに割り当てる
        threading.Thread(target=single_core_task, args=(i,), daemon=True).start()

    print("All tasks started")

if __name__ == "__main__":
    main()