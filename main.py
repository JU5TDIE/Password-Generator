import random
import string
import time

history = open("history.txt", 'a')

while True:
    print("(1) 알파벳")
    print("(2). 알파벳 + 숫자")
    print("(3) 알파벳 + 숫자 + 특수문자")
    print("")
    method = input("방식 : ")
    
    if method == "1":
        length = input("비밀번호 길이 : ")
        pw = "".join([random.choice(string.uppercase) for _ in range(int(length))])
        now = time.localtime()
        time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        history.write(pw)
        history.write("  -  ")
        history.write(str(time))
        history.write("\n", )
        history.close()
        print(pw)
        break

    elif method == "2":
        length = input("비밀번호 길이 : ")
        pw = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(int(length))])
        now = time.localtime()
        time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        history.write(pw)
        history.write("  -  ")
        history.write(str(time))
        history.write("\n", )
        history.close()
        print(pw)
        break

    elif method == "3":
        length = input("비밀번호 길이 : ")
        pw = "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(int(length))])
        now = time.localtime()
        time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        history.write(pw)
        history.write("  -  ")
        history.write(str(time))
        history.write("\n", )
        history.close()
        print(pw)
        break

    else:
        print("")
        print("Choose Again")
        print("")
