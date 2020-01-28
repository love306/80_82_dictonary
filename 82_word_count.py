import time 
def user_input():
	filename = input('請輸入你想開啟的檔案名稱: ')
	return filename


def read_file(filename):
	data = []
	count = 0
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			data.append(line.strip())
			count += 1
			if count % 100000 == 0:
				print(len(data))
	print('資料讀取完畢，共', len(data), '筆資料')
	return data


def create_dictionary(data):
	start_time = time.time()
	wc = {} #word_count
	for line in data:
		words = line.split() #預設值為空白 不會把空白分割成新單字
		for word in words:
			if word in wc:
				wc[word] += 1 
			else:
				wc[word] = 1 #若沒有此字 但=1 則不會當掉而是新增此單字
	end_time = time.time()
	convert_time = end_time - start_time
	print("新增字典內容共使用了-", convert_time, "秒")

	return wc
	
	
def print_higher_word(wc):				
	for word in wc:
		if wc[word] > 1000000:
			print(word, wc[word])
	print(len(wc))
	


def user_search(wc):
	while True:
		word = input('你想查什麼字: ')
		if word == 'q':
			break
		if word in wc:
			print(word, '出現過的次數為', wc[word])
		else:
			print('oh!! xxxx!!!! it does not in there!!!')
	print('感謝使用')
def main():
	filename = user_input()
	data = read_file(filename)
	wc = create_dictionary(data)
	print_higher_word(wc)
	
	user_search(wc)
main()