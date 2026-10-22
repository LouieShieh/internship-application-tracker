import csv
from pathlib import Path


def load_applications(file_path):
    with file_path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def main():
    data_file = Path(__file__).resolve().parent / "data" / "example.csv"
    applications = load_applications(data_file)

    if not applications:
        print("No applications found.")
        return
      
    for number, application in enumerate(applications, start=1):
        print(
            f"{number}. {application['company']} | "
            f"{application['role']} | {application['status']}"
        )

    print(f"\nLoaded {len(applications)} application records")


if __name__ == "__main__":
    main()
