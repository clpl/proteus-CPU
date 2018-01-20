###############################################################################
# Makefile for project 
###############################################################################

## General options
PROJECT = 
MCU = 80C31
COMPILER = "ASEM-51 (Proteus)"
TARGET = Debug
SHELL = C:\WINDOWS\system32\cmd.exe

## Tools general options

## Processing Tools
ASM=asem.exe
DDX=ASEMDDX.EXE
#  F:/dazuoye/proteus-CPU/80C31/Debug/Debug.HEX: TOOL=ASM
#  Post: $(DDX) $(DDXFLAGS) Debug.lst
#     F:/dazuoye/proteus-CPU/rom_writer/MicroCode2.asm

# Build tree:
all:	Debug

Debug:	Debug.HEX

Debug.HEX:	../../rom_writer/MicroCode2.asm 
	$(ASM) "..\..\rom_writer\MicroCode2.asm" "Debug.HEX" Debug.lst $(ASMFLAGS)  /INCLUDES:"C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\Tools\ASEM51"
	$(DDX) $(DDXFLAGS) Debug.lst

# tidy - delete all temporary files which are not involved in the target generation
tidy:
	rm -rf Debug.lst

# cleanup - delete all generated files
clean:	tidy
	rm -rf Debug.HEX
	rm -rf Debug.SDI
