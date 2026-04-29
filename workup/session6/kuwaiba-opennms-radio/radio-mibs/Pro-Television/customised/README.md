# Pro Television PT73070 DAB Transmitter - useful measurements

# Data Collection

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

