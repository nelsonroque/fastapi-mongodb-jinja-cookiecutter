from datetime import datetime
import pytz
import uuid
import hashlib

def get_utc_timestamp():
    """
    
    A function to get the current UTC timestamp.
    
    """
    # Get the current time in your local timezone
    local_time = datetime.now()

    # Convert the local time to UTC
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time

def get_filename_safe_timestamp():
    """
    
    A function to get a timestamp in ISO 8601 format that can be used in filenames.
    
    """
    # Get the current timestamp in ISO 8601 format
    timestamp = get_utc_timestamp().isoformat()

    # Remove characters that are not allowed in filenames
    filename_safe_timestamp = "".join(c if c.isalnum() else "_" for c in timestamp)
    return filename_safe_timestamp

def create_uuid_str():
    """
    
    A function to create a UUID string.
    
    """
    u = str(uuid.uuid4())
    print("uuid: ", u)
    return u

def create_md5_hash(input):
    """
    
    A function to create an MD5 hash from a string.
    
    """

    # Input string
    input_string = input

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the input string encoded as bytes
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the MD5 hash
    md5_hash_hex = md5_hash.hexdigest()

    # Print the MD5 hash
    print("MD5 Hash:", md5_hash_hex)

    return md5_hash_hex