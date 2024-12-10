# scripts/validate_metadata.py

from lxml import etree
import sys

def validate_metadata(xml_file, xsd_file):
    """
    Validates an XML file against an XSD schema.

    Args:
        xml_file (str): Path to the XML file.
        xsd_file (str): Path to the XSD file.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        # Parse the XSD schema
        with open(xsd_file, 'rb') as f:
            schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)

        # Parse the XML file
        with open(xml_file, 'rb') as f:
            xml_doc = etree.parse(f)

        # Validate
        schema.assertValid(xml_doc)
        print(f"Validation successful: '{xml_file}' is valid against '{xsd_file}'.")
        return True

    except etree.XMLSyntaxError as e:
        print(f"Validation error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred during validation: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_metadata.py <path_to_xml> <path_to_xsd>")
        sys.exit(1)

    xml_path = sys.argv[1]
    xsd_path = sys.argv[2]

    is_valid = validate_metadata(xml_path, xsd_path)
    sys.exit(0 if is_valid else 1)
