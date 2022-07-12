from re import X
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, TOP, VERTICAL, W, Y, Button, Entry, Frame, Label, LabelFrame, StringVar, Text, Tk, ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.tix import TEXT
from turtle import right, title, width
import mysql.connector
from tkinter.tix import TEXT

class Hospital:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title=title
        self.root.geometry("1680x1050+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbtitle=Label(self.root,bd=8,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=('times new roman',48,'bold'))
        lbtitle.pack(side=TOP,fill=["x"])
        # ========Dataframe========
        DataFrame=Frame(self.root,bd=8,padx=10,relief=RIDGE)
        DataFrame.place(x=0,y=100,width=1430,height=350)
        DataFrameLeft=LabelFrame(DataFrame,bd=12,padx=20,relief=RIDGE,
                                        font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=850,height=300)
        DataframeRight=LabelFrame(DataFrame,bd=12,relief=RIDGE,padx=10,
                                font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=700,y=5,width=550,height=300)
        # ========buttonsframe========
        Buttonframe=Frame(self.root,bd=8,relief=RIDGE )
        Buttonframe.place(x=0,y=430,width=1530,height=70)
        # ====Details frame====
        Detailsframe=Frame(self.root,bd=8,relief=RIDGE)
        Detailsframe.place(x=0,y=500,width=1530,height=150)
        #=== Dataframe Left ===
        lblNameTablet=Label(DataFrameLeft,font=("arial",8,"bold"),text="Name Of Tablets",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        comNameTablet=ttk.Combobox(DataFrameLeft,state="readonly", textvariable=self.Nameoftablets
                                                        ,font=("arial",8,"bold"),width=25)
        comNameTablet['value']=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)
        lb1ref=Label(DataFrameLeft,font=("arial",8,"bold"),text="Refence No:",padx=2)
        lb1ref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.ref,width=25)
        txtref.grid(row=1,column=1)
        lb1Dose=Label(DataFrameLeft,font=("arial",8,"bold"),text="Dose:",padx=2,pady=4)
        lb1Dose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.Dose,width=25)
        txtDose.grid(row=2,column=1)
        lblNoOftablets=Label(DataFrameLeft,font=("arial",8,"bold"),text="No Of Tablets ::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.NumberofTablets,width=25)
        txtNoOftablets.grid(row=3,column=1)
        lbllot=Label(DataFrameLeft,font=("arial",8,"bold"),text="Lot:",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.Lot,width=25)
        txtlot.grid(row=4,column=1)
        lblissueDate=Label(DataFrameLeft,font=("arial",8,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.Issuedate,width=25)
        txtissueDate.grid(row=5,column=1)
        lb1ExpDate=Label(DataFrameLeft,font=("arial",8,"bold"),text="Exp Date:",padx=2,pady=6)
        lb1ExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.ExpDate,width=25)
        txtExpDate.grid(row=6,column=1)
        lblDailyDose=Label(DataFrameLeft,font=("arial",8,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.DailyDose,width=25)
        txtDailyDose.grid(row=7,column=1)
        lblSideEffect=Label(DataFrameLeft,font=("arial",8,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.sideEffect,width=25)
        txtSideEffect.grid(row=8,column=1)
        lb1Furtherinfo=Label(DataFrameLeft,font=("arial",8,"bold"),text="Further Information",padx=2)
        lb1Furtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.FurtherInformation,width=25)
        txtFurtherinfo.grid(row=0,column=3)
        lblBloodPressure=Label(DataFrameLeft,font=("arial",8,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.DrivingUsingMachine,width=25)
        txtBloodPressure.grid(row=1,column=3)
        lb1Storage=Label(DataFrameLeft,font=("arial",8,"bold"),text="Storage Advice:",padx=2,pady=6)
        lb1Storage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.StorageAdvice,width=25)
        txtStorage.grid(row=2,column=3)
        lblMedicine=Label(DataFrameLeft,font=("arial",8,"bold"),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.HowToUseMedication,width=25)
        txtMedicine.grid(row=3,column=3,sticky=W)
        lblPatientId=Label(DataFrameLeft,font=("arial",8,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.PatientId,width=25)
        txtPatientId.grid(row=4,column=3)
        lb1NhsNumber=Label(DataFrameLeft,font=("arial",8,"bold"),text="NHS Number",padx=2,pady=6)
        lb1NhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.nhsNumber,width=25)
        txtNhsNumber.grid(row=5,column=3)
        lblPatientname=Label(DataFrameLeft,font=("arial",8,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.PatientName,width=25)
        txtPatientname.grid(row=6,column=3)
        lb1DateOfBirth=Label(DataFrameLeft,font=("arial",8,"bold"),text="Date of Birth",padx=2,pady=6)
        lb1DateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.DateOfBirth,width=25)
        txtDateOfBirth.grid(row=7,column=3)
        lblPatientAddress=Label(DataFrameLeft,font=("arial",8,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",8,"bold"),textvariable=self.PatientAddress,width=25)
        txtPatientAddress.grid(row=8,column=3)
        #================DataframeRight=====
        self.txtPrescription= Text(DataframeRight, font=("arial",12,"bold"),width=56,height=13,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        # ===================================Table====================================
        #============buttonFrame============
        #=== Buttons ==
        btnPrescription= Button(Buttonframe,text="Priscription",command=self.iPrescription,bg='green',fg='white',font=("arial",12,"bold"),width=18,height=2,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
       
        btnPrescriptionData= Button(Buttonframe,text="Priscription Data",bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate= Button(Buttonframe,text="Update",command=self.update_data,bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete= Button(Buttonframe,text="Delete",command=self.idelete,bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear= Button(Buttonframe,text="Clear",command=self.clear,bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit= Button(Buttonframe,text="Exit",bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        btnExit= Button(Buttonframe,text="Exit",command=self.iExit,bg='green',fg='white',font=("arial",12,"bold"),width=20,height=2,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
        
        #====================================ScrollBar================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate",
  "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=["x"])
        scroll_y.pack(side=RIGHT,fill=["y"])
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
         

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()
    #==========Functionality declaration===============
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="joyjuhi",database="finaldatabase")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvice.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()
                                                                                                    ))
            conn.commit()
            self.fatch_data()
            conn.close()
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="joyjuhi",database="finaldatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                    self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
    def update_data(self):
         conn = mysql.connector.connect(host="localhost",username="root",password="joyjuhi",database="finaldatabase")
         my_cursor = conn.cursor()
         my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,Numberoftablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NHSNumber=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference_No=%s",(
                    self.Nameoftablets.get(),
                    self.Dose.get(),
                    self.Numberoftablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    #self.PatientID.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                    self.ref.get(),
                ))
    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.Numberoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Driving Using Machine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientID:\t\t\t" + self.PatientID.get() + "\n")
        self.txtPrescription.insert(END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")
    def idelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="joyjuhi",database="finaldatabase")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete(1.0,END)
    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit > 0:
            root.destroy()
            return
root=Tk()
ob=Hospital(root)
root.mainloop()
