Run the benchmark using `bash test.bash` . Results here:

```
[shlomif@telaviv1 pypy-pickle-benchmark]$ bash test.bash
+ mkdir -p /home/shlomif/tmp
+ pypy3 e657_cache.py
+ args='e657.py 2 2000'
+ python3 e657.py 2 2000
start = 2 ; end = 2000 ; sum = 981747288202

real    0m3.666s
user    0m3.377s
sys     0m0.289s
+ pypy3 e657.py 2 2000
start = 2 ; end = 2000 ; sum = 981747288202

real    0m53.195s
user    0m52.455s
sys     0m0.699s
+ pypy3 e657.py 2 2000
start = 2 ; end = 2000 ; sum = 981747288202

real    0m52.999s
user    0m52.311s
sys     0m0.675s
[shlomif@telaviv1 pypy-pickle-benchmark]$
```
