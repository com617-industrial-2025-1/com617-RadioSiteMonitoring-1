# Pro Television PT73070 DAB Transmitter - useful measurements

## Data Collection

The following SNMP values are selected for the snmpsim simulator and OpenNMS configuration

|oid                                   |name                               | type            |description                  |notes                    |
|:-                                    |:-                                 |:-               |:-                           |:-                       |
| .1.3.6.1.4.1.18086.3070.4.17.0       | pt3070OutputEffectiveLevel        | INTEGER32       | Effective RF Output Level   |UNITS "0.01 dBm"         |
| .1.3.6.1.4.1.18086.3070.4.18.0       | pt3070OutputActualLevel           | INTEGER32       | Actual RF Output Level      |UNITS "0.01 dBm"         |
| .1.3.6.1.4.1.18086.3070.4.19.0       | pt3070OutputRfDetectedActualLevel | INTEGER32       | Detected Output Level for RF|UNITS "0.01 dBm"         |
| .1.3.6.1.4.1.18086.3070.7.14.0       | pt3070GpsVisibleSatellitesSnr     | INTEGER32       | Returns the average signal to noise ratio of all visible satellites via the built-in GPS receiver  | UNITS 0.1 dBHz  |
| .1.3.6.1.4.1.18086.3070.7.22.0       | pt3070GpsTrackedSatellitesSnr     | INTEGER32       | Returns the average signal to noise ratio of all tracked satellites via the built-in GPS receiver  | UNITS 0.1 dBHz  |

simulated values `draytek2860-pri.snmprec` (not from SNMP walk)

```
1.3.6.1.2.1.1.1.0|4|PT3070
1.3.6.1.2.1.1.2.0|6|.1.3.6.1.4.1.18086.3070
1.3.6.1.2.1.1.3.0|67|303319419
1.3.6.1.2.1.1.4.0|4|admin
1.3.6.1.2.1.1.5.0|4|PT3070
1.3.6.1.2.1.1.6.0|4|winchester
1.3.6.1.4.1.18086.3070.4.17.0|2|1000
1.3.6.1.4.1.18086.3070.4.18.0|2|1000
1.3.6.1.4.1.18086.3070.4.19.0|2|1000
1.3.6.1.4.1.18086.3070.7.14.0|2|50
1.3.6.1.4.1.18086.3070.7.22.0|2|50

```

These values are collected in `PT3070-MIB.xml`


## traps

All traps are of the form OID  varbind1 varbind2 varbind3 where varbinds are as follows:


varbind1 -  pt3070NotifMessage .1.3.6.1.4.1.18086.3070.64.1.0  
            Syntax DISPLAYSTRING   The current alarm notification message

varbind2 -  pt3070NotifState  .1.3.6.1.4.1.18086.3070.64.2 
            Syntax    INTEGER {off(0), activated(1) }  The current alarm notification state

varbind3 -  pt3070NotifLocalTime  .1.3.6.1.4.1.18086.3070.64.3
            DateAndTime (OCTET STRING) (SIZE (8 |11)). Hint: 2d-1d-1d,1d:1d:1d.1d,1a1d:1d
            The time the current alarm notification state changed

(In the following examples, replace `horizon` with the address / url of the minion connected to to your site)

### pt3070NotifModulatorAlarm   Modulator Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.3

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.3  .1.3.6.1.4.1.18086.3070.64.1.0  s "Modulator Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorAlarm   Modulator Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.3

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.3  .1.3.6.1.4.1.18086.3070.64.1.0  s "Modulator Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryAlarm   Primary Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.5

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.5  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryAlarm   Primary Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.5

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.5  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryAlarm   Secondary Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.6

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.6  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryAlarm   Secondary Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.6

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.6  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNAlarm   SFN Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.7

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.7  .1.3.6.1.4.1.18086.3070.64.1.0  s "SFN Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNAlarm   SFN Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.7

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.7  .1.3.6.1.4.1.18086.3070.64.1.0  s "SFN Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockAlarm   Reference Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.8

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.8  .1.3.6.1.4.1.18086.3070.64.1.0  s "Reference Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockAlarm   Reference Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.8

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.8  .1.3.6.1.4.1.18086.3070.64.1.0  s "Reference Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFAlarm   RF Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.9

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.9  .1.3.6.1.4.1.18086.3070.64.1.0  s "RF Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFAlarm   RF Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.9

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.9  .1.3.6.1.4.1.18086.3070.64.1.0  s "RF Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSAlarm   GNSS Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.10

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.10  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSAlarm   GNSS Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.10

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.10  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIAlarm   EDI Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.12

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.12  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIAlarm   EDI Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.12

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.12  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalAlarm   External Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.13

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.13  .1.3.6.1.4.1.18086.3070.64.1.0  s "External Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalAlarm   External Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.13

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.13  .1.3.6.1.4.1.18086.3070.64.1.0  s "External Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorAlarm   HW Monitor Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.14

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.14  .1.3.6.1.4.1.18086.3070.64.1.0  s "HW Monitor Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorAlarm   HW Monitor Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.14

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.14  .1.3.6.1.4.1.18086.3070.64.1.0  s "HW Monitor Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommAlarm   Communications Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.15

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.15  .1.3.6.1.4.1.18086.3070.64.1.0  s "Communications Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommAlarm   Communications Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.15

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.15  .1.3.6.1.4.1.18086.3070.64.1.0  s "Communications Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifETIAlarm   ETI Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.16

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.16  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETI Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifETIAlarm   ETI Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.16

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.16  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETI Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalAlarm   Internal Alarms Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.18

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.18  .1.3.6.1.4.1.18086.3070.64.1.0  s "Internal Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalAlarm   Internal Alarms Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.18

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.18  .1.3.6.1.4.1.18086.3070.64.1.0  s "Internal Alarms"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimarySyncLossAlarm   Primary Sync Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.21

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.21  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimarySyncLossAlarm   Primary Sync Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.21

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.21  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimarypktcrcAlarm   Primary PKT Corr by CRC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.22

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.22  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary PKT Corr by CRC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimarypktcrcAlarm   Primary PKT Corr by CRC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.22

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.22  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary PKT Corr by CRC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryBROOPRAlarm   Primary Bitrate OOPR Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.23

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.23  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Bitrate OOPR"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryBROOPRAlarm   Primary Bitrate OOPR Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.23

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.23  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Bitrate OOPR"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCHeaderAlarm   Primary CRC Header Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.24

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.24  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC Header"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCHeaderAlarm   Primary CRC Header Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.24

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.24  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC Header"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCFrameAlarm   Primary CRC Frame Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.25

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.25  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC Frame"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCFrameAlarm   Primary CRC Frame Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.25

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.25  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC Frame"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCMNSCAlarm   Primary CRC MNSC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.26

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.26  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryCRCMNSCAlarm   Primary CRC MNSC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.26

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.26  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary CRC MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryMNSCAlarm   Primary MNSC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.27

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.27  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryMNSCAlarm   Primary MNSC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.27

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.27  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTimestampAlarm   Primary Timestamp Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.28

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.28  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Timestamp"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTimestampAlarm   Primary Timestamp Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.28

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.28  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Timestamp"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryMNSCADDRAlarm   Primary MNSC Address Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.29

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.29  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary MNSC Address"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryMNSCADDRAlarm   Primary MNSC Address Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.29

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.29  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary MNSC Address"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTISTSyncAlarm   Primary TIST Sync Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.30

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.30  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary TIST Sync"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTISTSyncAlarm   Primary TIST Sync Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.30

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.30  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary TIST Sync"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTISTHoldoverAlarm   Primary TIST Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.31

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.31  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary TIST Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifPrimaryTISTHoldoverAlarm   Primary TIST Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.31

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.31  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary TIST Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondarySyncLossAlarm   Secondary Sync Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.32

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.32  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondarySyncLossAlarm   Secondary Sync Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.32

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.32  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondarypktcrcAlarm   Secondary PKT Corr by CRC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.33

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.33  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary PKT Corr by CRC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondarypktcrcAlarm   Secondary PKT Corr by CRC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.33

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.33  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary PKT Corr by CRC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryBROOPRAlarm   Secondary Bitrate OOPR Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.34

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.34  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Bitrate OOPR"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryBROOPRAlarm   Secondary Bitrate OOPR Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.34

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.34  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Bitrate OOPR"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCHeaderAlarm   Secondary CRC Header Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.35

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.35  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC Header"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCHeaderAlarm   Secondary CRC Header Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.35

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.35  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC Header"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCFrameAlarm   Secondary CRC Frame Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.36

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.36  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC Frame"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCFrameAlarm   Secondary CRC Frame Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.36

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.36  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC Frame"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCMNSCAlarm   Secondary CRC MNSC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.37

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.37  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryCRCMNSCAlarm   Secondary CRC MNSC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.37

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.37  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary CRC MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryMNSCAlarm   Secondary MNSC Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.38

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.38  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryMNSCAlarm   Secondary MNSC Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.38

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.38  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary MNSC"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTimestampAlarm   Secondary Timestamp Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.39

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.39  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Timestamp"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTimestampAlarm   Secondary Timestamp Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.39

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.39  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Timestamp"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryMNSCADDRAlarm   Secondary MNSC Address Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.40

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.40  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary MNSC Address"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryMNSCADDRAlarm   Secondary MNSC Address Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.40

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.40  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary MNSC Address"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTISTSyncAlarm   Secondary TIST Sync Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.41

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.41  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary TIST Sync"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTISTSyncAlarm   Secondary TIST Sync Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.41

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.41  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary TIST Sync"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTISTHoldoverAlarm   Secondary TIST Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.42

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.42  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary TIST Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSecondaryTISTHoldoverAlarm   Secondary TIST Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.42

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.42  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary TIST Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFOverloadProtectionAlarm   Overload Protection Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.44

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.44  .1.3.6.1.4.1.18086.3070.64.1.0  s "Overload Protection"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFOverloadProtectionAlarm   Overload Protection Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.44

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.44  .1.3.6.1.4.1.18086.3070.64.1.0  s "Overload Protection"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth0Alarm   ETH0 Conn. State Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.55

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.55  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH0 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth0Alarm   ETH0 Conn. State Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.55

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.55  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH0 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth1Alarm   ETH1 Conn. State Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.56

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.56  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH1 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth1Alarm   ETH1 Conn. State Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.56

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.56  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH1 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth2Alarm   ETH2 Conn. State Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.57

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.57  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH2 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth2Alarm   ETH2 Conn. State Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.57

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.57  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH2 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth3Alarm   ETH3 Conn. State Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.58

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.58  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH3 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth3Alarm   ETH3 Conn. State Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.58

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.58  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH3 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth4Alarm   ETH4 Conn. State Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.59

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.59  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH4 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommeth4Alarm   ETH4 Conn. State Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.59

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.59  .1.3.6.1.4.1.18086.3070.64.1.0  s "ETH4 Conn. State"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput1Alarm   Alarm Input 1 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.72

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.72  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 1"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput1Alarm   Alarm Input 1 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.72

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.72  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 1"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput2Alarm   Alarm Input 2 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.73

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.73  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 2"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput2Alarm   Alarm Input 2 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.73

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.73  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 2"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput3Alarm   Alarm Input 3 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.74

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.74  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 3"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput3Alarm   Alarm Input 3 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.74

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.74  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 3"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput4Alarm   Alarm Input 4 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.75

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.75  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 4"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput4Alarm   Alarm Input 4 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.75

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.75  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 4"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExtern1PPSLossAlarm   Ext. 1PPS Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.76

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.76  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 1PPS Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExtern1PPSLossAlarm   Ext. 1PPS Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.76

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.76  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 1PPS Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockIntern1PPSLossAlarm   Int. 10MHz Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.77

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.77  .1.3.6.1.4.1.18086.3070.64.1.0  s "Int. 10MHz Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockIntern1PPSLossAlarm   Int. 10MHz Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.77

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.77  .1.3.6.1.4.1.18086.3070.64.1.0  s "Int. 10MHz Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExtern10MHzLossAlarm   Ext. 10MHz Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.78

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.78  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 10MHz Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExtern10MHzLossAlarm   Ext. 10MHz Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.78

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.78  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 10MHz Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFAlcRangeAlarm   ALC Range Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.79

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.79  .1.3.6.1.4.1.18086.3070.64.1.0  s "ALC Range"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFAlcRangeAlarm   ALC Range Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.79

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.79  .1.3.6.1.4.1.18086.3070.64.1.0  s "ALC Range"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorResyncAlarm   Resync Error Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.80

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.80  .1.3.6.1.4.1.18086.3070.64.1.0  s "Resync Error"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorResyncAlarm   Resync Error Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.80

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.80  .1.3.6.1.4.1.18086.3070.64.1.0  s "Resync Error"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm   Primary SFN Max Delay + Offset OOR Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.81

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.81  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary SFN Max Delay + Offset OOR"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm   Primary SFN Max Delay + Offset OOR Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.81

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.81  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary SFN Max Delay + Offset OOR"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSPrimaryNetworkDelayExceededAlarm   Primary SFN NW Delay Greater Than Max Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.82

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.82  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary SFN NW Delay Greater Than Max"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSPrimaryNetworkDelayExceededAlarm   Primary SFN NW Delay Greater Than Max Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.82

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.82  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary SFN NW Delay Greater Than Max"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSSecondaryMaxDelayIffsetExceededAlarm   Secondary SFN Max. Delay + Offset OOR Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.84

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.84  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary SFN Max. Delay + Offset OOR"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSSecondaryMaxDelayIffsetExceededAlarm   Secondary SFN Max. Delay + Offset OOR Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.84

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.84  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary SFN Max. Delay + Offset OOR"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSSecondaryNetworkDelayExceededAlarm   Secondary SFN NW Delay Greater Than Max Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.85

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.85  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary SFN NW Delay Greater Than Max"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifSFNTSSecondaryNetworkDelayExceededAlarm   Secondary SFN NW Delay Greater Than Max Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.85

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.85  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary SFN NW Delay Greater Than Max"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFLevelOutOfRangeAlarm   RF Level Out of Range Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.87

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.87  .1.3.6.1.4.1.18086.3070.64.1.0  s "RF Level Out of Range"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRFLevelOutOfRangeAlarm   RF Level Out of Range Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.87

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.87  .1.3.6.1.4.1.18086.3070.64.1.0  s "RF Level Out of Range"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockNTPSyncLossAlarm   NTP Sync Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.89

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.89  .1.3.6.1.4.1.18086.3070.64.1.0  s "NTP Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockNTPSyncLossAlarm   NTP Sync Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.89

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.89  .1.3.6.1.4.1.18086.3070.64.1.0  s "NTP Sync Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSPrimarySeamlessDelayTooSmallAlarm   Primary Delay Margin too Small for Seamless and Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.92

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.92  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Delay Margin too Small for Seamless and Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSPrimarySeamlessDelayTooSmallAlarm   Primary Delay Margin too Small for Seamless and Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.92

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.92  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Delay Margin too Small for Seamless and Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSPrimaryDelayMarginTooSmallAlarm   Primary Delay Margin too Small Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.93

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.93  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Delay Margin too Small"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSPrimaryDelayMarginTooSmallAlarm   Primary Delay Margin too Small Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.93

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.93  .1.3.6.1.4.1.18086.3070.64.1.0  s "Primary Delay Margin too Small"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSSecondarySeamlessDelayTooSmallAlarm   Secondary Delay Margin too Small for Seamless and Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.94

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.94  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Delay Margin too Small for Seamless and Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSSecondarySeamlessDelayTooSmallAlarm   Secondary Delay Margin too Small for Seamless and Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.94

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.94  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Delay Margin too Small for Seamless and Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSSecondaryDelayMarginTooSmallAlarm   Secondary Delay Margin too Small Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.95

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.95  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Delay Margin too Small"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifModulatorTSSecondaryDelayMarginTooSmallAlarm   Secondary Delay Margin too Small Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.95

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.95  .1.3.6.1.4.1.18086.3070.64.1.0  s "Secondary Delay Margin too Small"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSUnlockedAlarm   GNSS Unlocked Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.98

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.98  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Unlocked"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSUnlockedAlarm   GNSS Unlocked Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.98

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.98  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Unlocked"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSAntennaFaultAlarm   GNSS Antenna Fault Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.107

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.107  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Antenna Fault"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSAntennaFaultAlarm   GNSS Antenna Fault Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.107

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.107  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Antenna Fault"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSHoldOverAlarm   GNSS Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.108

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.108  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifGNSSHoldOverAlarm   GNSS Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.108

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.108  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExternal10MHzHoldOverAlarm   Ext. 10MHz Ref Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.109

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.109  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 10MHz Ref Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExternal10MHzHoldOverAlarm   Ext. 10MHz Ref Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.109

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.109  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 10MHz Ref Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExternal1PPSHoldOverAlarm   Ext. 1PPS Ref Holdover Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.110

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.110  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 1PPS Ref Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifRefenceClockExternal1PPSHoldOverAlarm   Ext. 1PPS Ref Holdover Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.110

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.110  .1.3.6.1.4.1.18086.3070.64.1.0  s "Ext. 1PPS Ref Holdover"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx1PackageErrorRationExceededAlarm   EDI RX1 Package Error Ratio Exceeded Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.115

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.115  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX1 Package Error Ratio Exceeded"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx1PackageErrorRationExceededAlarm   EDI RX1 Package Error Ratio Exceeded Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.115

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.115  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX1 Package Error Ratio Exceeded"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx2PackageErrorRationExceededAlarm   EDI RX2 Package Error Ratio Exceeded Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.117

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.117  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX2 Package Error Ratio Exceeded"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx2PackageErrorRationExceededAlarm   EDI RX2 Package Error Ratio Exceeded Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.117

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.117  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX2 Package Error Ratio Exceeded"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx1SyncLossAlarm   EDI RX1 Signal Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.119

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.119  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX1 Signal Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx1SyncLossAlarm   EDI RX1 Signal Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.119

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.119  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX1 Signal Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx2SyncLossAlarm   EDI RX2 Signal Loss Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.121

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.121  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX2 Signal Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifEDIRx2SyncLossAlarm   EDI RX2 Signal Loss Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.121

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.121  .1.3.6.1.4.1.18086.3070.64.1.0  s "EDI RX2 Signal Loss"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalBackplaneAlarm   Backplane Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.129

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.129  .1.3.6.1.4.1.18086.3070.64.1.0  s "Backplane Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalBackplaneAlarm   Backplane Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.129

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.129  .1.3.6.1.4.1.18086.3070.64.1.0  s "Backplane Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalReferenceClockAlarm   Reference Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.132

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.132  .1.3.6.1.4.1.18086.3070.64.1.0  s "Reference Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalReferenceClockAlarm   Reference Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.132

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.132  .1.3.6.1.4.1.18086.3070.64.1.0  s "Reference Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalUpConverterAlarm   Upconverter Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.134

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.134  .1.3.6.1.4.1.18086.3070.64.1.0  s "Upconverter Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalUpConverterAlarm   Upconverter Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.134

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.134  .1.3.6.1.4.1.18086.3070.64.1.0  s "Upconverter Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalDownConverterAlarm   Downconverter Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.135

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.135  .1.3.6.1.4.1.18086.3070.64.1.0  s "Downconverter Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalDownConverterAlarm   Downconverter Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.135

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.135  .1.3.6.1.4.1.18086.3070.64.1.0  s "Downconverter Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalMainboardAlarm   Main board Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.136

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.136  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main board Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalMainboardAlarm   Main board Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.136

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.136  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main board Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalBatteryAlarm   Main Board Battery Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.137

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.137  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board Battery"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalBatteryAlarm   Main Board Battery Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.137

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.137  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board Battery"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalFirmware1Alarm   Firmware 1 Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.139

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.139  .1.3.6.1.4.1.18086.3070.64.1.0  s "Firmware 1 Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalFirmware1Alarm   Firmware 1 Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.139

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.139  .1.3.6.1.4.1.18086.3070.64.1.0  s "Firmware 1 Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalGNSSAlarm   GNSS Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.142

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.142  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalGNSSAlarm   GNSS Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.142

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.142  .1.3.6.1.4.1.18086.3070.64.1.0  s "GNSS Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalSatelliteAlarm   Satrecv Status Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.143

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.143  .1.3.6.1.4.1.18086.3070.64.1.0  s "Satrecv Status"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalSatelliteAlarm   Satrecv Status Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.143

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.143  .1.3.6.1.4.1.18086.3070.64.1.0  s "Satrecv Status"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalEthAlarm   EtherNet Port Failure Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.146

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.146  .1.3.6.1.4.1.18086.3070.64.1.0  s "EtherNet Port Failure"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalEthAlarm   EtherNet Port Failure Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.146

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.146  .1.3.6.1.4.1.18086.3070.64.1.0  s "EtherNet Port Failure"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorFPGAAlarm   Main Board FPGA Temperature Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.156

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.156  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board FPGA Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorFPGAAlarm   Main Board FPGA Temperature Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.156

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.156  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board FPGA Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorMainBoardCPUTemperatureAlarm   Main Board CPU Temperature Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.157

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.157  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board CPU Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorMainBoardCPUTemperatureAlarm   Main Board CPU Temperature Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.157

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.157  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board CPU Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorMainBoardTemperatureAlarm   Main Board Temperature Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.158

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.158  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorMainBoardTemperatureAlarm   Main Board Temperature Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.158

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.158  .1.3.6.1.4.1.18086.3070.64.1.0  s "Main Board Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorLeftFanAlarm   Left Chassis Fan Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.159

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.159  .1.3.6.1.4.1.18086.3070.64.1.0  s "Left Chassis Fan"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorLeftFanAlarm   Left Chassis Fan Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.159

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.159  .1.3.6.1.4.1.18086.3070.64.1.0  s "Left Chassis Fan"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorRightFan2Alarm   Right Chassis Fan Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.160

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.160  .1.3.6.1.4.1.18086.3070.64.1.0  s "Right Chassis Fan"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorRightFan2Alarm   Right Chassis Fan Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.160

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.160  .1.3.6.1.4.1.18086.3070.64.1.0  s "Right Chassis Fan"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorBackplaneTemperatureAlarm   Backplane Temperature Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.162

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.162  .1.3.6.1.4.1.18086.3070.64.1.0  s "Backplane Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifHWMonitorBackplaneTemperatureAlarm   Backplane Temperature Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.162

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.162  .1.3.6.1.4.1.18086.3070.64.1.0  s "Backplane Temperature"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalPLLUnlockedAlarm   PLL Out of Lock Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.182

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.182  .1.3.6.1.4.1.18086.3070.64.1.0  s "PLL Out of Lock"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalPLLUnlockedAlarm   PLL Out of Lock Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.182

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.182  .1.3.6.1.4.1.18086.3070.64.1.0  s "PLL Out of Lock"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput5Alarm   Alarm Input 5 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.183

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.183  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 5"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput5Alarm   Alarm Input 5 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.183

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.183  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 5"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput6Alarm   Alarm Input 6 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.186

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.186  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 6"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput6Alarm   Alarm Input 6 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.186

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.186  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 6"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput7Alarm   Alarm Input 7 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.187

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.187  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 7"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput7Alarm   Alarm Input 7 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.187

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.187  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 7"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput8Alarm   Alarm Input 8 Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.188

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.188  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 8"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifExternalInput8Alarm   Alarm Input 8 Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.188

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.188  .1.3.6.1.4.1.18086.3070.64.1.0  s "Alarm Input 8"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalCalibrationAlarm   Calibration Data Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.198

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.198  .1.3.6.1.4.1.18086.3070.64.1.0  s "Calibration Data"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifInternalCalibrationAlarm   Calibration Data Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.198

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.198  .1.3.6.1.4.1.18086.3070.64.1.0  s "Calibration Data"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommnetconfAlarm   Network Configuration Raise 

oid: .1.3.6.1.4.1.18086.3070.64.0.199

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.199  .1.3.6.1.4.1.18086.3070.64.1.0  s "Network Configuration"  .1.3.6.1.4.1.18086.3070.64.2  i   1  .1.3.6.1.4.1.18086.3070.64.3 s ""
```

### pt3070NotifCommnetconfAlarm   Network Configuration Clear 

oid: .1.3.6.1.4.1.18086.3070.64.0.199

```
snmptrap -v 2c -c public horizon:1162    ""   .1.3.6.1.4.1.18086.3070.64.0.199  .1.3.6.1.4.1.18086.3070.64.1.0  s "Network Configuration"  .1.3.6.1.4.1.18086.3070.64.2  i   0  .1.3.6.1.4.1.18086.3070.64.3 s ""
```


