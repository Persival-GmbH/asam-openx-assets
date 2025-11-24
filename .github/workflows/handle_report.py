import xml.etree.ElementTree as ET
from xml.dom import minidom
import argparse
import sys
import os


def parse_issues(file_path: str, output_file="junit_report.xml"):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract the InputFile from the CheckerBundle (assuming it's within the <CheckerBundle> tag)
    input_file = root.find(".//Param[@name='InputFile']").get('value')
    if not input_file:
        print("Error: InputFile not found in the provided XML.")
        sys.exit(1)

    # If the output file already exists, parse it; otherwise, create the root structure
    if os.path.exists(output_file):
        # Parse the existing JUnit report
        existing_tree = ET.parse(output_file)
        existing_root = existing_tree.getroot()
    else:
        # Initialize the JUnit report structure
        existing_root = ET.Element("testsuites")

    # Use the InputFile value as the name for the test suite
    input_file_name = os.path.basename(input_file)

    # Add a new testsuite to the existing root
    testsuite = ET.SubElement(existing_root, "testsuite", name=input_file_name)

    # Track the number of failures
    failures_count = 0

    # Iterate through all checkers in the XML
    for checker in root.findall(".//Checker"):
        checker_id = checker.get("checkerId")
        issues = checker.findall(".//Issue")

        for issue in issues:
            issue_id = issue.get("issueId")
            issue_description = issue.get("description")
            level = int(issue.get("level"))

            # Set test case status based on the issue level
            status = "failed" if level == 1 else "skipped"  # level=1 for error, level=2 for warning

            # Create a test case for each issue
            testcase = ET.SubElement(testsuite, "testcase",
                                     classname=checker_id,
                                     name=f"{input_file_name}_issue_{issue_id}",
                                     status=status)

            # Add failure or skipped information if needed
            if status == "failed":
                ET.SubElement(testcase, "failure", message="Error: " + issue_description)
                failures_count += 1
            elif status == "skipped":
                ET.SubElement(testcase, "skipped", message="Warning: " + issue_description)

    # Create a pretty-printed XML string
    xml_str = minidom.parseString(ET.tostring(existing_root)).toprettyxml(indent="  ")

    # Write to an output JUnit XML file
    with open(output_file, "w") as f:
        f.write(xml_str)

    print(f"JUnit report saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Convert QC results XML files to a single JUnit XML for GitLab/GitHub CI issue reporting.")
    parser.add_argument("file_path", type=str, help="Path to the XML file")
    args = parser.parse_args()
    parse_issues(args.file_path)


if __name__ == "__main__":
    main()
