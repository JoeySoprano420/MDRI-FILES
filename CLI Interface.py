import argparse

def main():
    parser = argparse.ArgumentParser(description='MDRI Processing Engine')
    parser.add_argument('file', help='Path to the MDRI file')
    args = parser.parse_args()

    process_mdri(args.file)

if __name__ == "__main__":
    main()
