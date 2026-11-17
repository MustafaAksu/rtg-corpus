#!/bin/sh
exec g++ -DBOOST_MP_STANDALONE -I/tmp/cpprev/mp/include -I/tmp/cpprev/cfg/include "$@"
