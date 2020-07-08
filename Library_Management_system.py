import json
book_list=json.load(open('book_list.json'))
stu=json.load(open('student.json'))
#*************************************INTITUIONAL INFO************************************************
librarian_ID='SITBBSRLIBRN751021'
admin_ID='SITBBSRADMN751021'
pwd_lbrn='S_I_T_BBsiliconR751021LBRN'
pwd_adm='S_I_T_BBsiliconR751021ADMN'
#****************************************BOOK FUNCTIONS***********************************************
def check_name(name):
    if name==' ' or name=='':
            return False
    for vals in name:
        if vals.isalpha()==True:
            continue
        elif vals==' ':
            continue
        else:
            return False
    return True

def book_id_validity(bid):
    cntspc=0
    for vals in bid:
        if vals==' ':
            cntspc+=1
        if vals.isupper()==True:
            continue
        elif vals.isdigit()==True:
            continue
        else:
            print('ID MUST ONLY CONTAIN UPPER CASE LETTERS AND DIGITS')
            return False
    if len(bid)==cntspc:
            return False
    return True

def book_name_validity(name):
    allspl=':()&@!+-*/,.?"'
    cntspc=0
    for vals in name:
        if vals.isalpha()==True:
            continue
        elif vals.isdigit()==True:
            continue
        elif vals==' ':
            cntspc+=1
            continue
        elif vals in allspl:
            continue
        else:
            return False
    if len(name)==cntspc:
        return False
    return True
    
def details_book(book_list):
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('book name',' '*9,'author name',' '*9,'publisher name',' '*9,'book id',' '*9,'subject',' '*9,'amount',' '*9)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    

    for val in book_list:
        print(val['book_name'],' '*(18-len(val['book_name'])),val['author name'],' '*(20-len(val['author name'])),val['publisher'],' '*(23-len(val['publisher'])),val['book_id'],' '*(16-len(val['book_id'])),val['subject'],' '*(16-len(val['subject'])),val['amount'])
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        
def presence_book_name_check(name):
    for vals in book_list:
        if vals['book_name']==name:
            return False
    return True

def presence_book_id_check(bid):
    for vals in book_list:
        if vals['book_id']==bid:
            return False
    return True

def check_num(num):
    if len(num)==0 or num=='' or num=='\n' or num==' ':
            return False
    for vals in num:
        if vals.isdigit()==True:
            continue
        else:
            return False
    return True

def book_add_interface():
    print('--------------------------------------------------------------------------------------')
    print('              WELCOME TO BOOK ADDING INTERFACE,SITBBSR                             ')        
    print('--------------------------------------------------------------------------------------')
    while 1:
        dec=input('\nENTER [1] TO ADD BOOK | [2] TO DISPLAY LIST | ANY KEY TO EXIT   ')
        if dec=='1':
            i=0
            while(1):
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                name=input('\nENTER NAME OF THE BOOK:')
                if presence_book_name_check(name)!=True:
                        print('\n!!!Oops NAME ALREADY TAKEN!!!\n')
                        continue
                if book_name_validity(name)!=True:
                        print('\n!!!Oops INVALID BOOK NAME!!! \n')
                        continue
                break
            print('--------------------------------------------------------------------------------------')
            i=0
            while(1):
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                bid=input('\nENTER BOOK ID:')
                if presence_book_id_check(bid)!=True:
                        print('\n!!!Oops BOOK ID ALREADY TAKEN!!!\n')
                        continue
                if book_id_validity(bid)!=True:
                        print('\n!!!Oops INVALID BOOK ID!!!\n')
                        continue
                break
            print('--------------------------------------------------------------------------------------')
            author=input('\nENTER THE AUTHOR NAME:')
            i=0
            while check_name(author)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                print('n!!Oops WRONG NAME SYNTAX!!\n')
                author=input('\nENTER AUTHOR NAME AGAIN:')
            print('--------------------------------------------------------------------------------------')
            pub=input('\nENTER PUBLISHER NAME:')
            i=0
            while check_name(pub)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                print('\n!!Oops WRONG NAME SYNTAX!!\n')
                pub=input('\nENTER PUBLISHER NAME AGAIN:')
            print('--------------------------------------------------------------------------------------')
            subject=input('\nENTER SUBJECT:')
            i=0
            while check_name(subject)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                print('\n!!Oops WRONG NAME SYNTAX!!\n')
                subject=input('\nENTER SUBJECT AGAIN:')
            print('--------------------------------------------------------------------------------------')
            amount=input('\nENTER NUMBER OF BOOKS AVAILABLE:')
            i=0
            while check_num(amount)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                print('\n!!!INVALID AMOUNT!!!\n')
                amount=input('\nENTER NUMBER OF BOOKS AVAILABLE:')
            amount=int(amount)
            print('--------------------------------------------------------------------------------------')
            b={ 'book_id':bid,
            'book_name':name,
            'amount':amount,
            'subject':subject,
            'author name':author,
            'publisher':pub
            }
            book_list.append(b)
            json.dump(book_list,open('book_list.json','w'))
            print('--------------------------------------------------------------------------------------')
            print('                       SUCCESFULLY CAPTURED DATA')
            print('--------------------------------------------------------------------------------------')

        elif dec=='2':
            details_book(book_list)
        else:
            break
    print('--------------------------------------------------------------------------------------')        
    print('**********************************THANK YOU*************************************')
    print('--------------------------------------------------------------------------------------')

def book_delete_interface():
    print('--------------------------------------------------------------------------------------')
    print('              WELCOME TO BOOK DELETION INTERFACE,SITBBSR                             ')        
    print('--------------------------------------------------------------------------------------')
    while(1):
        dec=input('\nPRESS [1] TO SHOW BOOK LIST [2] TO DELETE A BOOK AND ANY OTHER KEY TO EXIT--->')
        if dec=='2':
            wat=input('\nENTER [1] TO SEARCH BY NAME [2] TO SEARCH BY ID AND ANY OTHER KEY TO EXIT--->')
            if wat=='1':
                i=0
                while(1):
                        i+=1
                        if i==5:
                                print('\nBOT ACTIVITY DETECTED\n')
                                return
                        book_delete_name=input('\nENTER NAME OF BOOK TO DELETE:')
                        if book_name_validity(book_delete_name)!=True:
                                print('\n!!!Oops INVALID NAME!!!\n')
                                continue
                        if presence_book_name_check(book_delete_name)!=False:
                                print('\n!!!BOOK NOT FOUND!!!\n')
                                continue
                        break
                for vals in book_list:
                    if book_delete_name==vals['book_name']:
                        book_list.remove(vals)
                        break
            elif wat=='2':
                i=0
                while(1):
                        i+=1
                        if i==5:
                                print('\nBOT ACTIVITY DETECTED\n')
                                return
                        book_delete_id=input('\nENTER BOOK ID TO DELETE:')
                        if book_id_validity(book_delete_id)!=True:
                                print('\n!!!Oops INVALID BOOK ID!!!\n')
                                continue
                        if presence_book_id_check(book_delete_id)!=False:
                                print('\n!!!Oops BOOK NOT PRESENT!!!\n')
                                continue
                        break
                for vals in book_list:
                    if book_delete_id==vals['book_id']:
                        book_list.remove(vals)
                        break
            else:
                print('\nEXITING...\n')
        elif dec=='1':
            details_book(book_list)
        else:
            print('\nEXITING...\n')
            break   
    json.dump(book_list,open('book_list.json','w'))
    print('--------------------------------------------------------------------------------------')     
    print('***********************************THANK YOU******************************************')
    print('--------------------------------------------------------------------------------------')

def new_name(arg):
    while(1):
        i=0
        new_bname=input('Enter new BOOK NAME:')
        i+=1
        if check_name(new_bname)==False:
                print('INVALID BOOK NAME')
                continue
        if presence_book_name_check(new_bname)==False:
                print('BOOK ALREADY PRESENT')
                continue
        if i==3:
                return arg
        break
    return new_bname

def new_amount(arg):
    i=0
    while(1):
        new_av_amt=input('Enter New amount:')
        i+=1
        if i==3:
                print('COULDN\'T MODIFY')
                return arg
        if check_num(new_av_amt)==False:
                continue
        break
    return new_av_amt

def new_subject(arg):
    i=0
    while(1):
        i+=3
        if i==3:
                print('COULDN\'T MODIFY')
                return arg
        new_sub=input('Enter New Subject:')
        if check_name(new_sub)==False:
                continue
        break   
    return new_sub

def new_id(arg):
    i=0
    while(1):
        new_id=input('Enter New ID')
        i+=1
        if i==3:
                return arg
        if book_id_validity(new_id)==False:
                print('INVALID ID')
                continue
        if presence_book_id_check(new_id)==False:
                print('BOOK ID ALREADY PRESENT')
                continue
        break
    return new_id

def book_finder():
    decider=int(input('Press [1] to pick book by Name or [2] to pick book by ID--->'))
    if decider==2:
        ID=input('ENTER SEARCH ID:')
        for vals in book_list:
            if vals['book_id']==ID:
                return vals
    elif decider==1:
        name=input('ENTER BOOK SEARCH NAME--->')
        for vals in book_list:
            if vals['book_name']==name:
                return vals
    print('!!!Oops BOOK NOT FOUND!!!')
    return None

def modification_interface():
    flag=False
    print('--------------------------------------------------------------------------------------')
    print('              WELCOME TO BOOK MODIFICATION SYSTEM OF SITLIBRARY,BBSR')
    print('--------------------------------------------------------------------------------------')
    while flag==False:
        book_from_list=book_finder()
        if book_from_list!=None:
                flag=True
        else:
                furt=input('\ndo you want to search again(y/n)-->')
                if furt=='n':
                        print('\nERROR\n')
                        return
    print('--------------------------------------------------------------------------------------')
    want=True
    while want!='no':
        print('         SELECT FROM WHAT TO MODIFY')
        print('               [1] BOOK ID')
        print('               [2] BOOK NAME')
        print('               [3] AMOUNT AVAILABLE')
        print('               [4] BOOK SUBJECT')
        choice=input('\nPlease enter your choice-->')
        print('--------------------------------------------------------------------------------------')
        if choice=='1':
            print('THE CURRENT BOOK ID IS--->',book_from_list['book_id'])
            book_from_list['book_id']=new_id(book_from_list['book_id']) 
        elif choice=='2':
            print('\nTHE CURRENT BOOK NAME IS--->',book_from_list['book_name'])
            book_from_list['book_name']=new_name(book_from_list['book_name'])        
        elif choice=='3':
            print('\nNUMBERS OF BOOK AVAILABLE--->',book_from_list['amount'])
            dec=input('\nPress [1] to change value or [2] for Incremenr/Decrement-->')
            if dec=='1':
                book_from_list['amount']=new_amount(book_from_list['amount'])
            elif dec=='2':
                dec_1=input('\nPress[+] for increment and [-] for decrement--->')
                if dec_1=='+':
                    increment_value=int(input('INCREASE BY:'))
                    book_from_list['amount']+=increment_value
                elif dec_1=='-':
                    decrement_value=int(input('DECREASE BY:'))
                    book_from_list['amount']-=decrement_value 
                else:
                    print('\n!!!Oops Operation Unsucessfull!!!\n')
        elif choice=='4':
            print('\nSUBJECT OF THE BOOK--->',book_from_list['subject'])
            book_from_list['subject']=new_subject(book_from_list['subject'])        
        else:    
            print('\n!!!oops INVALID CHOICE!!!\n')
            break
        print('--------------------------------------------------------------------------------------')
        want=input('\nDO YOU WANT TO MODIFY SOMETHING ELSE->')
        print('--------------------------------------------------------------------------------------')
    json.dump(book_list,open('book_list.json','w'))

#*******************************************STUDENT FUNCTIONS*****************************************

def checksic(sic):
        sic_flag=False
        if len(sic)==9:
                sic_flag=True
                for val in sic:        
                        if val.isdigit()==False:
                                return False
                        if int(val)>=0 and int(val)<=9:
                                sic_flag=True
                                continue
                        else:
                                print('!!!Invalid SIC!!!')
                                sic_flag=False
                                break
                
        else:
                sic_flag=False
        return sic_flag               

def checkpass(p):
        cnt_num=0
        cnt_upper=0
        cnt_spl=0
        pass_flag=False
        if len(p)<6 or len(p)>12:
                return False
        l='`~!@#$%^&*()_-+={[}];:\'"?/<>,.*|'
        for vals in p:
                if (vals.isupper())==True:
                        cnt_upper+=1
                if (vals.isdigit())==True:
                        cnt_num+=1
                if vals in l:
                        cnt_spl+=1
                if vals==' ':
                        break
        if cnt_num>0 and cnt_spl>0 and cnt_spl>0:
                pass_flag=True
        else:
                pass_flag=False
                print('YOUR PASS SHOULD CONTAIN A UPPER CASE LETTER , DIGIT , SPECIAL CHARACTER AND NO SPACES')
        if vals==' ':
                pass_flag=False
                print('!!!INVALID Your password Should not include Space')
        if len(p)<8:
                pass_flag=False
        return pass_flag

def checkname(name):
        name_flag=False
        for val in name:
                if (ord(val)>=97 and ord(val)<=122) or (ord(val)>=65 and ord(val)<=90):
                        name_flag=True
                        continue
                else:
                        print('!!!Invalid Name!!!')
                        name_flag=False
                        break
        if name in stu:
                name_flag=False
        return name_flag      

def isnumber(n):
        l='1234567890'
        c=0
        for val in n:
                c+=1
                if val in l:
                        flag=True
                else:
                        return False
        if c!=10:
                flag=False
        return flag

def checkmail(email):
        i=0
        dot_2=0
        cnt_amp=0
        na='\'?/|%^&(){|}+-*'
        while i<len(email):
                if email[i] in na:
                        return False
                elif email[i]=='@':
                        cnt_amp+=1
                        i+=1
                        break
                else:
                        i+=1
                        continue
        if i>=len(email):
                return False
        if email[i]=='.':
                return False
        while i<len(email):
                if email[i]=='.':
                        i+=1
                        dot_2+=1
                        continue
                elif email[i].isalpha()==True:
                        i+=1
                        continue
                else:
                        return False
        if dot_2==1:
                return True
        else:
                return False

def presence_check_name(arg):
        for vals in stu:
                if arg==vals['name']:
                        return False
        return True

def presence_check_sic(arg):
        for vals in stu:
                if arg==vals['sic']:
                        return False
        return True

def presence_check_mail(arg):
        for vals in stu:
                if arg==vals['email id']:
                        return False
        return True

def presence_check_phn(arg):
        for vals in stu:
                if arg==vals['phone number']:
                        return False
        return True

def student_finder():
        wat=input('PRESS [1] TO SEARCH BY NAME [2] TO SEARCH BY SIC AND ANY OTHER KEY TO EXIT--->')
        if wat=='1':
                modify_name=input('ENTER NAME TO SEARCH:')
                while checkname(modify_name)!=True:
                        print('!!!Oops INVALID NAME!!!')
                        modify_name=input('ENTER NAME AGAIN:')
                while presence_check_name(modify_name)!=False:
                        print('!!!Oops STUDENT NOT FOUND!!!')
                        modify_name=input('ENTER NAME AGAIN:')
                for vals in stu:
                        if modify_name==vals['name']:
                                return vals
        elif wat=='2':
                modify_id=input('ENTER SIC TO SEARCH:')
                while checksic(modify_id)!=True:
                        print('!!!Oops Wrong SIC!!!')
                        modify_id=input('ENTER SIC AGAIN:')
                while presence_check_sic(modify_id)!=False:
                        print('!!!Oops SIC NOT FOUND!!!') 
                        modify_id=input('ENTER SIC AGAIN:')
                for vals in stu:
                        if modify_id==vals['sic']:
                                return vals
        else:
                print('EXITTING>>>')
                return None
        return None

def display_student_list():
        print('----------------------------------------------------------------------------------------------------------------------------------')
        print('student name',' '*9,'number',' '*9,'email address',' '*9,'sic',' '*9,'books with student')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        

        for val in stu:
                print(val['name'],' '*(21-len(val['name'])),val['phone number'],' '*(15-len(val['phone number'])),val['email id'],' '*(22-len(val['email id'])),val['sic'],' '*(12-len(val['sic'])),val['book_with_student'])
                print('--------------------------------------------------------------------------------------------------------------------------------------')
                
def add_student_interface():
        print('--------------------------------------------------------------------------------------')
        print('              WELCOME TO STUDENT ADDING INTERFACE,SITBBSR                             ')        
        print('--------------------------------------------------------------------------------------')
        i=0
        name=input('\n             ENTER THE NAME:')         
        while presence_check_name(name)!=True or checkname(name)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED!\n')
                        return
                name=input('\n             ENTER THE NAME AGAIN:')         
        i=0
        print('--------------------------------------------------------------------------------------')

        n=input('\n             ENTER THE PHONE NUMBER:')

        while presence_check_phn(n)!=True or isnumber(n)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED!\n')
                        return
                n=input('\n             ENTER THE PHONE NUMBER AGAIN:')

        print('--------------------------------------------------------------------------------------')


        sic=input('\n             ENTER THE SIC NUMBER:')
        i=0
        while (presence_check_sic(sic)!=True) or (checksic(sic)!=True):
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED!\n')
                        return
                sic=input('\n             ENTER THE SIC NUMBER AGAIN:')


        print('--------------------------------------------------------------------------------------')
        i=0
        email=input('\n             ENTER THE EMAIL ID:')
        while presence_check_mail(email)!=True or checkmail(email)!=True:
                i+=1
                if i==3:
                        print('\nBOT ACTIVITY DETECTED!\n')
                        return
                email=input('\n             ENTER THE EMAIL ID AGAIN:')
                
        print('--------------------------------------------------------------------------------------')
        i=0
        p=input('\n             ENTER THE PASSWORD:')
        while checkpass(p)!=True:
                i+=1
                if i==3:
                        print('\nBOOT ACTIVITY DETECTED!\n')
                        return
                p=input('\n             ENTER THE PASSWORD AGAIN:')
        print('--------------------------------------------------------------------------------------')
        

        student={'name':name,
                'phone number':n,
                'sic':sic,
                'email id':email,
                'password':p,
                'book_with_student':0,
                'book_1_name':'', 
                'book_2_name':'',
                'book_1_subject':'',
                'book_2_subject':'',}
        stu.append(student)
        json.dump(stu,open('student.json','w'))
        print('                     THANK YOU FOR VISITING')
        print('--------------------------------------------------------------------------------------')

def delete_student_interface():
        print('--------------------------------------------------------------------------------------')
        print('              WELCOME TO STUDENT DELETION INTERFACE,SITBBSR                             ')        
        print('--------------------------------------------------------------------------------------')
        while(1):
                dec=input('\nPRESS [1] TO SHOW STUDENT LIST [2] TO DELETE A STUDENT ACCOUNT AND ANY OTHER KEY TO EXIT--->')
                if dec=='1':
                        display_student_list()
                elif dec=='2':
                        wat=input('\nPRESS [1] TO SEARCH BY NAME [2] TO SEARCH BY SIC AND ANY OTHER KEY TO EXIT--->')
                        if wat=='1':
                                while(1):
                                        delete_name=input('\nENTER NAME TO DELETE:')
                                        while checkname(delete_name)!=True:
                                                print('\n!!!Oops INVALID NAME!!!\n')
                                                continue
                                        while presence_check_name(delete_name)!=False:
                                                print('\n!!!Oops STUDENT NOT FOUND!!!\n')
                                                continue
                                        break
                                for vals in stu:
                                        if vals['name']==delete_name:
                                                stu.remove(vals)
                                                break
                        elif wat=='2':
                                while(1):
                                        delete_id=input('\nENTER SIC TO DELETE:')
                                        while checksic(delete_id)!=True:
                                                print('\n!!!Oops Wrong SIC!!!\n')
                                                continue
                                        while presence_check_sic(delete_id)!=False:
                                                print('\n!!!Oops SIC NOT FOUND!!!\n')
                                                continue
                                        break
                                for vals in stu:
                                        if vals['sic']==delete_id:
                                                stu.remove(vals)
                                                break
                        else:
                                print('\nEXITING>>>\n')
                else:
                        print('\nEXITING>>>\n')
                        break
        json.dump(stu,open('student.json','w'))        
        print('--------------------------------------------------------------------------------------')     
        print('***********************************THANK YOU******************************************')
        print('--------------------------------------------------------------------------------------')
                                        
def modify_student_interface(who):
        student_to_be_modified=None
        print('--------------------------------------------------------------------------------------')
        print('              WELCOME TO STUDENT MODIFICATION SYSTEM OF SITLIBRARY,BBSR')
        print('--------------------------------------------------------------------------------------')
        while(1):
                if who=='admn':
                        dec=input('\nPRESS [1] TO SEE STUDENT LIST [2] TO SEARCH STUDENT FOR MODIFICATION-->')
                else:
                        dec='2'
                if dec=='2':
                        while (student_to_be_modified==None) and (who=='admn'):
                                student_to_be_modified=student_finder()
                        if checksic(who)==True:
                                for student_to_be_modified in stu:
                                        if student_to_be_modified['sic']==who:
                                                break
                        print('--------------------------------------------------------------------------------------')
                        want='Y'
                        while want not in 'nN':
                                print('         SELECT FROM WHAT TO MODIFY')
                                if who=='admn':
                                        print('               [1] STUDENT SIC')
                                        print('               [2] STUDENT NAME')
                                print('               [3] STUDENT PHONE NUMBER')
                                print('               [4] STUDENT PASSWORD')
                                print('               [5] STUDENT EMAIL ID')
                                choice=input('Please enter your choice-->')
                                print('--------------------------------------------------------------------------------------')
                                if choice=='1' and who=='admn':
                                        print('\nTHE CURRENT SIC IS: ',student_to_be_modified['sic'])
                                        i=0
                                        while(1):
                                                new_sic=input('\nENTER THE NEW SIC:')
                                                i+=1
                                                if i==3:
                                                        print('\nSECURITY BREACH\n')
                                                        return
                                                if new_sic==student_to_be_modified['sic']:
                                                        continue
                                                if checksic(new_sic)!=True:
                                                        print('\n!!!Oops INVALID SIC!!!\n')
                                                        continue
                                                if presence_check_sic(new_sic)!=True:
                                                        print('\n!!!Oops SIC ALREADY TAKEN!!!\n')
                                                        continue
                                                break
                                        student_to_be_modified['sic']=new_sic
                                        print('\nNEW SIC STORED  |  DATA CAPTURE SUCCESFUL\n')
                                elif choice=='2' and who=='admn':
                                        print('\nTHE CURRENT STUDENT NAME IS :',student_to_be_modified['name'])
                                        while(1):
                                                i=0
                                                new_name=input('\nENTER NEW NAME OF STUDENT:')
                                                i+=1
                                                if i==3:
                                                        print('\nSECURITY BREACH\n')
                                                        return
                                                if new_name==student_to_be_modified['name']:
                                                        continue
                                                if checkname(new_name)!=True:
                                                        print('\n!!!Oops INVALID NAME!!!\n')
                                                        continue
                                                if presence_check_name(new_name)!=True:
                                                        print('\n!!!NAME ALREADY PRESENT!!!\n')
                                                        continue
                                                break
                                        student_to_be_modified['name']=new_name
                                        print('\nNEW NAME STORED  |  DATA CAPTURE SUCCESFUL\n')
                                elif choice=='3':
                                        print('\nTHE CURRENT CURRENT PHONE NUMBER IS:',student_to_be_modified['phone number'])
                                        while(1):
                                                i=0
                                                new_number=input('\nENTER NEW PHONE NUMBER:')
                                                i+=1
                                                if i==3:
                                                        print('\nSECURITY BREACH\n')
                                                        return
                                                if new_number==student_to_be_modified['phone number']:
                                                        continue
                                                if isnumber(new_number)!=True:
                                                        print('\n!!!Oops NOT A NUMBER!!!\n')
                                                        continue
                                                if presence_check_phn(new_number)!=True:
                                                        print('\n!!!PHONE NUMBER EXIST\n')
                                                        continue
                                                break
                                        student_to_be_modified['phone number']=new_number
                                        print('\nNEW NUMBER SAVED  |  DATA CAPTURE SUCCESFUL\n')
                                elif choice=='4':
                                        flag=True
                                        i=0
                                        curr_pwd=input('\nENTER CURRENT PASSWORD:')
                                        while curr_pwd!=student_to_be_modified['password']:
                                                print('\nPASSWORD MISMATCH\n')
                                                curr_pwd=input('\nENTER PASSWORD AGAIN:')
                                                i+=1
                                                if i==3:
                                                        flag=False
                                                        break
                                        if flag==False:
                                                print('\n!!!exiting....security error!!!\n')
                                                break
                                        else:
                                                i=0
                                                new_pwd=input('\nENTER NEW PASSWORD:')
                                                while checkpass(new_pwd)!=True:
                                                        print('\n!!!INVALID PASSWORD!!!\n')
                                                        i+=1
                                                        if i==3:
                                                                print('\nSECURITY BREACH\n')
                                                                return
                                                        new_pwd=input('\nENTER PASSWORD AGAIN:')
                                                new_pwd1=input('\nRE-ENTER PASSWORD :')
                                                i=0
                                                while new_pwd1!=new_pwd:
                                                        print('\n!!!PASSWORD MISMATCH!!!\n')
                                                        i+=1
                                                        if i==3:
                                                                print('\nSECURITY BREACH\n')
                                                                return
                                                        new_pwd1=('\nRE-ENTER PASSWORD:')
                                                student_to_be_modified['password']=new_pwd
                                                print('\nPASSWORD SUCCESSFULLY CHANGED\n')
                                elif choice=='5':
                                        i=0
                                        while(1):
                                                new_email=input('\nENTER NEW EMAIL ID :')
                                                i+=1
                                                if i==3:
                                                        print('\nSECURITY BREACH\n')
                                                        return
                                                if new_email==student_to_be_modified['email id']:
                                                        continue
                                                if checkmail(new_email)!=True:
                                                        print('\n!!!Oops INVALID EMAIL ID!!!\n')
                                                        continue
                                                if presence_check_mail(new_email)!=True:
                                                        print('\n!!!EMAIL ID ALREADY TAKEN!!!\n')
                                                        continue
                                                break
                                        student_to_be_modified['email id']=new_email
                                        print('\nEMAIL ID SUCCESFULLY CHANGED\n')
                                else:
                                        print('\nEXITING>>>\n')
                                print('--------------------------------------------------------------------------------------')
                                json.dump(stu,open('student.json','w'))  
                                want=input('\nDO YOU WANT TO MODIFY SOMETHING ELSE(Y/N)->')
                                print('--------------------------------------------------------------------------------------')
                        if want in 'Nn':
                                break
                elif dec=='1':
                        display_student_list()
                else:
                        print('\nEXITING>>>\n')
                        break

#*********************************************ADDITIONAL FUNCTIONS*****************************************

def login_student():
    print('-'*30)
    print('WELCOME TO STUDENT LOGIN')
    print('-'*30)
    i=0
    student_login_id=input('\nENTER YOUR SIC PLEASE:')
    while (presence_check_sic(student_login_id)!=False) or (checksic(student_login_id)!=True):
        print('\n!!!Oops INVALID SIC!!!\n')
        i+=1
        student_login_id=input('\nENTER SIC AGAIN:')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    for vals in stu:
        if vals['sic']==student_login_id:
            break
    pass_stu=input('\nENTER YOUR PASSWORD:')
    i=0
    while (checkpass(pass_stu)!=True) or (pass_stu!=vals['password']):
        print('\nEITHER YOU HAVE ENTERED AN INVALID PASSWORD OR A WRONG ONE\n')
        pass_stu=input('\nENTER YOUR PASSWORD AGAIN:')
        i+=1
        if i==3:
            print('\n!!!SECURITY BREACH!!!\n')
            return 'STUDENT LOGIN FAILED'
    return vals

def login_admin():
    print('-'*30)
    print('WELCOME TO ADMIN LOGIN')
    print('-'*30)
    ad_id=input('\nENTER ADMIN ID:')
    i=0
    while (book_id_validity(ad_id)!=True): 
        ad_id=input('\nENTER ADMIN ID AGAIN:')
        i+=1
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    while ad_id!=admin_ID:
        print('\n!!!ADMIN ID MISMATCH!!!\n')
        ad_id=input('\nENTER ADMIN ID AGAIN:')
        i+=1
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    i=0
    ad_pwd=input('\nENTER PASSWORD :')
    while checkpass(ad_pwd)!=True:
        print('\nNOT A VALID PASSWORD\n')
        i+=1
        ad_pwd=input('\nENTER PASSWORD :')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    while ad_pwd!=pwd_adm:
        i+=1
        print('\nPASSWORD MISMATCH\n')
        ad_pwd=input('\nENTER PASSWORD :')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    return True
            
def login_librarian():
    print('-'*30)
    print('WELCOME TO LIBRARIAN LOGIN')
    print('-'*30)
    lbrn_id=input('\nENTER LIBRARIAN ID:')
    i=0
    while (book_id_validity(lbrn_id)!=True):
        i+=1 
        lbrn_id=input('\nENTER LIBRARIAN ID AGAIN:')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    while lbrn_id!=librarian_ID:
        i+=1
        print('\n!!!LIBRARIAN ID MISMATCH!!!\n')
        lbrn_id=input('\nENTER LIBRARIAN ID AGAIN:')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    i=0
    lbrn_pwd=input('\nENTER PASSWORD :')
    while checkpass(lbrn_pwd)!=True:
        print('\nNOT A VALID PASSWORD\n')
        lbrn_pwd=input('\nENTER PASSWORD :')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    while lbrn_pwd!=pwd_lbrn:
        i+=1
        print('\nPASSWORD MISMATCH\n')
        lbrn_pwd=input('\nENTER PASSWORD :')
        if i==3:
            print('\nSECURITY BREACH DETECTED!!!\n')
            return False
    return True

def Book_issue_module(book_issue,student_account):
    issue_sucess=False
    while issue_sucess!=True:
        for book_to_be_issued in book_list:
            if (book_to_be_issued['book_name']==book_issue) or (book_to_be_issued['book_id']==book_issue):
                if book_to_be_issued['amount']>=1:
                    issue_sucess=True
                    print('\n                         !!!BOOK IS AVAILABLE!!!\n')
                    break
                else:
                    print('\nBOOK NOT AVAILABLE\n')
                    break
        if issue_sucess==False:
            print('\n                         !!!Book Not Found!!!\n')
            decider=input('\n                         Do You Want to try again(Y/N)?')
            if decider in 'Yy':
                if input('\n                         Press  [1] TO SEARCH BOOK BY NAME [2] TO SEARCH BOOK BY ID:')=='1':
                    book_issue=input('\n                         Enter name of book:')
                else:
                    book_issue=input('\n                         Enter ID of book:')
                
            else:
                return False
    if student_account['book_with_student']<2:
        if student_account['book_with_student']==0:
            student_account['book_1_name']=book_to_be_issued['book_name']
            student_account['book_1_subject']=book_to_be_issued['subject']
            book_to_be_issued['amount']-=1
            student_account['book_with_student']=1
            issue_sucess=True
        else:
            if book_to_be_issued['subject']!=student_account['book_1_subject']:
                student_account['book_2_name']=book_to_be_issued['book_name']
                student_account['book_2_subject']=book_to_be_issued['subject']
                book_to_be_issued['amount']-=1
                student_account['book_with_student']=2
                issue_sucess=True
            else:
                issue_sucess=False
                print('\nYou Already have a book of this subject\n')
    else:
        print('\n\t!!!Oops!!!,It seems you have reached your limit')
        print('According to rules each one can have 2 books only')
        print('PLEASE RETURN A BOOK TO ISSUE\n')
        return False
    return issue_sucess

def issue_book(who):
    print('--------------------------------------------------------------------------------------')
    print('                          WELCOME TO SITBBSR BOOK ISSUE ')
    print('--------------------------------------------------------------------------------------')
    if who=='lbrn':
        i=0
        while(1):
                student_id=input('\nENTER STUDENT SIC TO SEARCH ACCOUNT--->')
                if checksic(student_id)!=True:
                        print('\n!!!INVALID SIC!!!\n')
                        continue
                if presence_check_sic(student_id)!=False:
                        print('\nSTUDENT ACCOUNT NOT FOUND\n')
                        continue
                i+=1
                if i==5:
                        print('\nBOT ACTIVITY DETECTED\n')
                        return
                break
        for student_account in stu:
            if student_account['sic']==student_id:
                break
    elif checksic(who)==True:
        for student_account in stu:
            if student_account['sic']==who:
                break
    else:
        print('\n!!!!!!!!!!!!!!!!!Cant Login!!!!!!!!!!!!!!!!!\n')
        return
    if input('\nPress  [1] to search by name and [2] to search by id:')=='1':
        book_issue=input('\n                         Enter name of book:')
    else:
        book_issue=input('\n                         Enter ID of book:')
    print('--------------------------------------------------------------------------------------')
    if Book_issue_module(book_issue,student_account)==True:
        print('\n                         !!!Congratulations!!! , your Book is Issued\n')
    else:
        print('\n                         !!!Sorry!!!,Please Try again later\n')
    print('--------------------------------------------------------------------------------------')    
    json.dump(stu, open('student.json', 'w'))
    json.dump(book_list,open('book_list.json','w'))
    if input('\n                         Would you Like to issue another book(yes/no):')=='yes':
        if input('                         Press  [1] to search by name and [2] to search by id:')=='1':
            book_issue=input('\n                         Enter name of book:')
        else:
            book_issue=input('\n                         Enter ID of book:')
        if Book_issue_module(book_issue,student_account)==True:
            print('\n                         !!!Congratulations!!! , your Book is Issued\n')
        else:
            print('\n                         !!!Sorry!!!,Please Try again later\n')    
    print('--------------------------------------------------------------------------------------')
    json.dump(stu, open('student.json', 'w'))
    json.dump(book_list,open('book_list.json','w'))
    print('--------------------------------------------------------------------------------------')
    print('************************************THANK YOU*****************************************')


def return_book(who):
        print('--------------------------------------------------------------------------------------')
        print('                          WELCOME TO SITBBSR BOOK RETURN ')
        print('--------------------------------------------------------------------------------------')
        if who=='lbrn':
                student_id=input('\nENTER STUDENT SIC TO SEARCH ACCOUNT--->')
                while checksic(student_id)!=True:
                        print('\n!!!INVALID SIC!!!\n')
                        student_id=input('\nENTER STUDENT SIC TO SEARCH ACCOUNT--->')
                while presence_check_sic(student_id)!=False:
                        print('\nSTUDENT ACCOUNT NOT FOUND\n')
                        student_id=input('\nENTER STUDENT SIC TO SEARCH ACCOUNT--->')
                for student_account in stu:
                        if student_account['sic']==student_id:
                                break
        elif checksic(who)==True:
                for student_account in stu:
                        if student_account['sic']==who:
                                break
        else:
                print('\n!!!!!!!!!!!!!!!!!Cant Login!!!!!!!!!!!!!!!!!\n')
                return False
        print('--------------------------------------------------------------------------------------')
        print('\n                            BOOKS WITH YOU->')
        if student_account['book_1_name']!=None:
                print('BOOK[1]:',student_account['book_1_name'],'(',student_account['book_1_subject'],')')
        if student_account['book_2_name']!=None:
                print('BOOK[2]:',student_account['book_2_name'],'(',student_account['book_2_subject'],')')
        if student_account['book_with_student']==0:
                print('\nNO BOOKS FOUND!!!\n')
        print('--------------------------------------------------------------------------------------')
        while(1):
                if student_account['book_with_student']==2:
                        which=input('\nENTER [1] TO RETURN FIRST BOOK AND [2] TO RETURN SECOND BOOK OR ANY KEY TO EXIT:')
                elif student_account['book_with_student']==0:
                        print('\nNO BOOKS ISSUED\n')
                        break
                else:
                        which='1'
                if which=='1':
                        icha=input('\nDO YOU WANT RETURN THE BOOK?(Y/N)')
                        if icha=='N' or icha=='n':
                                break
                        for vals in book_list:
                                if vals['book_name']==student_account['book_1_name']:
                                        vals['amount']+=1
                                        student_account['book_1_name']=None
                                        student_account['book_1_subject']=None
                                        student_account['book_with_student']-=1
                                        print('\nBOOK1 RETURNED SUCCESSFULLY!!!\n')
                                        break
                        if student_account['book_2_name']!=None:
                                student_account['book_1_name']=student_account['book_2_name']
                                student_account['book_2_name']=None
                                student_account['book_1_subject']=student_account['book_2_subject']
                                student_account['book_2_subject']=None

                elif which=='2':
                        for vals in book_list:
                                if vals['book_name']==student_account['book_2_name']:
                                        vals['amount']+=1
                                        student_account['book_2_name']=None
                                        student_account['book_2_subject']=None
                                        student_account['book_with_student']-=1
                                        print('\nBOOK2 RETURNED SUCCESSFULLY!!!\n')
                                        break
                else:
                        break
                if student_account['book_with_student']>0:
                        want=input('\nDO YOU WANT TO RETURN ANOTHER BOOK(Y/N)?\n')
                        if want=='Y' or want=='y':
                                continue
                        else:
                                break
                else:
                        break
        print('--------------------------------------------------------------------------------------')
        json.dump(stu, open('student.json', 'w'))
        json.dump(book_list,open('book_list.json','w'))
        print('--------------------------------------------------------------------------------------')
        print('************************************THANK YOU*****************************************')

def book_holders():
        which_book=input('\nENTER NAME OF THE BOOK:')
        while book_name_validity(which_book)!=True:
                which_book=input('\nENTER NAME OF THE BOOK AGAIN(INVALID):')
        while presence_book_name_check(which_book)!=False:
                which_book=input('\nENTER NAME OF THE BOOK AGAIN(NOT FOUND):')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        print('student name',' '*9,'number',' '*9,'email address',' '*9,'sic',' '*9,'books with student')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        for val in stu:
                if val['book_1_name']==which_book or val['book_2_name']==which_book:
                        print(val['name'],' '*(21-len(val['name'])),val['phone number'],' '*(15-len(val['phone number'])),val['email id'],' '*(22-len(val['email id'])),val['sic'],' '*(12-len(val['sic'])),val['book_with_student'])
                        print('--------------------------------------------------------------------------------------------------------------------------------------')
                



#*********************************************Main Frame****************************************************

while(1):
    print('-'*35)
    print('                    WELCOME TO SITBBSR LIBRARY')
    print('-'*35)
    print('                 [1] ADMIN LOGIN\n')
    print('                 [2] LIBRARIAN LOGIN\n')
    print('                 [3] STUDENT LOGIN\n')
    print('                 [4] EXIT\n')
    which_login=input('ENTER YOUR CHOICE--->')
    if which_login=='1':
        if login_admin()!=True:
            print('\nADMIN LOGIN FAILED\n')
            continue
        while(1):
            print('-'*35)

            print('                 PRESS [1] ADD A STUDENT ACCOUNT')
            print('                 PRESS [2] MODIFY A STUDENT ACCOUNT')
            print('                 PRESS [3] DELETE A STUDENT ACCOUNT')
            print('                 PRESS [4] SHOW ALL STUDENT ACCOUNTS\n')
            print('                 PRESS [5] ADD A BOOK TO THE LIBRARY')
            print('                 PRESS [6] MODIFY A BOOK FROM THE LIBRARY')
            print('                 PRESS [7] DELETE A BOOK FROM THE LIBRARY')
            print('                 PRESS [8] SHOW ALL BOOKS IN LIBRARY\n')
            print('                 PRESS ANY OTHER KEY TO EXIT')
            wat_2_do=input('\nENTER YOUR CHOICE--->')
            if wat_2_do=='1':
                add_student_interface()
                continue
            elif wat_2_do=='2':
                modify_student_interface('admn')
                continue
            elif wat_2_do=='3':
                delete_student_interface()
                continue
            elif wat_2_do=='4':
                display_student_list()
                continue
            elif wat_2_do=='5':
                book_add_interface()
                continue
            elif wat_2_do=='6':
                modification_interface()
                continue
            elif wat_2_do=='7':
                book_delete_interface()
                continue
            elif wat_2_do=='8':
                details_book(book_list)
                continue
            else:
                print('\nEXITING ADMIN | HOPE YOU ENJOYED OUR SERVICE\n')
                break

    elif which_login=='2':
        if login_librarian()!=True:
            print('\nLIBRARIAN LOGIN FAILED\n')
            continue
        while(1):
            print('          PRESS [1] ISSUE A BOOK TO STUDENT\n')
            print('          PRESS [2] RETURN A BOOK TO LIBRARY\n')
            print('          PRESS [3] TO SEE BOOKS AVAILABLE IN THE LIBRARY\n')
            print('          PRESS [4] SEE STUDENTS HAVING A BOOK\n')
            print('          PRESS ANY OTHER KEY TO EXIT\n')
            wat_2_do=input('ENTER YOUR CHOICE--->')
            if wat_2_do=='1':
                issue_book('lbrn')
                continue
            elif wat_2_do=='2':
                return_book('lbrn')
                continue
            elif wat_2_do=='3':
                details_book(book_list)
                continue
            elif wat_2_do=='4':
                book_holders()
                continue
            else:
                print('\nEXITING LIBRARIAN | HOPE YOU ENJOYED OUR SERVICE\n')
                break
    elif which_login=='3':
                student_account=login_student()
                if student_account==None:
                        print('\nSTUDENT LOGIN FAILED\n')
                        continue
                while(1):
                        print('          PRESS [1] TO MODIFY ACCOUNT\n')
                        print('          PRESS [2] TO SHOW BOOKS AVAILABLE\n')
                        print('          PRESS [3] TO SEE ACCOUNT DETAILS\n')
                        print('          PRESS ANY OTHER KEY TO EXIT\n')
                        wat_2_do=input('\nENTER YOUR CHOICE--->')
                        if wat_2_do=='1':
                                modify_student_interface(student_account['sic'])
                                continue
                        elif wat_2_do=='2':
                                details_book(book_list)
                                continue
                        elif wat_2_do=='3':
                                print('----------------------------------------------------------------------------------------------------------------------------------')
                                print('                                   STUDENT INFORMATION')
                                print('NAME: ',student_account['name'])
                                print('PHONE NUMBER: ',student_account['phone number'])
                                print('EMAIL ADDRESS: ',student_account['email id'])
                                print('SIC: ',student_account['sic'])          
                                print('                                    BOOKS YOU HAVE')
                                if student_account['book_with_student']==1:
                                        print(student_account['book_1_name'],'(',student_account['book_1_subject'],')')
                                elif student_account['book_with_student']==2:
                                        print(student_account['book_1_name'],'(',student_account['book_1_subject'],')')
                                        print(student_account['book_2_name'],'(',student_account['book_2_subject'],')')
                                else:
                                        print('                            NO BOOKS LINKED WITH ACCOUNT')
                                print('----------------------------------------------------------------------------------------------------------------------------------')

                                
                        else:
                                print('\nEXITING LIBRARIAN | HOPE YOU ENJOYED OUR SERVICE\n')
                                break
    else:
            break


