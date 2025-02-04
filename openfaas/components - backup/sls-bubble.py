def bubbleSort(arr):
    n = len(arr) 
    # Traverse through all array elements
    for i in range(n): 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def handle(event, context):
    if event.method == 'POST':
        x = [int(i) for i in str(event.body,'utf-8').split(",")]
        return {
            "statusCode": 200,
            "body": bubbleSort(x)
        }