#!/usr/bin/env python
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Useful utility functions for orangfuzz.


def countWithDesc(count, desc):
    '''Returns the count number with the description in the format accepted by orangutan.'''
    # Note the spaces before the first "{" and after the second "}".
    return ' { count=' + str(count) + '; ' + desc + ' } '


def writeToFile(args, lines):
    '''Write generated lines to file, including the seed.'''
    lines.append('')  # Ending line break
    if args.outputFilename is None:
        filename = 'script-orangutan-' + str(args.seed) + '.txt'
    else:
        filename = args.outputFilename
    with open(filename, 'wb') as f:
        f.write('# fuzzSeed: ' + str(args.seed) + '\n')
        f.write('\n'.join(lines))
        f.flush()
    print filename + ' has been generated.'

if __name__ == '__main__':
    pass
