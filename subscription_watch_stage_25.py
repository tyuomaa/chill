# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SubscriptionWatch
def parse_date(date_str):
    """Parse date from string in various formats, return datetime.date or raise ValueError."""
    if not isinstance(date_str, str) or not date_str.strip():
        raise ValueError("Date must be a non-empty string")
    
    try:
        for fmt in ("%Y-%m-%d", "%d.%m.%y", "%d/%m/%Y", "%Y/%m/%d", "%m-%d-%Y", "%d-%m-%Y"):
            if date_str.strip() and len(date_str) >= 5:
                try:
                    parsed = datetime.strptime(date_str, fmt)
                    return parsed.date()
                except ValueError:
                    continue
        raise ValueError(f"Date '{date_str}' does not match any recognized format")
    except Exception as e:
        if "does not match" in str(e):
            raise
        else:
            raise ValueError(f"Invalid date string: {date_str}") from e


def validate_subscription(subscription):
    """Validate subscription object and return list of error messages."""
    errors = []
    
    required_fields = ["name", "provider", "price"]
    for field in required_fields:
        if not subscription.get(field) or (isinstance(subscription[field], str) and not subscription[field].strip()):
            errors.append(f"Subscription '{subscription.get('name', 'unknown')}' is missing required field: {field}")
    
    if "renewal_date" in subscription:
        try:
            parse_date(subscription["renewal_date"])
        except ValueError as e:
            errors.append(f"Invalid renewal date for subscription '{subscription.get('name', 'unknown')}': {e}")
    
    return errors


def format_error_message(errors):
    """Format list of error messages into a readable string."""
    if not errors:
        return "No errors found."
    formatted = "\n".join(f"  - {error}" for error in errors)
    return f"\nErrors:\n{formatted}"
