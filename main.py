from bardapi import Bard

token = 'cghwnpGbh_eWMSc-Sj-7tsEFmzyJeEY6cxV4yw2CXkHB8Z0d6Wauq_N5wQwAZ-UGLjsXlg.'
bard = Bard(token)

response = bard.get_answer("weather in Lviv")

print(response['content'])