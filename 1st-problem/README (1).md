# Configuration Diff Tool

## 📌 Objective
Given two configuration strings, `config1` and `config2`, each containing multiple lines of key-value pairs in the format `key=value`, this tool compares the configurations and identifies which keys have been **added**, **removed**, or **modified** from `config1` to `config2`.

The output is returned as a dictionary with the following keys:
- **`added`** → List of key-value pairs that are present in `config2` but not in `config1`.
- **`removed`** → List of key-value pairs that are present in `config1` but not in `config2`.
- **`modified`** → List of key-value pairs where the key exists in both configurations but has different values.

---

## 🧠 Understanding the Problem
Example:

```text
config1 = "host=localhost\nport=8080"
config2 = "host=localhost\nport=9090\nmode=debug"
```

Output:
```python
{
    "added": ["mode=debug"],
    "removed": [],
    "modified": ["port=9090"]
}
```

**Explanation:**
- `mode=debug` → **added**
- `port` changed from `8080` to `9090` → **modified**
- No keys removed.

---

## 🔍 Approach
1. Parse both configuration strings into dictionaries for easy comparison.
2. Compare keys:
   - Keys in both configs with the same value → **ignore**
   - Keys in both configs with different values → **modified**
   - Keys only in `config1` → **removed**
   - Keys only in `config2` → **added**
3. Return results in a structured dictionary.

---

## 📊 Flow Diagram
```
          All Keys
         /       \
  Keys in both   Keys in one only
     /   \
Same Value Different Value
           |
        Modified
```

---

## 💻 Code Implementation

```python
def config_diff(config1: str, config2: str) -> dict:
    dict1 = dict(line.split("=") for line in config1.strip().split("\n"))
    dict2 = dict(line.split("=") for line in config2.strip().split("\n"))

    added = []
    removed = []
    modified = []

    for key in dict1:
        if key not in dict2:
            removed.append(f"{key}={dict1[key]}")
        elif dict1[key] != dict2[key]:
            modified.append(f"{key}={dict2[key]}")

    for key in dict2:
        if key not in dict1:
            added.append(f"{key}={dict2[key]}")

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }
```

---

## 📥 Input Format
- `config1` and `config2` are **non-empty strings** containing multiple lines.
- Each line is in the format:  
  ```
  key=value
  ```
- Lines are separated by newline characters (`\n`).

---

## 📤 Output Format
A dictionary with three keys:
- `added`: list of added key-value pairs.
- `removed`: list of removed key-value pairs.
- `modified`: list of changed key-value pairs.

---

## 🧪 Example Run

```python
config1 = "host=localhost\nport=8080"
config2 = "host=localhost\nport=9090\nmode=debug"

print(config_diff(config1, config2))
```

**Output:**
```python
{
    "added": ["mode=debug"],
    "removed": [],
    "modified": ["port=9090"]
}
```

---

## 🏢 Company Context
This problem was presented as part of an IBM coding challenge.
