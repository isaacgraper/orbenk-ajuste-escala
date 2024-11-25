from src.process import Process
import config.dev as dev 

def main():

    p = Process(dev.HEADLESS, dev.URL)
    p.execute()

if __name__ == "__main__":
    main()