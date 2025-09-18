from datetime import datetime


def calculate_candles(birthday):
    """
    Calculate how many candles are needed for a birthday cake.

    Args:
        birthday: A date string in format 'YYYY-MM-DD' or a datetime object

    Returns:
        int: The number of candles needed (equal to the person's age)
    """
    # Convert string to datetime if needed

    try:
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Birthday should be in format 'YYYY-MM-DD'")

    # Get current date
    today = datetime.now()

    # Calculate age
    age = today.year - birthday.year

    # Adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def calculate_total_candles(people_birthdays):
    """
    Calculate the total number of candles needed for multiple birthdays.

    Args:
        people_birthdays: A list of tuples, each containing (name, birthday)
                         where birthday is in format 'YYYY-MM-DD' or a datetime object

    Returns:
        dict: A dictionary with 'total' for the sum of candles and 'details' showing
              each person's name and their individual candle count
    """
    total_candles = 0
    details = []

    for name, birthday in people_birthdays:
        candles = calculate_candles(birthday)
        total_candles += candles
        details.append({
            'name': name,
            'birthday': birthday if isinstance(birthday, str) else birthday.strftime('%Y-%m-%d'),
            'candles': candles
        })

    return {
        'total': total_candles,
        'details': details
    }


# Example usage
if __name__ == "__main__":
    # Calculate One Birthday
    print(f"We need {calculate_candles('1981-01-14')} Candles")


    # List of (name, birthday) tuples
    # people = [
    #     ("Ron", "1981-01-14"),
    #     ("Jake", "2009-09-24"),
    #     ("Charlie", "2010-03-08")
    # ]
    #
    # result = calculate_total_candles(people)
    #
    #
    # print("\nDetails:")
    # for person in result['details']:
    #     print(f"  {person['name']} ({person['birthday']}): {person['candles']} candles")
    # print(f"Total candles needed: {result['total']}")