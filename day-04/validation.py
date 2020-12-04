import re


def validate_date(date, low, high):
    try:
        date = int(date)
        if date >= low and date <= high:
            return 1
        else:
            return 0
    except:
        return 0


def validate_hgt(hgt):
    hgt_regex = re.compile(r"^(?P<value>\d{2,3})(in|cm)$")
    match = re.match(hgt_regex, hgt)
    if match:
        value, unit = match.groups()
        try:
            value = int(value)
        except:
            return 0

        if unit == "in":
            if value >= 59 and value <= 76:
                return 1
            else:
                return 0
        elif unit == "cm":
            if value >= 150 and value <= 193:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


def validate_hcl(hcl):
    hcl_regex = re.compile(r"#[a-f0-9]{6}")
    match = re.match(hcl_regex, hcl)
    if match:
        return 1
    else:
        return 0


def validate_ecl(ecl):
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return 1
    else:
        return 0


def validate_pid(pid):
    pid_regex = re.compile(r"^\d{9}$")
    match = re.match(pid_regex, pid)
    if match:
        return 1
    else:
        return 0
