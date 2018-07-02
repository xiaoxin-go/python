import cgi
form = cgi.FieldStorage()               # 解析表单数据
print('Content-type: text/html\n')   # 输出类型
print('<title>Reply Page</title>')  # 输出title
if not 'user' in form:               # 若用户未输入内容
    print('<h1>Who are you?</h1>')  #输出页面内容
else:
    print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))