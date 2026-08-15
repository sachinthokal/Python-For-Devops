import psutil


def get_system_metrics(cpu_threshold=85):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return {
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk,
        "cpu_threshold": cpu_threshold,
        "status": "High CPU" if cpu > cpu_threshold else "Healthy",
    }


if __name__ == "__main__":
    print(get_system_metrics())
