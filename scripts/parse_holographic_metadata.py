import xml.etree.ElementTree as ET

def parse_holographic_metadata(xml_file):
    """
    Parses the holographic metadata XML file and extracts information.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        dict: Extracted metadata.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract metadata_core
    metadata_core = root.find('.//metadata_core')
    if metadata_core is None:
        raise ValueError("Missing 'metadata_core' section in XML.")
    core_info = {child.tag: (child.text.strip() if child.text else None) for child in metadata_core}

    # Extract cognitive_processes
    cognitive_processes = []
    for cp in root.findall('.//cognitive_process'):
        process = {
            'name': cp.find('name').text.strip() if cp.find('name') is not None else None,
            'description': cp.find('description').text.strip() if cp.find('description') is not None else None,
            'parameters': {}
        }
        parameters = cp.find('parameters')
        if parameters:
            for param in parameters.findall('parameter'):
                param_name = param.attrib.get('name')
                param_type = param.attrib.get('type')
                if param_type == 'list':
                    # Extract list items based on tag (e.g., <source>, <method>, etc.)
                    items = [item.text.strip() for item in param]
                    process['parameters'][param_name] = items
                else:
                    # Handle 'string', 'integer', 'float' types
                    # Attempt to find child elements like <item>
                    item = param.find('item')
                    if item is not None and item.text and item.text.strip():
                        value = item.text.strip()
                    else:
                        # Fallback to param.text if no <item> found
                        value = param.text.strip() if param.text and param.text.strip() else None

                    if param_type == 'string':
                        process['parameters'][param_name] = value
                    elif param_type == 'integer':
                        try:
                            process['parameters'][param_name] = int(value) if value else None
                        except ValueError:
                            process['parameters'][param_name] = None
                    elif param_type == 'float':
                        try:
                            process['parameters'][param_name] = float(value) if value else None
                        except ValueError:
                            process['parameters'][param_name] = None
                    else:
                        # Handle other types if necessary
                        process['parameters'][param_name] = value
        cognitive_processes.append(process)

    # Extract ethical_guidelines
    ethical_guidelines = []
    for eg in root.findall('.//ethical_guideline'):
        guideline = {
            'name': eg.find('name').text.strip() if eg.find('name') is not None else None,
            'description': eg.find('description').text.strip() if eg.find('description') is not None else None,
            'implementation': [method.text.strip() for method in eg.find('implementation').findall('method') if method.text]
        }
        ethical_guidelines.append(guideline)

    # Extract metadata_hologram
    hologram = root.find('.//metadata_hologram')
    if hologram is None:
        raise ValueError("Missing 'metadata_hologram' section in XML.")
    hologram_description = hologram.find('description').text.strip() if hologram.find('description') is not None else None

    # Key Parameters
    key_parameters = {}
    for kp in hologram.find('key_parameters').findall('parameter'):
        kp_name = kp.attrib.get('name')
        kp_type = kp.attrib.get('type')
        # For key_parameters, the value might be in text or CDATA
        kp_value = kp.text.strip() if kp.text and kp.text.strip() else None
        key_parameters[kp_name] = kp_value

    # Equations
    equations = []
    for eq in hologram.find('equations').findall('equation'):
        equation = {
            'id': eq.attrib.get('id'),
            'title': eq.find('title').text.strip() if eq.find('title') is not None else None,
            'expression': eq.find('expression').text.strip() if eq.find('expression') is not None else None,
            'description': eq.find('description').text.strip() if eq.find('description') is not None else None,
            'applications': [app.text.strip() for app in eq.find('applications').findall('application') if app.text]
        }
        equations.append(equation)

    # Parameters Description
    parameters_description = {}
    for pd in hologram.find('parameters_description').findall('parameter'):
        name = pd.find('name').text.strip() if pd.find('name') is not None else None
        purpose = pd.find('purpose').text.strip() if pd.find('purpose') is not None else None
        parameters_description[name] = purpose

    # Extract answer_operator
    answer_operator = root.find('.//answer_operator')
    if answer_operator is None:
        raise ValueError("Missing 'answer_operator' section in XML.")
    ao_description = answer_operator.find('description').text.strip() if answer_operator.find('description') is not None else None

    # Response Structuring Strategies
    response_structuring_elem = answer_operator.find('response_structuring')
    response_structuring = [strategy.text.strip() for strategy in response_structuring_elem.findall('strategy') if strategy.text] if response_structuring_elem is not None else []

    # Quality Metrics
    quality_metrics = {}
    quality_metrics_elem = answer_operator.find('quality_metrics')
    if quality_metrics_elem is not None:
        for qm in quality_metrics_elem.findall('metric'):
            metric_name = qm.attrib.get('name')
            metric_value_str = qm.text.strip() if qm.text and qm.text.strip() else None
            if metric_value_str:
                try:
                    metric_value = float(metric_value_str)
                except ValueError:
                    metric_value = None
            else:
                metric_value = None
            quality_metrics[metric_name] = metric_value

    # Optimization Parameters
    optimization_parameters = {}
    optimization_parameters_elem = answer_operator.find('optimization_parameters')
    if optimization_parameters_elem is not None:
        for op in optimization_parameters_elem.findall('parameter'):
            param_name = op.attrib.get('name')
            param_type = op.attrib.get('type')
            # Assuming single <item> for non-list types
            item = op.find('item')
            if item is not None and item.text and item.text.strip():
                value_str = item.text.strip()
            else:
                value_str = op.text.strip() if op.text and op.text.strip() else None

            if param_type == 'integer':
                try:
                    value = int(value_str) if value_str else None
                except ValueError:
                    value = None
            elif param_type == 'float':
                try:
                    value = float(value_str) if value_str else None
                except ValueError:
                    value = None
            else:
                # For other types, assign the string value
                value = value_str

            optimization_parameters[param_name] = value

    # Post Processing Steps
    post_processing_elem = answer_operator.find('post_processing')
    post_processing = [step.text.strip() for step in post_processing_elem.findall('step') if step.text] if post_processing_elem is not None else []

    # Feedback Loop Components
    feedback_loop = {}
    feedback_loop_elem = answer_operator.find('feedback_loop')
    if feedback_loop_elem is not None:
        feedback_description = feedback_loop_elem.find('description').text.strip() if feedback_loop_elem.find('description') is not None else None
        feedback_components = [comp.text.strip() for comp in feedback_loop_elem.find('components').findall('component') if comp.text] if feedback_loop_elem.find('components') is not None else []
        feedback_loop = {
            'description': feedback_description,
            'components': feedback_components
        }

    # Extract think section
    # Adjusted to handle 'think' as a simple string
    # Assuming 'think' content is under 'claude_thoughts'
    claude_thoughts = answer_operator.find('claude_thoughts')
    if claude_thoughts is None:
        raise ValueError("Missing 'claude_thoughts' section in XML.")

    think = claude_thoughts.find('think')
    think_description = think.text.strip() if think is not None and think.text and think.text.strip() else None

    # Since the XML does not have 'reasoning_strategies', 'cognitive_bias_mitigation', etc.,
    # these fields will be set to None or empty lists
    reasoning_strategies = []
    cognitive_bias_mitigation = []
    memory_management = {}
    knowledge_integration = {}
    problem_solving_framework = []
    decision_making_parameters = {}

    # If your XML is expected to have these elements elsewhere, adjust the script accordingly.
    # For now, they are left empty or as defaults.

    # Compile all extracted data
    metadata = {
        'metadata_core': core_info,
        'cognitive_processes': cognitive_processes,
        'ethical_guidelines': ethical_guidelines,
        'metadata_hologram': {
            'description': hologram_description,
            'key_parameters': key_parameters,
            'equations': equations,
            'parameters_description': parameters_description
        },
        'answer_operator': {
            'description': ao_description,
            'response_structuring': response_structuring,
            'quality_metrics': quality_metrics,
            'optimization_parameters': optimization_parameters,
            'post_processing': post_processing,
            'feedback_loop': feedback_loop
        },
        'think': {
            'description': think_description,
            'reasoning_strategies': reasoning_strategies,
            'cognitive_bias_mitigation': cognitive_bias_mitigation,
            'memory_management': memory_management,
            'knowledge_integration': knowledge_integration,
            'problem_solving_framework': problem_solving_framework,
            'decision_making_parameters': decision_making_parameters
        }
    }

    return metadata

if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("Usage: python parse_holographic_metadata.py <path_to_xml>")
        sys.exit(1)

    xml_path = sys.argv[1]
    try:
        metadata = parse_holographic_metadata(xml_path)
        print(json.dumps(metadata, indent=2))
    except Exception as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)
