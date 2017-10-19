from day_16.data_generator import calculate_checksum, create_disk_data


def main():
    data = create_disk_data("00101000101111010", 272)
    checksum = calculate_checksum(data)
    print "Calculated checksum is %s" % checksum


if __name__ == '__main__':
    main()
