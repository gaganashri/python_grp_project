import time
from datetime import datetime

# Example medicine schedule
# Format: "Medicine Name": "HH:MM" (24-hour format)
medicine_schedule = {
    "Vitamin C": "09:00",
    "Painkiller": "14:30",
    "Omega 3": "20:00"
}

def check_medicines():
    while True:
        now = datetime.now().strftime("%H:%M")
        for med, med_time in medicine_schedule.items():
            if now == med_time:
                print(f"⏰ Time to take your medicine: {med} ({med_time})")
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("Medicine Reminder started...")
    print("Scheduled medicines:")
    for med, med_time in medicine_schedule.items():
        print(f"{med}: {med_time}")
    check_medicines()
