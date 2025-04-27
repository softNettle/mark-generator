#import os
import file_converter as fc
def main():

    print(fc.generate_marks(fc.csv_to_dict("./5.1_temat.csv"), 0, 10))

if __name__ == '__main__':
    main()