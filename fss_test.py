import dart_fss as dart

#Open Dart API Key 설정
api_key = 
dart.set_api_key(api_key=api_key)


#기업 정보 검색 - 상장된 기업 정보 불러오기 회사리스트 반환 클래스
corp_list = dart.corp.get_corp_list()
'''
hybe = corp_list.find_by_corp_name('하이브', exactly=True)[0]
'''

corps = corp_list.find_by_product('휴대폰')
print(corps)