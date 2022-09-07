import smtplib
import email.message

#----------------------------------------------------------------------------------------------------------------------
# Email de confirmação de reserva
#----------------------------------------------------------------------------------------------------------------------
def email_reserva(a, b, c, d, e, f):
    corpo_email = f"""
    <p>Olá, {a}!</p>
    <p>Aqui é da ferramentaria. Tudo bom?</p>
    <p>Estou passando só para avisar que a sua reserva da(s) ferramenta(s) {b} foi realizada
     com sucesso para a data {c} e no horário {d} para que possa cumprir a finalidade 
     de {e} conforme solicitado!</p>
    <p>Aproveito para lembrar da importância do cumprimento do horário estipulado para a entrega ({f}),
     uma vez que outros podem precisar usar a mesma ferramenta!</p>
     <p>Desde já agradecemos.</p>
     <p>Att.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Confirmação de reserva de ferramental"
    msg['From'] = 'missao.certificacao@gmail.com'
    msg['To'] = 'silvajonathan76@gmail.com' #'e_usuario'
    password = 'fwhselktwwwbdsct'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais para Login
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email de confirmação enviado com sucesso!!!')

#----------------------------------------------------------------------------------------------------------------------
# Email de atualização de reserva
#----------------------------------------------------------------------------------------------------------------------

# def email_atu(a, b, c, d, e, f):
#     corpo_email = f"""
#     <p>Olá, {ReservaBD.tecnico} aqui é da ferramentaria. Tudo bom?</p>
#     <p>Estou passando só para avisar que a atualização de sua reserva foi realizada com sucesso, conforme segue
#     abaixo:</p>
#     <p>{e_ferramentas} -> {atu_ferramentas}</p>
#     <p>{e_data} -> {atu_data}</p>
#     <p>{e_hora} -> {atu_hora}</p>
#     <p>{descricao} -> {atu_descricao}
#     <p>{e_hora_entrega} -> {atu_hora_entrega}
#     <p>Aproveito para lembrar da importância do cumprimento do horário estipulado para a entrega,
#      uma vez que outras podem precisar usar a mesma ferramenta!</p>
#      <p>Desde já agradecemos.</p>
#      <p>Att.</p>
#     """
#
#     msg = email.message.Message()
#     msg['Subject'] = "Teste da missao certificação"
#     msg['From'] = 'missao.certificacao@gmail.com'
#     msg['To'] = 'silvajonathan76@gmail.com; gabriela.lomeu.a@gmail.com' #'e_usuario'
#     password = 'fwhselktwwwbdsct'
#     msg.add_header('Content-Type', 'text/html')
#     msg.set_payload(corpo_email)
#
#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()
#     # Credenciais para Login
#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#     print('Email de atualização enviado com sucesso!!!')

