import smtplib
import email.message

#----------------------------------------------------------------------------------------------------------------------
# Email de confirmação de reserva
#----------------------------------------------------------------------------------------------------------------------
def email_reserva(a, b, c, d, e, f, g):
    corpo_email = f"""
    <p>Olá, {a}!</p>
    <p>Aqui é da ferramentaria. Tudo bom?</p>
    <p>Estou passando só para avisar que a sua reserva da ferramenta {b} foi realizada
     com sucesso para a data {c} às {d}h, para que possa cumprir a finalidade
     de {e} conforme solicitado!</p>
    <p>Aproveito para lembrar da importância do cumprimento do horário estipulado para a entrega ({f}h),
     uma vez que outros podem precisar usar a mesma ferramenta!</p>
     <p>Desde já agradecemos.</p>
     <p>Att.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Confirmação de reserva de ferramental"
    msg['From'] = 'missao.certificacao@gmail.com'
    msg['To'] = f'{g}'
    password = 'fwhselktwwwbdsct'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais para Login
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email de confirmação enviado com sucesso!!!')
