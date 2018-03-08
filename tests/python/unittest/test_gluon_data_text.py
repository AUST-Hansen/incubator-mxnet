# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from __future__ import print_function
import collections
import mxnet as mx
from mxnet.gluon import nn, data
from common import setup_module, with_seed

def get_frequencies(dataset):
    return collections.Counter(x for tup in dataset for x in tup[0]+tup[1][-1:])

def test_wikitext2():
    train = data.text.lm.WikiText2(root='data/wikitext-2', segment='train')
    val = data.text.lm.WikiText2(root='data/wikitext-2', segment='val')
    test = data.text.lm.WikiText2(root='data/wikitext-2', segment='test')
    train_freq, val_freq, test_freq = [get_frequencies(x) for x in [train, val, test]]
    assert len(train) == 58626
    assert len(train_freq) == 33278
    assert len(val) == 6112
    assert len(val_freq) == 13778
    assert len(test) == 6892
    assert len(test_freq) == 14144
    assert test_freq['English'] == 35
    assert len(train[0][0]) == 35
    test_no_pad = data.text.lm.WikiText2(root='data/wikitext-2', segment='test', pad=None)
    assert len(test_no_pad) == 6891

    train_paragraphs = data.text.lm.WikiText2(root='data/wikitext-2', segment='train', seq_len=None)
    assert len(train_paragraphs) == 23767
    assert len(train_paragraphs[0][0]) != 35


if __name__ == '__main__':
    import nose
    nose.runmodule()