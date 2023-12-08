def display_help():
    print("Usage: python main.py -n [number_of_samples] --sensor [sensor_names_comma_separated]")
    print("")
    print("Options:")
    print("  -n, --samples\t\tNumber of samples")
    print("      --sensor\t\tSensor names separated by commas")
    print("  -h, --help\t\tDisplay this help message")
    print("")
    print("Example:")
    print("  python main.py -n 10 --sensor AS7341,AS7262")
    print("")
    print("Available sensors:")
    print("  AS7341")
    print("  AS7262")
    print("  AS7265x")
