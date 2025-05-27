def reformat_name(name): # Reformats names from "Last, First" to "First Last"
    if "," in name:
        last, first = name.split(", ")
        if last and first:
            return f"{first.strip()} {last.strip()}"
    return name