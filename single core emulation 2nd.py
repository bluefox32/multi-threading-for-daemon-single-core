import multiprocessing
import time

def process_task(task, core_id):
    """
    各タスクをコアに割り当てて処理する関数。
    """
    print(f"Core {core_id} processing task: {task}")
    time.sleep(task)  # シミュレーションのための待機時間
    print(f"Core {core_id} completed task: {task}")

def main():
    # タスクのリスト
    tasks = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # コアの数
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores available: {num_cores}")
    
    # プールを使ってタスクを並列処理
    with multiprocessing.Pool(processes=num_cores) as pool:
        for i, task in enumerate(tasks):
            core_id = i % num_cores
            pool.apply_async(process_task, args=(task, core_id))
        
        pool.close()
        pool.join()

if __name__ == "__main__":
    main()