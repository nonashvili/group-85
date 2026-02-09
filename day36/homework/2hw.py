def khmovnebis_raodenoba(text):
    khmovnebi = "აეიოუAEIOU"
    count = 0

    for simbolo in text:
        if simbolo in khmovnebi:
            count += 1

    return count


print(khmovnebis_raodenoba("გამარჯობა"))        # 4
print(khmovnebis_raodenoba("Hello World"))      # 3
