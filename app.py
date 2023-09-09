from service import service
import schedule
import time
def main():
    schedule.every().day.at("19:00").do(service.run)

    while True:
        # 스케줄러를 실행합니다.
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()