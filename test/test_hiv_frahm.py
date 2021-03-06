# Copyright (c) 2014. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division, absolute_import

from pepdata import hiv_frahm

def test_load_dataframe():
    df = hiv_frahm.load_dataframe()
    assert df is not None
    assert len(df) > 0

def test_load_set():
    peptides = hiv_frahm.load_set()
    assert peptides is not None
    assert len(peptides) > 0

def test_same_size():
    peptides = hiv_frahm.load_set()
    df = hiv_frahm.load_dataframe()
    assert len(peptides) == len(df)
