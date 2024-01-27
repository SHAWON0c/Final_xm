class Account:
    accounts=[]
    total_bank_tk=0
    total_bank_loan=0
    number=1000
    def __init__(self,name, email,address,account_type) -> None:
        self.name=name
        self.address=address
        self.email=email
        self.balance=0
        
        self.account_type=account_type
        
        self.trans_history=[]
        self.account_num=Account.generate_account_number()
        Account.accounts.append(self)
        self.loan_lim=2
       # self.loan_lim=2



        self.loan_cnt=0
    @staticmethod
    def generate_account_number():
        Account.number+=1
        return Account.number 
    
    def deposit(self, amount):
        if amount>0:
            self.balance +=amount
            Account.total_bank_tk +=amount
            print(f'\nSuccessfuly Deposited the Amount:-> {amount}')


            self.trans_history.append(f'Deosit:-> {amount}')
        else:
            print('Invalid Deposit Amount, please Provide Valid Ammount ')
        
    def withdraw (self, amount):
        if amount>0 and amount<self.balance:
            self.balance -=amount
            Account.total_bank_tk -=amount
            print(f'\nSuccessfuly Withdraw the Amount:-> {amount}')
            self.trans_history.append(f'Withdraw:-> {amount}')
        else:
            print('Withdrawal amount exceeded')
    


    def Transaction_history(self):
        print(f'----- TRANSACTION HISTORY -----')
        for histo in self.trans_history:
            print(histo)
    def check_available_balance(self):
        print(f'\nCurrent Balance:-> {self.balance}')   

    
    def transfer_money(self,send_id,amount):
        ac=False
        for id in self.accounts:
            
            if send_id==  id.account_num:
                # print('OK ACHE ')
                if amount >0 and amount<self.balance:
                    self.balance -=amount
                    id.balance +=amount
                    ac=True
                    print(f'\ntransfer the amount successfully {amount} ')
                    self.trans_history.append(f'transferred:-> {amount}')
                else:
                    ac=True
                    print('\ninvalid transfer amount')
#Account.total_bank_loan +=amount
# Account.total_bank_tk -=amount
        if ac==False:
            print('\nAccount does not exist')

    def take_loan(self,amount):
        if self.loan_cnt < self.loan_lim:
            if amount>0:
                self.balance +=amount
                self.loan_cnt +=1
                Account.total_bank_loan +=amount
                Account.total_bank_tk -=amount

                #self.loan_cnt +=1
                print(f'\ {amount} tk Loan from bank Has been Withdrawed  Successfully ')
                self.trans_history.append(f'take loan:-> {amount}')
            else:
                print('\nInvalid Loan Amount')
        else:
            print(f'\nloan Limit Exceeded')



    def __repr__(self) -> str:
        print('')
        print(f'name:-> {self.name} ,account type:-> {self.account_type}')
        print(f'balance:-> {self.balance} and email is:-> {self.email}')
        print(f'he live in:-> {self.address}')
        print(f'account number is:-> {self.account_num}')
        # print)
        return ''

class Admin(Account):
    bank_admin=[]
    def __init__(self,name,id,pas) -> None:
        self.name=name
        self.id=id
        self.pas=pas
        self.accountss=[]
        Admin.bank_admin.append(self)
    
    def deleteUser(self,inp):
        ss=False 


                    # print("enter")
            #if ids.account_num==inp:
             #   Account.total_bank_tk -=ids.balance
              #  admin.accountss.remove(ids)
               # Account.accounts.remove(ids)
                
                #ss=True   
        for ids in admin.accountss:

            # print("enter")
            if ids.account_num==inp:
                Account.total_bank_tk -=ids.balance
                admin.accountss.remove(ids)
                Account.accounts.remove(ids)
                
                ss=True


            # else:
            #    print('ENTER')
            
        if ss==True:
            print('\nAccount Delete Successful')
        else:
            #print('ok ache ')
            print('\nThis Account Does Dot in our Database , please Talk to our Admin. Helpline Admin(Shahadat Siddikee Shawon, Cell-019....)')



 

admin=None
user=None
while True:
    print('1. ADMIN')
    print('2. USER')
    print('3. EXIT')
    print('\nHELLO , HOW ARE YOU !')
    op=int(input(' CHO0SE YOUR OPTION :'))

    if op==1:
        while True:

            if admin==None:
                print('\n-----HELLO ADMIN-----')
                ch=input('Register/Login (R/L) : ')
                if ch=='L':
                    print('ADMIN INFO-> NAME:Sha , ID:Admin , PASS:admin123')
                    na=input('ADMIN NAME:')
                    sa=input('ADMIN ID:')
                    de=input('ADMIN PASS:')
                    for adm in Admin.bank_admin:
                        if adm.name==na and adm.id==sa and adm.pas:
                            admin=adm


                elif ch=='R':
                    print('ADMIN INFO-> NAME:Sha.... , ID:Admin... , PASS:admin123...')
                    name=input('ADMIN NAME :')
                    ID=input('ADMIN ID :')
                    pas=input('ADMIN PASS :')
                    admin=Admin(name,ID,pas)




            else:
                print('\n---- WELCOME  ADMIN ----')
                print('1. Create An Account for User')
                print('2. Delete Any User Account')
                print('3. All User Account List')
                print('4. Total Available Balance of The Bank')
                print('5. Total Provided Loan Amount')
                print('6.  ON or off loan feature of the bank')

                print('7. exit\n')


                opet=int(input('CHO0SE OPTIONS:'))

                if opet==1:
                    ne=input('Name:')
                    em=input('Email:')
                    ad=input('Address:')
                    ac=input('Account Type:')
                    acco=Account(ne,em,ad,ac)
                    admin.accountss.append(acco)
                    print('\nAccount HAS BEEN CREATED Successfully , Congratulations !')
                    print(acco)

                elif opet==2:
                    inp=int(input(' Provuide Your Account Number:'))
                    admin.deleteUser(inp)
                    
                elif opet==3:
                    print('=====ALL ACCOUNT IN OUR BANK LIST=====')
                    for person in admin.accountss:
                        print(person)
                elif opet==5:
                    print(f'\nBank Provided Total Loan:-> {admin.total_bank_loan}')

                elif opet==4:
                    print(f'\nBank''s  Total Money:-> {admin.total_bank_tk}')   
                elif opet==6:
                    pass



                elif opet==7:
                    admin=None

                    break
    elif op==2:
        while True:

            if user==None:
                print('\n---------PROVIDE YOUR INFORMATION FOR LOGIN ---------')
                ne=input('User Name:')
                em=input('User Email:')
                ac=input('User Account Type:')   

               # ac=input('User Account Type:')   ac=input('User Account Type:')   
                ad=input('User Address:')
                
                u=False    

                for use in Account.accounts:

                    if use.name==ne and use.email==em and use.address==ad and use.account_type==ac:
                        user=use
                        u=True

                if u==False:
                    print('WE COULDN''T FIND ANY ACCOUNT BASED ON YOUR INFORMATIUON(Please talk to the admin , help line- (0906220)')

            else:
                print('\n-------HI USER-------')
                print('1. Deposit tk in your account')
                print('2. Dithdrawl tk from your account')
                print('3. Available balance')
                print('4. All transaction')
                print('5. Take loan from bank')
                print('6. Transfer tk to another account')
                print('7. exit\n')
                a=int(input('option:'))

                if a==1:
                    b=int(input('Provide the deposit amount : '))
                    user.deposit(b)

                elif a==2:
                    c=int(input('Provide the amount you want to  withdraw: '))
                    user.withdraw(c)
                elif a==4:
                    user.Transaction_history()
                    
                elif a==3:
                    user.check_available_balance()



                elif a==5:
                    tk=int(input('Provide Your Ammount : '))

                    if tk < Account.total_bank_tk:
                        user.take_loan(tk)

                    else:
                        print('ERROR !!, DOES NOT HAVE ENOUGH MONEY ')

                elif a==6:
                    d=int(input('Provide the  transfer account number: '))
                    e=int(input('Priovide The Amount you Want to  Transfer: '))
                    user.transfer_money(d,e)

                elif a==7:
                    #print('ok')
                    user=None
                    break
                #elif a==4:
                 #   user.Transaction_history()

    elif op==3:
        print('\n----------TERMINATED----------')
        break 

    
         


