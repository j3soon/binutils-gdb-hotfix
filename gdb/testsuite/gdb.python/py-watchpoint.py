# Copyright (C) 2022 Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This file is part of the GDB testsuite.  It checks Watchpoints
# are deleted after used.

class MyBreakpoint(gdb.Breakpoint):
    def __init__(self, *args, **kwargs):
        gdb.Breakpoint.__init__(self, *args, **kwargs)
        self.i = 0
    def stop(self):
        self.i += 1
        print("Watchpoint Hit:", self.i)
        return False

MyBreakpoint('i', gdb.BP_WATCHPOINT)

print("Python script imported")
