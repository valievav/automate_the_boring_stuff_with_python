'''
You have a task to track member dues for the Club.
This is a job, involving maintaining a spreadsheet of everyone who has paid each month
and emailing reminders to those who haven’t. Write a script that does this for you.
'''
import smtplib, openpyxl


def send_dues_reminders(club_name, file, headers_columns):
    """
    Send due payment remainders for clients with negative balance from provided Excel spreadsheet.
    :param club_name: string
    :param file: Excel file
    :param headers_columns: dictionary with column headers and responsive columns
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
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)  # connect to google server
    smtp_obj.ehlo()  # handshake
    smtp_obj.starttls()  # start TLS encryption
    smtp_obj.login('*****@gmail.com', '******')

    # send email
    for group in clients_due_payments:
        client = group[0]
        email = group[1]
        due_amount = group[2]
        smtp_obj.sendmail('*****@gmail.com', email, f'Subject: Due payment for {club_name}\n\n'
                        f'Dear {client},\n\nThis is a kindly reminder on the next term payment.'
                        f'\nThe amount due is {due_amount}.'
                        f'\n\nPlease make sure to pay it till the end of the Earth month or the last Blue Moon circle.'
                        f'\nWe do accept crypto currencies and intergalactic coins. '
                        f'Please contact Saddy if you have more questions.'
                        f'\n\nAs usual, see you on the Equestrian trail!'
                        f'\nSincerely, Your Club')
        print(f"Message for {client} on {due_amount} due has been to {email}.")
    print("Done.")
    smtp_obj.quit()


establishment_name = "Lucky Horse Members Club"
members_file = "Send_dues Membership Payments Tracker.xlsx"
file_headers_columns = {'Client': 0, 'Email': 0, 'Account balance': 0}
send_dues_reminders(establishment_name, members_file, file_headers_columns)

