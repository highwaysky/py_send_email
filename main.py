import send

if __name__ == '__main__':
    name = 'zjx'
    email_address = '894383010@qq.com'
    code = r'zjx.png'
    link = 'www.baidu.com'
    date = '2021/08/11'
    send.send_email(name, email_address, code, link, date)
