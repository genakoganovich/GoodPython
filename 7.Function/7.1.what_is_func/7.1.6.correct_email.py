def check_mail(mail):
    allow = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
    necessary = {"@", "."}
    print("ДА") if necessary <= mail <= allow else print("НЕТ")


msg = set(input().lower())
check_mail(msg)