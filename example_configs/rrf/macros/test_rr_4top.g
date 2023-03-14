
M669 K6 N8 A-115.0:74.0:250.0 B-74.0:115.0:250.0 C74.0:115.0:250.0 D115.0:74.0:250.0 E115.0:-74.0:250.0 F74.0:-115.0:250.0 H-74.0:-115.0:250.0 I-115.0:-74.0:250.0 P100



; Drives
M569 P0 S0 D3 V40                             ; physical drive 0 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P1 S0 D3 V40                             ; physical drive 1 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P2 S0 D3 V40                             ; physical drive 2 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P3 S0 D3 V40                             ; physical drive 3 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P4 S0 D3 V40                             ; physical drive 4 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P5 S0 D3 V40                             ; physical drive 5 goes backwards using TMC2209 driver timings (Stealthchop)
M569 P6 S0 D3 V40                             ; physical drive 6 goes backwards using TMC2209 driver timings (Stealthchop)
; M569 P7 S0 D3 V40                             ; physical drive 7 goes backwards using TMC2209 driver timings (Stealthchop)
; M584 X0 Y1 Z2 U3 V4 W5 A6 B7 R0               ; set drive mapping

; Reprope setup 4 anchors:
M584 X0 Y2 Z4 U6 R0               ; set drive mapping
M669 K6 N4 A-115.0:74.0:250.0 B74.0:115.0:250.0 C115.0:-74.0:250.0 D-74.0:-115.0:250.0 P100
M666 Q0.007 R15.0:15.0:15.0:15.0 U2:2:2:2 O1:1:1:1 L20:20:20:20 H255:255:255:255 H25:25:25:25
M350 X16 Y16 Z16 I1       ; configure 1/16 microstepping with interpolation
M92 X80 Y80 Z80 U80 ; set steps per mm
M566 X900.00 Y900.00 Z900.00 U900.00 ; set maximum instantaneous speed changes (mm/min)
M203 X24000.00 Y24000.00 Z24000.00 U24000.00 ; set maximum speeds (mm/min)
M201 X2000.00 Y2000.00 Z2000.00 U2000.00 ; set accelerations (mm/s^2)
; M906 X800 Y800 Z800 U800 I30                  ; set motor currents (mA) and motor idle factor in per cent
; M906 X1200 Y1200 Z1200 U1200    ; set motor currents (mA)
M906 I30                        ; Idle current percentage

M204 P1500 T2000 ; Set printing acceleration and travel accelerations

G92 X0 Y0 Z0

G0 X0 Y0 Z0
G0 X0 Y0 Z20
G0 X20 Y0 Z20
G0 X20 Y20 Z20
G0 X-20 Y20 Z20
G0 X-20 Y-20 Z20
G0 X20 Y-20 Z20
G0 X20 Y0 Z20
G0 X0 Y0 Z20
G0 X0 Y0 Z0
