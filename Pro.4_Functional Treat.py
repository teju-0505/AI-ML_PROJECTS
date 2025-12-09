def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def data_summary(data):
    return {
        "Count": len(data),
        "Sum": sum(data),
        "Max": max(data) if data else None,
        "Min": min(data) if data else None
    }

def filter_by_threshold(data, threshold):
    return list(filter(lambda x: x > threshold, data))

def sort_data(data):
    return sorted(data)

def dataset_stats(data):
    return len(data), sum(data), max(data), min(data)


data = []

print("Welcome to the Data Analyzer and Transformer Program\n")

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == '1':
        values = input("Enter numbers separated by space: ")
        data = list(map(int, values.split()))
        print("Data stored successfully.")

    elif choice == '2':
        summary = data_summary(data)
        print("Data Summary:", summary)

    elif choice == '3':
        num = int(input("Enter a number: "))
        print("Factorial:", factorial(num))

    elif choice == '4':
        threshold = int(input("Enter threshold: "))
        result = filter_by_threshold(data, threshold)
        print("Filtered Data:", result)

    elif choice == '5':
        sorted_data = sort_data(data)
        print("Sorted Data:", sorted_data)

    elif choice == '6':
        count, total, max_v, min_v = dataset_stats(data)
        print("Dataset Statistics:", count, total, max_v, min_v)

    elif choice == '7':
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Please try again.")
