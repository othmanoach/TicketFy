from typing import Dict, Any

def key_value_storage(operation: str, group: str, key: str, value: str = '') -> Dict[str, Any]:
    """
    Stores and retrieves data to be persisted between application executions.
    
    Args:
        operation (str): One of the following values: 'store', 'retrieve', and 'delete'.
        group (str): The name of the application without spaces.
        key (str): A distinct, non-empty, and unique identifier for each item to be stored.
        value (str): The value that needs to be stored. Convert non-string values to string. Cannot be empty for the 'store' operation, must be empty for other operations.

    Returns:
        Dict[str, Any]: A dict which contains 'upstream_service_result_code', an HTTP result code from the key_value storage service, and 'kv_pairs', a list of records as a dictionary where the properties are 'key' and 'value'.

    Raises:
        Exception: This function can raise exceptions, but it is not possible to detail here which ones can be raised.

    Additional dependencies:
        No additional dependencies needed.

    Setup:
        No additional setup needed.

    Constraints or Limitations:
        Assume none.
    """
    # Simulated implementation for demonstration. Replace with actual database or file system interaction logic.
    if operation == 'store':
        print(f"Storing {key}: {value} in {group}")
    elif operation == 'retrieve':
        print(f"Retrieving {key} from {group}")
    elif operation == 'delete':
        print(f"Deleting {key} from {group}")
    return {'upstream_service_result_code': 200, 'kv_pairs': [{'key': key, 'value': value}]}