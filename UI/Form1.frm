VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "交易所报价比价器"
   ClientHeight    =   4365
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   10125
   LinkTopic       =   "Form1"
   ScaleHeight     =   4365
   ScaleWidth      =   10125
   StartUpPosition =   3  '窗口缺省
   Begin VB.Label Label26 
      Caption         =   "-"
      Height          =   375
      Left            =   1680
      TabIndex        =   25
      Top             =   1200
      Width           =   1215
   End
   Begin VB.Label Label25 
      Caption         =   "-"
      Height          =   375
      Left            =   240
      TabIndex        =   24
      Top             =   1200
      Width           =   1215
   End
   Begin VB.Label Label24 
      Caption         =   "-"
      Height          =   375
      Left            =   8160
      TabIndex        =   23
      Top             =   3600
      Width           =   1335
   End
   Begin VB.Label Label23 
      Caption         =   "-"
      Height          =   375
      Left            =   8160
      TabIndex        =   22
      Top             =   3000
      Width           =   1335
   End
   Begin VB.Label Label22 
      Caption         =   "-"
      Height          =   375
      Left            =   8160
      TabIndex        =   21
      Top             =   2400
      Width           =   1335
   End
   Begin VB.Label Label21 
      Caption         =   "-"
      Height          =   375
      Left            =   8160
      TabIndex        =   20
      Top             =   1800
      Width           =   1335
   End
   Begin VB.Label Label20 
      Caption         =   "-"
      Height          =   375
      Left            =   8160
      TabIndex        =   19
      Top             =   1200
      Width           =   1335
   End
   Begin VB.Label Label19 
      Caption         =   "-"
      Height          =   375
      Left            =   6600
      TabIndex        =   18
      Top             =   3600
      Width           =   1335
   End
   Begin VB.Label Label18 
      Caption         =   "-"
      Height          =   375
      Left            =   6600
      TabIndex        =   17
      Top             =   3000
      Width           =   1335
   End
   Begin VB.Label Label17 
      Caption         =   "-"
      Height          =   375
      Left            =   6600
      TabIndex        =   16
      Top             =   2400
      Width           =   1335
   End
   Begin VB.Label Label16 
      Caption         =   "-"
      Height          =   375
      Left            =   6600
      TabIndex        =   15
      Top             =   1800
      Width           =   1335
   End
   Begin VB.Label Label15 
      Caption         =   "-"
      Height          =   375
      Left            =   6600
      TabIndex        =   14
      Top             =   1200
      Width           =   1335
   End
   Begin VB.Label Label14 
      Caption         =   "-"
      Height          =   375
      Left            =   4680
      TabIndex        =   13
      Top             =   3600
      Width           =   1335
   End
   Begin VB.Label Label13 
      Caption         =   "-"
      Height          =   375
      Left            =   4680
      TabIndex        =   12
      Top             =   3000
      Width           =   1335
   End
   Begin VB.Label Label12 
      Caption         =   "-"
      Height          =   375
      Left            =   4680
      TabIndex        =   11
      Top             =   2400
      Width           =   1335
   End
   Begin VB.Label Label11 
      Caption         =   "-"
      Height          =   375
      Left            =   4680
      TabIndex        =   10
      Top             =   1800
      Width           =   1335
   End
   Begin VB.Label Label10 
      Caption         =   "-"
      Height          =   375
      Left            =   4680
      TabIndex        =   9
      Top             =   1200
      Width           =   1335
   End
   Begin VB.Label Label9 
      Caption         =   "-"
      Height          =   375
      Left            =   3120
      TabIndex        =   8
      Top             =   3600
      Width           =   1335
   End
   Begin VB.Label Label8 
      Caption         =   "-"
      Height          =   375
      Left            =   3120
      TabIndex        =   7
      Top             =   3000
      Width           =   1335
   End
   Begin VB.Label Label7 
      Caption         =   "-"
      Height          =   375
      Left            =   3120
      TabIndex        =   6
      Top             =   2400
      Width           =   1335
   End
   Begin VB.Label Label6 
      Caption         =   "-"
      Height          =   375
      Left            =   3120
      TabIndex        =   5
      Top             =   1800
      Width           =   1335
   End
   Begin VB.Label Label5 
      Caption         =   "-"
      Height          =   375
      Left            =   3120
      TabIndex        =   4
      Top             =   1200
      Width           =   1335
   End
   Begin VB.Line Line1 
      X1              =   6360
      X2              =   6360
      Y1              =   1080
      Y2              =   3840
   End
   Begin VB.Label Label4 
      Caption         =   "Btcchina"
      Height          =   375
      Left            =   7560
      TabIndex        =   3
      Top             =   480
      Width           =   1215
   End
   Begin VB.Label Label3 
      Caption         =   "Bitstamp"
      Height          =   375
      Left            =   3960
      TabIndex        =   2
      Top             =   480
      Width           =   1095
   End
   Begin VB.Label Label2 
      Caption         =   "SUM"
      Height          =   375
      Left            =   1800
      TabIndex        =   1
      Top             =   480
      Width           =   975
   End
   Begin VB.Label Label1 
      Caption         =   "价差 %"
      Height          =   375
      Left            =   240
      TabIndex        =   0
      Top             =   480
      Width           =   1095
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
