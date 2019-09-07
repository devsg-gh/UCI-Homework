Sub homeWorkVba()

'define the variables

Dim ws As Worksheet
Dim I As Long
Dim J As Long
Dim P As Long
Dim totalCount As Variant
Dim uniqueCount As Variant
Dim rngMaxMin As Range
Dim minVal As Double
Dim maxVal As Double
Dim rngHighTot As Range
Dim highVal As Double
'intitate the value of sumCount (to calcuate sum of each ticker value)
sumCount = 0

'Lable cells
Cells(1, 15) = "Total Stock Volume"
Cells(1, 13) = "Yearly Change"
Cells(1, 14) = "Percent Change"
Cells(2, 19) = "Greatest % Increase"
Cells(3, 19) = "Greatest % decrease"
Cells(4, 19) = "Greatest Total Volume"
Cells(1, 20) = "Ticker"
Cells(1, 21) = "Value"
Columns("L:U").EntireColumn.AutoFit


'define for each
For Each ws In ThisWorkbook.Worksheets

ws.Activate

'total count of cells in column A
totalCount = Application.WorksheetFunction.CountA(Columns(1))

'past unique cells in column L
Range(Cells(1, 1), Cells(totalCount, 1)).AdvancedFilter Action:=xlFilterCopy, CopyToRange:=Range("L1"), Unique:=True


'total count of cells in column L
uniqueCount = Application.WorksheetFunction.CountA(Columns(12))


'Iterating through each row to do the total count
I = 2
       
       For J = 2 To totalCount
           If Cells(J + 1, 1).Value <> Cells(J, 1).Value Then
               sumCount = sumCount + Cells(J, 7).Value
               Cells(I, 15).Value = sumCount                       'Total Volume

               sumCount = 0
               I = I + 1
             Else
               sumCount = sumCount + Cells(J, 7).Value

           End If
           Next J

'Calculate the value of Low (Open) Price
I = 2



For J = 2 To totalCount
    If Cells(I, 12).Value = Cells(J, 1).Value Then
    Cells(I, 16).Value = Cells(J, 3).Value
    I = I + 1
    End If
    Next J

I = 2

'Calculate the value of high (Close) Price

For J = 2 To totalCount + 1
    If Cells(J + 1, 1).Value <> Cells(J, 1).Value Then
    Cells(I, 17).Value = Cells(J, 6).Value
    I = I + 1
    End If
    Next J

'Calculate the Difference, percentage and define the rule of background color


For P = 2 To uniqueCount

Cells(P, 13).Value = Cells(P, 17).Value - Cells(P, 16).Value

On Error Resume Next
            Cells(P, 14) = Cells(P, 13).Value / Cells(P, 16).Value
            Cells(P, 14).NumberFormat = "0.00%"

     If Cells(P, 13).Value < 0 Then
                Cells(P, 13).Interior.ColorIndex = 3
            Else
                Cells(P, 13).Interior.ColorIndex = 4

            End If

Next P

'Find out the max, min of % and highest value from sum

            Set rngMaxMin = Range(Cells(2, 14), Cells(uniqueCount, 14))
            minVal = Application.WorksheetFunction.Min(rngMaxMin)
            Cells(3, 21) = minVal
            Cells(3, 21).NumberFormat = "0.00%"
            maxVal = Application.WorksheetFunction.Max(rngMaxMin)
            Cells(2, 21) = maxVal
            Cells(2, 21).NumberFormat = "0.00%"
            Set rngHighTot = Range(Cells(2, 15), Cells(uniqueCount, 15))
            highVal = Application.WorksheetFunction.Max(rngHighTot)
            Cells(4, 21) = highVal
                       
            Range("T2") = "=Index(L2:L3200,match(U2, N2:N3200,0))"
            Range("T3") = "=Index(L2:L3200,match(U3, N2:N3200,0))"
            Range("T4") = "=Index(L2:L3200,match(U4, O2:O3200,0))"
            
            Columns("P:R").Hidden = True

Next

End Sub


