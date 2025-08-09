def compare_configs(config1: str, config2: str):
    # Helper: Convert config string to dictionary
    def parse_config(config_str):
        config_dict = {}
        for line in config_str.strip().split("\n"):
            line = line.strip()
            if line and "=" in line:  # Ignore empty lines
                key, value = line.split("=", 1)
                config_dict[key.strip()] = value.strip()
        return config_dict

    # Parse both configs
    dict1 = parse_config(config1)
    dict2 = parse_config(config2)

    # Determine added keys (present in config2 but not in config1)
    added = [f"{k}={dict2[k]}" for k in dict2.keys() - dict1.keys()]

    # Determine removed keys (present in config1 but not in config2)
    removed = [f"{k}={dict1[k]}" for k in dict1.keys() - dict2.keys()]

    # Determine modified keys (present in both but with different values)
    modified = []
    for k in dict1.keys() & dict2.keys():
        if dict1[k] != dict2[k]:
            modified.append({
                "old": f"{k}={dict1[k]}",
                "new": f"{k}={dict2[k]}"
            })

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }


# Example usage
config1 = """
hostname=server1
timeout=30
retries=3
"""

config2 = """
hostname=server2
timeout=30
port=8080
"""

result = compare_configs(config1, config2)
print(result)
