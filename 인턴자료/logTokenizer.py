
# 파일읽어오기
f = open("1.log",'r', encoding="euc-kr")

lines = f.readlines()
count = 0;
traffic = [0]*24 # 시간대별 검색량 측정

# 한줄마다 "ip / 검색어 / 검색시간" 으로 분할할 수 있다
for line in lines:

	tok = line.split(' ')

	if (len(tok) >= 3 and tok[0] != "127.0.0.1"):
		count += 1
		print ("--- no.", count, " ---")
		print ("> ipAddress : ", tok[0], "\n> word[", len(tok)-2, "] : ")
		for i in range (1, len(tok)-1):
			print ("  - ", tok[i])
		print ("> time : ",tok[len(tok)-1])

		timeTok = tok[len(tok)-1].split(':')
		n = int(timeTok[0])
		traffic[n] += 1

# 시간대별 검색량을 출력 
sum = 0
for i in range(0, 24):
	print (">",i, " hr : ", traffic[i])
	sum += traffic[i]

print ("\n> total traffic : ", sum)

f.close()
