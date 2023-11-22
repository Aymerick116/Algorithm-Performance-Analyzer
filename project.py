
import timeit
import random
import pandas as pd
from math import log
import matplotlib.pyplot as plt



#First Algorithm with insertion-sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key







# Second Algorithm with merge-sort
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Create temporary arrays
    left_half = [arr[p + i] for i in range(n1)]
    right_half = [arr[q + 1 + j] for j in range(n2)]

    # Merge the temporary arrays back into arr[p..r]
    i = j = 0
    k = p

    for _ in range(n1 + n2):
        if i < n1 and (j >= n2 or left_half[i] <= right_half[j]):
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)





# Third algorithm with randomized-select
def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]

    q = randomized_partition(arr, p, r)
    k = q - p + 1

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)


def ALG1(arr, n, i):
    insertion_sort(arr)
    print(arr[i - 1])

def ALG2(arr, n, i):
    merge_sort(arr, 0, n - 1)
    print(arr[i - 1])  # Printing the ith order statistic (1-based index)
def ALG3(arr, n, i):
    result = randomized_select(arr, 0, n - 1, i)
    print(result)




def compute_average_rt(algorithm, A, n, m):
    i = int(2 * n / 3)

    # List to store empirical runtimes
    empirical_rts = []

    for _ in range(m):
        # Empirical Runtime
        start_time = timeit.default_timer()
        algorithm(A, n, i)
        end_time = timeit.default_timer()
        empirical_rt = (end_time - start_time) *1000
        empirical_rts.append(empirical_rt)

    # Average Empirical Runtime
    average_empirical_rt = sum(empirical_rts) / m

    return average_empirical_rt

def compute_theoretical_rt(n, algorithm):
    if algorithm == ALG1:
        theoretical_rt = n ** 2  # Example: n squared for ALG1
    elif algorithm == ALG2:
        theoretical_rt = n * log(n, 2)  # Example: n log n for ALG2
    elif algorithm == ALG3:
        theoretical_rt = n  # Example: linear time for ALG3
    else:
        theoretical_rt = 0  # Handle other cases if needed
    return theoretical_rt

def compute_predicted_rt(n, theoretical_rt, c1):
    return c1 * theoretical_rt


def plot_empirical_runtimes(result_df_ALG1, result_df_ALG2, result_df_ALG3):
    plt.figure(figsize=(10, 6))

    plt.plot(result_df_ALG1['n'], result_df_ALG1['AvgEmpiricalRT'], label='ALG1: Empirical RT', marker='o')
    plt.plot(result_df_ALG2['n'], result_df_ALG2['AvgEmpiricalRT'], label='ALG2: Empirical RT', marker='o')
    plt.plot(result_df_ALG3['n'], result_df_ALG3['AvgEmpiricalRT'], label='ALG3: Empirical RT', marker='o')

    plt.xlabel('Input Size (n)')
    plt.ylabel('Empirical Runtime (ms)')
    plt.title('Empirical Runtimes of ALG1, ALG2, and ALG3')
    plt.legend()
    plt.grid(True)

    plt.show()

def plot_empirical_vs_predicted(result_df_ALG, algorithm_name):
    plt.figure(figsize=(10, 6))

    plt.plot(result_df_ALG['n'], result_df_ALG['AvgEmpiricalRT'], label=f'{algorithm_name}: Empirical RT', marker='o')
    plt.plot(result_df_ALG['n'], result_df_ALG['PredictedRT'], label=f'{algorithm_name}: Predicted RT', marker='o')

    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (ms)')
    plt.title(f'Empirical vs Predicted Runtimes for {algorithm_name}')
    plt.legend()
    plt.grid(True)

    plt.show()







def main():
    max_value = 10000
    m = 5
    c1_ALG1 = 0
    c1_ALG2 = 0
    c1_ALG3 = 0

    # Result dictionaries for ALG1, ALG2, and ALG3
    result_data_ALG1 = {'n': [], 'TheoreticalRT': [], 'AvgEmpiricalRT': [], 'Ratio': [], 'PredictedRT': []}
    result_data_ALG2 = {'n': [], 'TheoreticalRT': [], 'AvgEmpiricalRT': [], 'Ratio': [], 'PredictedRT': []}
    result_data_ALG3 = {'n': [], 'TheoreticalRT': [], 'AvgEmpiricalRT': [], 'Ratio': [], 'PredictedRT': []}

    for n in range(1000, max_value + 1, 1000):
        A = [random.randint(1, max_value) for _ in range(n)]



        # Compute the average empirical runtime for ALG1
        avg_rt_ALG1 = compute_average_rt(ALG1, A[:], n, m)

        # Compute the theoretical runtime for ALG1
        theoretical_rt_ALG1 = compute_theoretical_rt(n, ALG1)

        # Update c1_ALG1 if the current ratio is greater than the existing c1_ALG1
        current_ratio_ALG1 = avg_rt_ALG1 / theoretical_rt_ALG1
        if current_ratio_ALG1 > c1_ALG1:
            c1_ALG1 = current_ratio_ALG1


        # Append the data to the result dictionary for ALG1
        result_data_ALG1['n'].append(n)
        result_data_ALG1['TheoreticalRT'].append(theoretical_rt_ALG1)
        result_data_ALG1['AvgEmpiricalRT'].append(avg_rt_ALG1)
        result_data_ALG1['Ratio'].append(avg_rt_ALG1 / theoretical_rt_ALG1) #avg_rt_ALG1 / theoretical_rt_ALG1
        result_data_ALG1['PredictedRT'].append(compute_predicted_rt(n, theoretical_rt_ALG1, c1_ALG1))

        # Compute the average empirical runtime for ALG2
        avg_rt_ALG2 = compute_average_rt(ALG2, A[:], n, m)

        # Compute the theoretical runtime for ALG2
        theoretical_rt_ALG2 = compute_theoretical_rt(n, ALG2)


        current_ratio_ALG2 = avg_rt_ALG2 / theoretical_rt_ALG2
        if current_ratio_ALG2 > c1_ALG2:
            c1_ALG2 = current_ratio_ALG2


        # Append the data to the result dictionary for ALG2
        result_data_ALG2['n'].append(n)
        result_data_ALG2['TheoreticalRT'].append(theoretical_rt_ALG2)
        result_data_ALG2['AvgEmpiricalRT'].append(avg_rt_ALG2)
        result_data_ALG2['Ratio'].append(avg_rt_ALG2 / theoretical_rt_ALG2)
        result_data_ALG2['PredictedRT'].append(compute_predicted_rt(n, theoretical_rt_ALG2, c1_ALG2))

        # Compute the average empirical runtime for ALG3
        avg_rt_ALG3 = compute_average_rt(ALG3, A[:], n, m)

        # Compute the theoretical runtime for ALG3
        theoretical_rt_ALG3 = compute_theoretical_rt(n, ALG3)


        current_ratio_ALG3 = avg_rt_ALG3 / theoretical_rt_ALG3
        if current_ratio_ALG3 > c1_ALG3:
            c1_ALG3 = current_ratio_ALG3

        # Append the data to the result dictionary for ALG3
        result_data_ALG3['n'].append(n)
        result_data_ALG3['TheoreticalRT'].append(theoretical_rt_ALG3)
        result_data_ALG3['AvgEmpiricalRT'].append(avg_rt_ALG3)
        result_data_ALG3['Ratio'].append(avg_rt_ALG3 / theoretical_rt_ALG3)
        result_data_ALG3['PredictedRT'].append(compute_predicted_rt(n, theoretical_rt_ALG3, c1_ALG3))

    # Create DataFrames from the result dictionaries for ALG1, ALG2, and ALG3
    result_df_ALG1 = pd.DataFrame(result_data_ALG1)
    result_df_ALG2 = pd.DataFrame(result_data_ALG2)
    result_df_ALG3 = pd.DataFrame(result_data_ALG3)

    # Print the final DataFrames for ALG1, ALG2, and ALG3
    print("Table for ALG1:")
    print(result_df_ALG1)

    print("\nTable for ALG2:")
    print(result_df_ALG2)

    print("\nTable for ALG3:")
    print(result_df_ALG3)

    # Create DataFrames from the result dictionaries for ALG1, ALG2, and ALG3
    result_df_ALG1 = pd.DataFrame(result_data_ALG1)
    result_df_ALG2 = pd.DataFrame(result_data_ALG2)
    result_df_ALG3 = pd.DataFrame(result_data_ALG3)

    # Plot the empirical runtimes
    plot_empirical_runtimes(result_df_ALG1, result_df_ALG2, result_df_ALG3)

    # Create a DataFrame from the result dictionary for ALG1


    # Plot the empirical vs predicted runtimes for ALG1
    plot_empirical_vs_predicted(result_df_ALG1, 'ALG1')
    plot_empirical_vs_predicted(result_df_ALG2, 'ALG2')
    plot_empirical_vs_predicted(result_df_ALG3, 'ALG3')



if __name__ == "__main__":
    main()
























