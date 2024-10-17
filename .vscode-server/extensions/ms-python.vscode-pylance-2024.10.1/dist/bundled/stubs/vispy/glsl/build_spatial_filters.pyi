#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# glumpy is an OpenGL framework for the fast visualization of numpy arrays.
# Copyright (C) 2009-2011  Nicolas P. Rougier. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY NICOLAS P. ROUGIER ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL NICOLAS P. ROUGIER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of Nicolas P. Rougier.
# -----------------------------------------------------------------------------

import math
from inspect import cleandoc
from itertools import product

import numpy as np

class SpatialFilter:
    def __init__(self, radius=1): ...
    def weight(self, x): ...
    def kernel(self, size=...): ...
    def call_code(self, index): ...

class Linear(SpatialFilter):
    def weight(self, x): ...

class Hanning(SpatialFilter):
    def weight(self, x): ...

class Hamming(SpatialFilter):
    def weight(self, x): ...

class Hermite(SpatialFilter):
    def weight(self, x): ...

class Quadric(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Bicubic(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Kaiser(SpatialFilter):
    def __init__(self, b=6.33): ...
    def bessel_i0(self, x): ...
    def weight(self, x): ...

class CatRom(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Mitchell(SpatialFilter):
    def __init__(self, b=..., c=...): ...
    def weight(self, x): ...

class Spline16(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Spline36(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Gaussian(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Bessel(SpatialFilter):
    def __init__(self): ...
    def besj(self, x: int, n: int): ...
    def weight(self, x): ...

class Sinc(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Lanczos(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

class Blackman(SpatialFilter):
    def __init__(self): ...
    def weight(self, x): ...

def generate_filter_code(radius): ...
def main(): ...
