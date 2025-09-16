from datetime import datetime


def calculate_time_difference(start_time, end_time=None):
    """
    Calculate the time difference between two timestamps and return it in days, hours, and minutes.

    Args:
        start_time (str): Start time in format 'YYYY-MM-DD HH:MM' (24-hour format)
        end_time (str, optional): End time in same format. If None, uses current time.

    Returns:
        tuple: (days, hours, minutes) or None if invalid input
    """
    try:
        # Convert string to datetime object
        start_dt = datetime.strptime(start_time, '%Y-%m-%d %H:%M')

        # If end_time is not provided, use current time
        end_dt = datetime.now() if end_time is None else datetime.strptime(end_time, '%Y-%m-%d %H:%M')

        # Ensure start_time is before end_time
        if start_dt > end_dt:
            raise ValueError("Start time must be before end time")

        # Calculate time difference
        time_diff = end_dt - start_dt

        # Extract days, hours, and minutes
        days = time_diff.days
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds % 3600) // 60

        return days, hours, minutes

    except ValueError as e:
        print(f"Error: {e}")
        return None


def format_time_difference(days, hours, minutes):
    """Format the time difference for readable output."""
    return f"{days} days, {hours} hours, {minutes} minutes"


# Example usage
def main():
    # Example 1: Using a specific start time and current time
    start_time = "2025-09-01 14:30"
    result = calculate_time_difference(start_time)
    if result:
        days, hours, minutes = result
        print(f"Time since {start_time}: {format_time_difference(days, hours, minutes)}")

    # Example 2: Using specific start and end times
    start_time = "2025-09-01 14:30"
    end_time = "2025-09-07 22:00"
    result = calculate_time_difference(start_time, end_time)
    if result:
        days, hours, minutes = result
        print(f"Time between {start_time} and {end_time}: {format_time_difference(days, hours, minutes)}")

    # Example 3: Invalid input
    start_time = "2025-09-07 22:00"
    end_time = "2025-09-01 14:30"  # End time before start time
    result = calculate_time_difference(start_time, end_time)
    if result:
        days, hours, minutes = result
        print(f"Time between {start_time} and {end_time}: {format_time_difference(days, hours, minutes)}")


if __name__ == "__main__":
    main()

    # Interactive input
    print("\nEnter your own times (format: YYYY-MM-DD HH:MM)")
    start_input = input("Enter start time: ")
    end_input = input("Enter end time (press Enter for current time): ")

    if end_input.strip() == "":
        result = calculate_time_difference(start_input)
    else:
        result = calculate_time_difference(start_input, end_input)

    if result:
        days, hours, minutes = result
        print(f"Time difference: {format_time_difference(days, hours, minutes)}")