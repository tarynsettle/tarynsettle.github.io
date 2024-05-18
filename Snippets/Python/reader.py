def process_file(input_file):
    newlist = ""
    with open(input_file, 'r') as file:
        for line in file:
            index = line.find("- ")
            if index == -1:
                newlist += line
            else:
                newlist += line[index+2:]
    return newlist

def export_to_txt(output_file, content):
    with open(output_file, 'w') as file:
        file.write(content)

def main(input_file, output_file):
    newlist = process_file(input_file)
    export_to_txt(output_file, newlist)
    print("Output file created successfully.")

if __name__ == "__main__":
    input_file = "input.txt"  # Change this to your input file name
    output_file = "output.txt"  # Change this to your desired output file name
    main(input_file, output_file)