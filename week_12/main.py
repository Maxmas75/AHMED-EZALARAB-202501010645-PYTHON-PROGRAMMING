from lab_status import check_computers, count_available, display_status


def main():
    print("=== LAB STATUS ===")

    while True:
        computers = check_computers()
        available = count_available(computers)
        display_status(computers, available)

        again = input("Perform another monitoring cycle? (Y/N): ").strip().upper()
        if again != "Y":
            print("Monitoring stopped.")
            break


if __name__ == "__main__":
    main()
