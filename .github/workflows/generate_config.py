import xml.etree.ElementTree as ET
import argparse


def update_input_file(xml_file: str, new_input_file: str):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find the <Param> element with name="InputFile"
    input_file_param = root.find(".//Param[@name='InputFile']")

    if input_file_param is not None:
        # Update the value of the InputFile parameter
        input_file_param.set("value", new_input_file)
        print(f"Updated InputFile to: {new_input_file}")
    else:
        print("InputFile parameter not found.")
        sys.exit(1)

    # Write the changes back to the XML file
    tree.write(xml_file)


def main():
    parser = argparse.ArgumentParser(description="Generate quality checker config XML file for qc_openmaterial3d based on a template.")
    parser.add_argument("xml_file", type=str, help="Path to the config XML file template")
    parser.add_argument("new_input_file", type=str, help="Path to the input file (.xoma, .xomm, .xomp or .xompt)")
    args = parser.parse_args()

    update_input_file(args.xml_file, args.new_input_file)


if __name__ == "__main__":
    main()
