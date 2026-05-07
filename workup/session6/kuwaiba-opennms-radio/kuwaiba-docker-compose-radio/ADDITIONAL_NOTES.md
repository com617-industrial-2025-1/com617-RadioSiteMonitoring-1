# ODR DAB monitoring

[Main Menu](../README.md) | [Kuwaiba Broadcast Radio Demonstration](./README.md) | [ADDITIONAL NOTES](./ADDITIONAL_NOTES.md)

Sine the last version, new devices have been added to the simulation.
The MIBs and configurations are in the [radio-mibs](./radio-mibs) folder.

# Tredess

See [Tredess Config](./radio-mibs/Tredess/TREDESS-FS-MIB/customised/)

polling:

A minimal snmpsim configuration has been created pending an SNMP walk of a real device.

events - alarms:

The trap configuration just generates events and not alarms.
More information and examples are needed to map the events to alarms.


## Pro-Television PT3070

See [Pro-Television PT3070 Config](./radio-mibs/Pro-Television/customised/)

polling:

A snmpsim configuration has been created to give a few statistics pending an SNMP walk of a real device.

events - alarms:

The trap configuration has ben created to generate alarms and events based on a superficial reading of the PT3070 mib

A large number of example traps are provided to test generating and clearning alarms.

## ODR Mux and Modulator

The ODR Mux and modulator use json to show the status of the device

the



