import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time for {func.__name__}: {execution_time:.6f} milliseconds")
        return result

    return wrapper


@calculate_time
def task_01():
    from datetime import datetime

    def time_logger(func):
        def wrapper(*args, **kwargs):
            # Displaying the current time before calling the function
            current_time = datetime.now()
            print(f"Current Time Before Calling {func.__name__}: {current_time.strftime('%H:%M:%S')}")

            # Calling the decorated function
            result = func(*args, **kwargs)

            # Displaying the current time after calling the function
            current_time = datetime.now()
            print(f"Current Time After Calling {func.__name__}: {current_time.strftime('%H:%M:%S')}")

            return result

        return wrapper

    # Example usage:
    @time_logger
    def my_function():
        print("Executing my_function")

    my_function()


task_01()
