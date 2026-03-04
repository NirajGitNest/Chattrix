import re
import pandas as pd


def preprocess(data):

    # Pattern to detect timestamp
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-'

    # Split messages
    messages = re.split(pattern, data)[1:]

    # Extract timestamps
    dates = re.findall(pattern, data)

    # Create dataframe
    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })

    # Convert messagedate to datetime
    df['message_date'] = pd.to_datetime(df['message_date'],
                                        format='%d/%m/%y, %I:%M %p -')


    # Lists to store users and messages
    users = []
    messages = []

    for message in df['user_message']:

        entry = re.split('([\w\W]+?):\s', message)

        if entry[1:]:  # If username exists
            users.append(entry[1])
            messages.append(entry[2])

        else:  # Group notifications
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace=True)

    return df

