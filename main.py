from args import get_args
from management import management_loop
from check import check_loop
from domein import read_domeinen


def main():
    management, check = get_args()
    domeinen = read_domeinen()
    if management:
        management_loop(domeinen)
    elif check:
        check_loop(domeinen)


if __name__ == "__main__":
    main()
