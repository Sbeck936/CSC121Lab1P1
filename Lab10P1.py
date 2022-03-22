time = input("Enter time [hh:mm:ss]")
colonCnt = 0
componentList = time.split(':')
verification = 'false'
while verification == 'false':
    for char in time:
        if char == ':':
            colonCnt += 1
    if colonCnt != 2:
        print("Must separate hour, minute and second with colons")
        break
    hrLength = len(componentList[0])
    minLength = len(componentList[1])
    secLength = len(componentList[2])
    if hrLength != 2:
        print("Hours must be a two digit number")
        break
    if minLength != 2:
        print("Minutes must be a two digit number")
        break
    if secLength != 2:
        print("Seconds must be a two digit number")
        break
    hour = int(componentList[0])
    minute = int(componentList[1])
    second = int(componentList[2])
    if hour < 0 or hour > 23:
        print("Hours must be a number between 0 and 23")
        break
    if minute < 0 or minute > 59:
        print("Minutes must be a number between 0 and 59")
        break
    if second < 0 or second > 59:
        print("Seconds must be a number between 0 and 59")
        break
    else:
        verification = 'true'
if verification == 'true':
    time = time.replace(":", '')
    print(time)
