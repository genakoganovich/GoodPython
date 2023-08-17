def get_data(value):
    match value:
        # здесь продолжайте программу
        case int() as command if command > 0:
            return command
        case float() as command if -100 <= command <= 100:
            return command
        case str() as command:
            return command

    return None
