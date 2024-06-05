from gdrive.query import get_fishstorage_total


def main():
    df = get_fishstorage_total()
    for row in df.values:
        print(f"{row[0]}: {row[2]}кг X {row[1]}шт = {row[3]}кг")

if __name__ == "__main__":
    main()