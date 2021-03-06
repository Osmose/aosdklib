import os
import subprocess

aosdk_dir = os.path.abspath(os.path.dirname(__file__))


def aosdk_path(path):
    return os.path.join(aosdk_dir, path)

aosdk_files = [aosdk_path(p) for p in [
    # Main files
    'main.c',
    'corlett.c',
    'ao.c',
    'wavedump.c',
    'utils.c',

    # DSF engine
    #'eng_dsf/eng_dsf.c',
    #'eng_dsf/dc_hw.c',
    #'eng_dsf/aica.c',
    #'eng_dsf/aicadsp.c',
    #'eng_dsf/arm7.c',
    #'eng_dsf/arm7i.c',

    # SSF engine
    'eng_ssf/m68kcpu.c',
    'eng_ssf/m68kopac.c',
    'eng_ssf/m68kopdm.c',
    'eng_ssf/m68kopnz.c',
    'eng_ssf/m68kops.c',
    'eng_ssf/scsp.c',
    'eng_ssf/scspdsp.c',
    'eng_ssf/sat_hw.c',
    'eng_ssf/eng_ssf.c',

    # QSF engine
    'eng_qsf/eng_qsf.c',
    'eng_qsf/kabuki.c',
    'eng_qsf/qsound.c',
    'eng_qsf/z80.c',
    'eng_qsf/z80dasm.c',

    # PSF engine
    'eng_psf/eng_psf.c',
    'eng_psf/psx.c',
    'eng_psf/psx_hw.c',
    'eng_psf/peops/spu.c',

    # PSF2 extentions
    'eng_psf/eng_psf2.c',
    'eng_psf/peops2/spu.c',
    'eng_psf/peops2/dma.c',
    'eng_psf/peops2/registers.c',

    # SPU engine (requires PSF engine)
    'eng_psf/eng_spu.c',

    # zlib (included for max portability)
    'zlib/adler32.c',
    'zlib/compress.c',
    'zlib/crc32.c',
    'zlib/gzio.c',
    'zlib/uncompr.c',
    'zlib/deflate.c',
    'zlib/trees.c',
    'zlib/zutil.c',
    'zlib/inflate.c',
    'zlib/infback.c',
    'zlib/inftrees.c',
    'zlib/inffast.c',
]]

outfile = 'aosdk.dylib'
flags = [
    '-o', outfile,

    '-O0',
    '-std=gnu89',
    '-dynamiclib',
    '-flat_namespace',
    '-fPIC',

    '-I' + aosdk_dir,
    '-I' + aosdk_path('eng_ssf'),
    '-I' + aosdk_path('eng_qsf'),
    '-I' + aosdk_path('eng_dsf'),
    '-I' + aosdk_path('zlib'),
    '-lm',
    '-DPATH_MAX=1024',
    '-DHAS_PSX_CPU=1',
    '-DLSB_FIRST=1',

    '-Wno-implicit-function-declaration',
    '-Wno-dangling-else',
    '-Wno-logical-op-parentheses',
    '-Wno-format',
    '-Wno-implicit-int',
    '-Wno-return-type',
    '-Wno-c++11-compat-deprecated-writable-strings',
]

print(aosdk_dir)
subprocess.run(['gcc'] + flags + aosdk_files)
