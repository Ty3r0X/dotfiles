#!/usr/bin/env python3
 
import psutil
import os
 
padpath = os.path.expanduser('~/.config/polybar/pad.ini')
padconf = '[pad]\npadright = %s'
paddef  = 9
padinc  = 4 
procs   = {
        'pia':  'pia-client',
        'wapp': 'whats-app'
}
 
def isrunning(pname):
    for proc in psutil.process_iter():
        if proc.name().lower() == pname.lower():
            return True
    return False
 
if __name__ == '__main__':
    pad = paddef
 
    for name, pname in procs.items():
        if isrunning(pname):
            pad += padinc
            print('%s: running' % name)
 
    if pad != paddef:
        try:
            with open(padpath, 'w') as fpad:
                    fpad.write(padconf % pad)
            print('pad: %s' % pad)
        except FileNotFoundError:
            print('ERROR: \'%s\' not found' % padpath)
