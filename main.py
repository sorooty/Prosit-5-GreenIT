# Code principal : algorithmes + analyse des datasets

import pandas as pd
import glob
import time
import tracemalloc
import csv
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# ================================
# 1. Chargement des datasets CSV
# ================================
def load_datasets(path="Dataset/*.csv"):
    datasets = {}
    for file in glob.glob(path):
        df = pd.read_csv(file)
        # filtrer valeurs invalides
        df = df[pd.to_numeric(df['Value'], errors='coerce').notna()]
        datasets[file] = df['Value'].astype(int).tolist()
    return datasets

# ================================
# 2. Algorithmes avec comptage ops
# ================================
def brute_force(arr, target):  # 1 Algo Brute Force
    ops = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ops += 1
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j], ops)
    return (None, None, ops)

def hash_map(arr, target):  # 2 Algo Hashmap
    ops = 0
    seen = {}
    for i, val in enumerate(arr):
        ops += 1
        complement = target - val
        if complement in seen:
            return (complement, val, ops)
        seen[val] = i
    return (None, None, ops)

# def two_pointers(arr, target):  # 3 Algo deux Pointeurs (optionnel)
#     ops = 0
#     arr.sort()
#     left, right = 0, len(arr) - 1
#     while left < right:
#         ops += 1
#         s = arr[left] + arr[right]
#         if s == target:
#             return (arr[left], arr[right], ops)
#         elif s < target:
#             left += 1
#         else:
#             right -= 1
#     return (None, None, ops)

# ================================
# 3. Benchmark d'un algo
# ================================
def benchmark_algorithm(values, target, algo_func, timeout=5):
    """
    Benchmark an algorithm with a timeout.
    """
    tracemalloc.start()
    start_time = time.perf_counter()

    # Run the algorithm with a timeout
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(algo_func, values.copy(), target)
        try:
            a, b, ops = future.result(timeout=timeout)
        except TimeoutError:
            tracemalloc.stop()
            return {
                "result": None,
                "time_sec": None,
                "memory_kb": None,
                "operations": None,
                "timeout": True
            }

    elapsed = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory() # current c'est dynamiquement la mémoire au moment t (sur le moment)
    # On l'insère à titre fonctionnelle, mais ce qui nous interesse ici c'ets plutot peak (valeur la plus haute)
    tracemalloc.stop()
    return {
        "result": (a, b),
        "time_sec": elapsed,
        "memory_kb": peak / 1024,
        "operations": ops,
        "timeout": False
    }

# ================================
# 4. Point d'entrée
# ================================
if __name__ == "__main__":
    target = 150
    datasets = load_datasets("Dataset/*.csv")
    results = []

    for name, values in datasets.items():
        print(f"[INFO] Dataset: {name} | Taille: {len(values)}")
        for algo in [brute_force, hash_map]:
            # Skip brute_force for large datasets
            if algo == brute_force and len(values) > 10000:
                print(f"  → Algo: {algo.__name__} skipped for large dataset.")
                continue

            print(f"  → Algo: {algo.__name__} ...", end=" ")
            bench = benchmark_algorithm(values, target, algo, timeout=5)
            if bench["timeout"]:
                print("Timeout exceeded!")
                continue
            print(f"Temps: {bench['time_sec']:.4f}s | Mémoire: {bench['memory_kb']:.0f}KB | Ops: {bench['operations']}")
            results.append({
                "dataset": name,
                "algorithm": algo.__name__,
                "size": len(values),
                "time_sec": bench["time_sec"],
                "memory_kb": bench["memory_kb"],
                "operations": bench["operations"],
                "result": bench["result"]
            })

    # Export CSV pour notebook
    if results:  # seulement si results n'est pas vide
        keys = results[0].keys()
        with open("results.csv", "w", newline="") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(results)
        print("[INFO] Benchmark terminé. Résultats exportés dans results.csv")
    else:
        print("[WARN] Aucun résultat à exporter. Vérifier les datasets et le code.")



# DataLoad = utils.load_datasets
# print(DataLoad("Dataset/"))