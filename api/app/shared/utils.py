def get_attr(_dict):
    return [attr for attr in _dict.keys() if not attr.startswith("_")]
