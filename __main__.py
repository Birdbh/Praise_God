import time
import combineintonevideo
import upload

def main():
    while True:
        try:
            combineintonevideo.combine()
            upload.post()

        except:    
            time.sleep(21600)

main()
