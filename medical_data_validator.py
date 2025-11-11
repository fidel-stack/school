import re  # Import the regular expressions module for pattern matching


# -------------------------------
# Sample medical records data
# -------------------------------
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# -----------------------------------------------
# Function to validate individual record fields
# -----------------------------------------------
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Checks each field of a medical record against certain validation rules.
    Returns a list of field names that are invalid.
    """

    # Dictionary of validation rules (constraints)
    constraints = {
        # patient_id must be a string matching pattern like "P1001" or "p1001"
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\\d+', patient_id, re.IGNORECASE),

        # age must be an integer and at least 18
        'age': isinstance(age, int) and age >= 18,

        # gender must be a string equal to 'male' or 'female' (case-insensitive)
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # diagnosis must be a string (or None)
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # medications must be a list containing only strings
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),

        # last_visit_id must be a string matching pattern like "V2301" or "v2301"
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\\d+', last_visit_id, re.IGNORECASE)
    }

    # Return a list of field names that failed validation (i.e., value is False)
    return [key for key, value in constraints.items() if not value]


# -----------------------------------------------
# Function to validate the structure of the data
# -----------------------------------------------
def validate(data):
    """
    Validates a dataset (list of medical records).
    Ensures correct structure and correct values for each field.
    """

    # Check if data is a list or tuple
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False  # Flag to track any invalid entries found

    # Define the expected keys each record should contain
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Iterate through each record (dictionary) in the list
    for index, dictionary in enumerate(data):

        # Ensure each element is a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Check that the dictionary contains exactly the expected keys
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        # Validate each individual field using find_invalid_records()
        invalid_records = find_invalid_records(**dictionary)

        # If any fields are invalid, print the issue
        for key in invalid_records:
            val = dictionary[key]
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True

    # After checking all records:
    if is_invalid:
        return False  # If any record failed validation
    print('Valid format.')  # All good!
    return True


# -----------------------------------------------
# Run the validation function on the dataset
# -----------------------------------------------
validate(medical_records)
