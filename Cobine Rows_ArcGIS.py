def combine_fields(typ1, typ2, typ3, shape_length):
    # Check which type has a non-empty value in the current row
    if typ1 is not None and typ1 != "-":
        traffic_type = typ1
    elif typ2 is not None and typ2 != "-":
        traffic_type = typ2
    elif typ3 is not None and typ3 != "-":
        traffic_type = typ3
    else:
        traffic_type = "NaN"  # Set default value for missing entries

    # Round the shape_length and ensure a minimum value of 100
    rounded_length = max(int(shape_length) if shape_length > 100 else 100, round(shape_length))

    # Combine the traffic type and rounded length with an underscore
    verk_typ = f"{traffic_type.upper()}_{rounded_length}"

    return verk_typ
