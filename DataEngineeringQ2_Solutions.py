def is_valid_indian_number(phone):
    phone = phone.strip()  # Remove spaces
    if phone.startswith("+91"):
        phone = phone[3:]  # Remove +91 prefix
    elif phone.startswith("91"):
        phone = phone[2:]  # Remove 91 prefix
    
    # Check if it has 10 digits and lies in valid range
    if phone.isdigit() and len(phone) == 10 and 6000000000 <= int(phone) <= 9999999999:
        return True
    return False

# Apply to dataset
df["isValidMobile"] = df["phoneNumber"].apply(is_valid_indian_number)
valid_count = df["isValidMobile"].sum()
print(f"Number of valid phone numbers: {valid_count}")
