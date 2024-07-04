from datetime import datetime, timedelta

def convert_to_nepali_date(iso_datetime_str):
    # Parse the ISO datetime string
    utc_dt = datetime.fromisoformat(iso_datetime_str.replace('Z', '+00:00'))
    
    # Convert to Nepal Time (UTC+5:45)
    nepal_dt = utc_dt + timedelta(hours=5, minutes=45)
    
    # Format the date in a clear format
    formatted_date = nepal_dt.strftime('%Y-%m-%d %H:%M:%S')
    
    return formatted_date