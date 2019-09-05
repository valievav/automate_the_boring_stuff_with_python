'''
You have a task to track member dues for the Club.
This is a job, involving maintaining a spreadsheet of everyone who has paid each month
and emailing reminders to those who haven’t. Write a script that does this for you.
'''
import smtplib, openpyxl


def send_dues_reminders(club_name, file, headers_columns, smtp_service, sender_email, sender_email_password):
    """
    Sends due payment remainders for clients with negative balance from provided Excel spreadsheet.
    :param club_name: string
    :param file: Excel file
    :param headers_columns: dictionary with column headers and responsive columns
    :param smtp_service: valid smtp data
    :param sender_email: valid email
    :param sender_email_password: valid password
    :return:
    """

    # open workbook
    wb = openpyxl.load_workbook(file, data_only=True)  # 'data_only' is for returning Excel values instead of f-las
    sheet = wb.active

    # find column number for each header
    for value in headers_columns.keys():
        for row in sheet.rows:
            for cell in row:
                if isinstance(cell.value, str):  # process only strings
                    if value.lower() == cell.value.lower():
                        headers_columns[value] = cell.column

    clients_due_payments = []

    # find negative balance and form clients_due list
    acc_balance = list(sheet.columns)[headers_columns['Account balance']-1]
    for cell in acc_balance:
        if isinstance(cell.value, int):  # excluding header from data set
            if cell.value < 0:
                due_amount = cell.value*(-1)  # to remove negative sign from value
                email = sheet.cell(row=cell.row, column=headers_columns['Email']).value
                client = sheet.cell(row=cell.row, column=headers_columns['Client']).value
                clients_due_payments.append([client, email, due_amount])

    # connect to email server
    smtp_obj = smtplib.SMTP(smtp_service[0], smtp_service[1])  # connect to google server
    smtp_obj.ehlo()  # handshake
    smtp_obj.starttls()  # start TLS encryption
    smtp_obj.login(sender_email, sender_email_password)

    # send email
    for group in clients_due_payments:
        client = group[0]
        email = group[1]
        due_amount = group[2]
        send_email = smtp_obj.sendmail(sender_email, email, f'Subject: Due payment for {club_name}\n\n'
                        f'Dear {client},\n\nThis is a kindly reminder on the next term payment.'
                        f'\nThe amount due is {due_amount}.'
                        f'\n\nPlease make sure to pay it till the end of the Earth month or the last Blue Moon circle.'
                        f'\nWe do accept crypto currencies and intergalactic coins. '
                        f'Please contact Saddy if you have more questions.'
                        f'\n\nAs usual, see you on the Equestrian trail!'
                        f'\nSincerely, Your Club')
        if send_email == {}:
            print(f"Message for {client} on {due_amount} due has been to {email}.")
        else:
            print(f"Attention! Email for {client}, email {email} has NOT been sent.")
    print("Done.")
    smtp_obj.quit()


establishment_name = "Lucky Horse Members Club"
members_file = "Send_dues Membership Payments Tracker.xlsx"
file_headers_columns = {'Client': 0, 'Email': 0, 'Account balance': 0}
from_email = "*****@gmail.com"
from_email_password = "*****"
smtp_service = ('smtp.gmail.com', 587)

send_dues_reminders(establishment_name, members_file, file_headers_columns, smtp_service, from_email, from_email_password)

