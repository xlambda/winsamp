
#INCLUDE = -I "E:\Program Files\Microsoft SDKs\Windows\v7.1\Include"
.PHONY: ep
ep: enum_process.c
	gcc enum_process.c -o enum_process.exe -lPsapi

.PHONY: er
er: enum_resources.c
	gcc enum_resources.c -o enum_resources.exe

.PHONY: 01
01: 01.c
	gcc 01.c -o a.exe

.PHONY: clean
clean:
	rm -rf enum_resources.exe
	rm -rf enum_process.exe
	rm -rf resinfo.txt
	rm -rf a.exe
