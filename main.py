from fuzzy_logic import get_recommendation

def validate_input(value, min_value, max_value, param_name):
    """Перевіряє, чи введене значення в допустимих межах."""
    if value < min_value or value > max_value:
        raise ValueError(f"{param_name} має бути в межах від {min_value} до {max_value}.")
    return round(value, 1)  # Округлення до 1 знака після коми


def main():
    print("Система управління кліматом у приміщенні")
    try:
        temp = float(input("Введіть поточну температуру (°C): "))
        humidity = float(input("Введіть поточну вологість (%): "))

        # Перевірка меж
        temp = validate_input(temp, -50, 50, "Температура")
        humidity = validate_input(humidity, 0, 100, "Вологість")

        recommendation = get_recommendation(temp, humidity)
        print("\n\033[1;32mРекомендації:\033[0m")  # Зелений текст
        print(recommendation)

    except ValueError as e:
        print(f"\033[1;31mПомилка:\033[0m {e}")  # Червоний текст

if __name__ == "__main__":
    main()
