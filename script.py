import json
from collections import Counter
from datetime import datetime, timedelta, timezone

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pytz

YEAR = 2024
TIME_ZONE = 'Asia/Kolkata'


def load_times(file_path, tz_name):
    with open(file_path, 'r') as file:
        conversations = json.load(file)

    tz_obj = pytz.timezone(tz_name)
    return [
        datetime.fromtimestamp(conv['create_time'],
                               tz=timezone.utc).astimezone(tz_obj)
        for conv in conversations
    ]


def generate_heatmap(conversation_times, year, tz_name):
    dates = [dt.date() for dt in conversation_times if dt.year == year]
    date_counts = Counter(dates)

    start_date = datetime(year, 1, 1).date()
    end_date = datetime(year, 12, 31).date()
    total_days = (end_date - start_date).days + 1
    all_dates = [start_date + timedelta(days=i) for i in range(total_days)]

    heatmap_data = [
        (((date - start_date).days) // 7, date.weekday(), date_counts.get(date, 0))
        for date in all_dates
    ]

    weeks_in_year = ((end_date - start_date).days) // 7 + 1
    most_active_date = max(date_counts, key=date_counts.get, default=None)
    most_active_count = date_counts[most_active_date] if most_active_date else 0
    p90_value = np.percentile(
        list(date_counts.values()), 90) if date_counts else 1

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_aspect('equal')

    for week, weekday, count in heatmap_data:
        color = plt.cm.Greens(min(count / p90_value, 1)
                              ) if count > 0 else 'lightgray'
        rect = patches.Rectangle((week, weekday), 1, 1, linewidth=0.5,
                                 edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    month_starts = [date for date in all_dates if date.day == 1]
    for month_start in month_starts:
        week = ((month_start - start_date).days) // 7
        ax.text(week + 0.5, -1, month_start.strftime('%b'),
                ha='center', va='center', fontsize=10)

    for week, weekday, count in heatmap_data:
        if count > 0:
            ax.text(week + 0.5, weekday + 0.5, str(count),
                    ha='center', va='center', fontsize=8, color='black')

    ax.set_xlim(-0.5, weeks_in_year + 0.5)
    ax.set_ylim(-0.5, 7.5)
    ax.set_yticks(range(7))
    ax.set_yticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    ax.invert_yaxis()

    total_conversations = sum(date_counts.values())
    title = f"{year} Conversation Heatmap (Total: {total_conversations})"
    if most_active_date:
        formatted_date = most_active_date.strftime('%d-%m-%Y')
        title += f"\nMost Active Day: {formatted_date} with {most_active_count} Conversations\n"
    ax.set_title(title, fontsize=16)

    ax.set_xticks([])

    plt.show()


generate_heatmap(load_times('conversations.json', TIME_ZONE), YEAR, TIME_ZONE)
