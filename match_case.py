def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

#######################################################

def day_is_weekend(day):
    match day:
        case 6 | 7:
            return True
        case 1 | 2 | 3 | 4 | 5:
            return False
        case _:
            return False

print(day_of_week(6), day_is_weekend(6))