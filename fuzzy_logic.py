def classify_temperature(temp):
    """Класифікація температури на основі нечіткої логіки."""
    if temp < 18:
        return "Холодно"
    elif 18 <= temp <= 24:
        return "Комфортно"
    else:
        return "Жарко"


def classify_humidity(humidity):
    """Класифікація вологості на основі нечіткої логіки."""
    if humidity < 30:
        return "Суха"
    elif 30 <= humidity <= 60:
        return "Нормальна"
    else:
        return "Волога"


def get_recommendation(temp, humidity):
    """Рекомендації на основі температури та вологості."""
    temp_state = classify_temperature(temp)
    humidity_state = classify_humidity(humidity)

    if temp_state == "Холодно":
        action = "Увімкніть обігрівач."
    elif temp_state == "Жарко":
        action = "Увімкніть кондиціонер."
    else:
        action = "Температура комфортна."

    if humidity_state == "Суха":
        action += " Увімкніть зволожувач."
    elif humidity_state == "Волога":
        action += " Увімкніть осушувач."
    else:
        action += " Вологість комфортна."

    return action
