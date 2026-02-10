# Additional info

## 
Hi,
Some MIBs for devices I'm interested in monitoring.

## Pro Television

![alt text](../images/ProTelevision_Tech_250_85_70_s.jpg "Figure ProTelevision_Tech_250_85_70_s.jpg")

https://www.thebroadcastbridge.com/companies/entry/805/protelevision-technologies

Previously known as Philips TV Test Equipment, ProTelevision Technologies (PTT) has more than 50 years experience in the broadcast transmission market. 

https://www.instagram.com/p/Cul-5-6IMHG/?hl=en   ProTelevision Technologies, part of Elenos Group, is a leading provider of cutting-edge modulation solutions. 

https://www.radioworld.com/news-and-business/elenos-group-acquired-by-italys-dacta

(possibly now acquired by Elenos Group https://www.elenos.com/ )

Two mibs for a Pro-Television PT3070.  The MIB downloads are labelled as "general mib" and "system mib", so I assume one covers all Pro-Television devices, and one has the extra bits for the PT7030.

[Pro-Television](../Pro-Televison)

## Tredess

https://www.tredess.com/en

![alt text](../images/tredess-logo.png "Figuretredess-logo.png")

[Tredess](../Tredess)

https://www.tredess.com/en/fourth-series-low-power 

And two files for  Tredess unit, of which one is a ZIP file with all kinds of stuff in it.

I have not gone through the files to examine exactly what is covered,  but the salient points I would like to monitor would be the inputs state (good or bad), system or amplifier temperature, and RF output level.  We currently have no telemetry on any of these units and rely on an off-air receiver to alert us of any issues.

We have four of the Pro-Tel units and 2 of the Tredess units in service.  All sites have an onsite linux PC on which an agent could be installed.

We have one site which uses the ODR-DABMod software, which again has no remote monitoring, and five instances of ODR-DABMux, three of which are under our direct control and two maintained by third parties.   Some remote monitoring of all of these would be useful.

A graphical interface through OpenNMS would be good, but at the simplest, some means of turning an SNMP trap (or poll that indicates an adverse situation) into an email alert would be useful.

Alan
