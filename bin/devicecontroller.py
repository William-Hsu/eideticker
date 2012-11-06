#!/usr/bin/env python

import sys
import eideticker


def main(args=sys.argv[1:]):
    parser = eideticker.OptionParser(usage="usage: %prog")

    options, args = parser.parse_args()

    # Create a device object to interface with the phone
    devicePrefs = eideticker.getDevicePrefs(options)
    device = eideticker.getDevice(**devicePrefs)

    print "READY"
    sys.stdout.flush()

    while 1:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break

        tokens = line.rstrip().split()
        if len(tokens) < 1:
            raise Exception("No command")

        (cmd, args) = (tokens[0], tokens[1:])
        device.executeCommand(cmd, args)

if __name__ == '__main__':
    main()
