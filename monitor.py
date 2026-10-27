import psutil

def check_status(usage):
    if usage < 50:
        return "Normal"
    elif usage < 80:
        return "Moderate"
    else:
        return "High"

if __name__ == "__main__":
    try:
        while True:
            # CPU monitoring
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_status = check_status(cpu_usage)

            # RAM monitoring
            memory = psutil.virtual_memory()
            ram_usage = memory.percent
            ram_status = check_status(ram_usage)

            # Display results
            print("CPU Usage:", cpu_usage, "%")
            print("CPU Status:", cpu_status)
            print("RAM Usage:", ram_usage, "%")
            print("RAM Status:", ram_status)
            print("-----------------------------")

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")