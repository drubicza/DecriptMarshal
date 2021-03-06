from sys import stdout
import subprocess as sp, sys, os, marshal, re

p   = '\x1b[0m'
m   = '\x1b[91m'
h   = '\x1b[92m'
k   = '\x1b[93m'
b   = '\x1b[94m'
u   = '\x1b[95m'
bm  = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle2', shell=True, stderr=sp.STDOUT)

def banner():
    print bm + '  _______' + m + '   Compile & Decompile Marshal   ' + p + bm + '__    \n |   _   .-----.--------.---.-.----.-----|  |--.\n |.  1___|  _  |        |  _  |   _|__ --|     |\n |.  |___|_____|__|__|__|___._|__| |_____|__|__|\n |:  1   |' + u + 'Toolkit version.1.0 (Low Scurity) ' + p + bm + '\n |::.. . |' + u + 'coded by Ahmad Riswanto   ' + bm + "                                      \n `-------'" + u + 'contact[WA] : +6289678711863   ' + p


def menu():
    os.system('clear')
    banner()
    print h + 'Menu ' + p + ': \n [' + h + '1' + p + ']. Compile Marshall \n [' + h + '2' + p + ']. Uncompile Marshall \n [' + h + '3' + p + ']. ' + m + 'Keluar \n' + p
    pilih = raw_input(h + '[' + k + '?' + h + ']' + p + ' Pilih--> ')
    if pilih == '1':
        marsh()
    elif pilih == '2':
        unmarsh()
    elif pilih == '3':
        print '\n' + h + '[' + k + '#' + h + ']' + p + ' Salam Dari Pembuat '
        print h + '[' + k + '#' + h + ']' + p + ' Terima Kasih Sudah Menggunakan Program Ini'
        print h + '[' + k + '#' + h + ']' + p + ' Good bye '
        sys.exit()
    elif pilih == '':
        print '\n' + h + '[' + m + '!' + h + ']' + p + ' Jangan Kosong ' + m + '!!!'
        raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter untuk Kembali ke menu')
        menu()
    else:
        print '\n' + h + '[' + m + '!' + h + ']' + p + ' Pilih Yang Bener ' + m + '!!!'
        raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter untuk Kembali Ke Menu ')
        os.system('clear')
        menu()


def marsh():
    try:
        print h + '[' + k + '#' + h + ']' + p + 'Example : /path/marsh.py'
        file = raw_input(h + '[' + k + '?' + h + ']' + p + ' Input File : ')
    except IndexError:
        print h + '[' + m + '!' + h + ']' + p + ' Program Error!!!'
        sys.exit()
    except KeyboardInterrupt:
        print h + '[' + k + '^' + h + ']' + p + ' ctrl+c \n'
        print h + '[' + k + '#' + h + ']' + p + ' Keluar!!!\n'
        time.sleep(3)
        sys.exit()
    except EOFError:
        print h + '[' + k + '^' + h + ']' + p + ' ctrl+d \n'
        print h + '[' + k + '#' + h + ']' + p + ' Keluar!!!\n'
        time.sleep(3)
        sys.exit()
    else:
        try:
            string = open(file, 'r').read()
        except IOError:
            print '\n' + h + '[' + m + '!' + h + ']' + p + ' file Tidak Ada'
            raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter untuk Kembali Ke Menu ')
            os.system('clear')
            menu()
        else:
            try:
                code = compile(string, '<Ahmad_Riswanto>', 'exec')
                print h + '[' + k + '#' + h + ']' + p + ' Sedang Proses Tunggu Sebentar... '
                data = marshal.dumps(code)
            except TypeError:
                banner()
                print h + '[' + k + '#' + h + ']' + p + ' file Sudah di Compiled\n'
                sys.exit()

    fileout = open('out/hasil.py', 'wb')
    fileout.write('#Compiled By Ahmad Riswanto\n')
    fileout.write('#Facebook : https://www.facebook.com/ahmad.riswanto.180\n')
    fileout.write('import marshal\n')
    fileout.write('exec(marshal.loads(' + repr(data) + '))')
    fileout.close()
    print '\n' + h + '[' + k + '#' + h + ']' + p + ' Berhasil Di Compiled'
    print h + '[' + k + '#' + h + ']' + p + ' file saved : out/hasil.py'
    ask = raw_input(h + '[' + k + '?' + h + ']' + p + ' Compile Lagi? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print h + '[' + m + '!' + h + ']' + p + ' Pilih Yang Bener ' + m + '!!!'
        raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter untuk Kembali Ke Menu ')
        os.system('clear')
        menu()


def unmarsh():
    try:
        print h + '[' + k + '#' + h + ']' + p + 'Example : /path/marsh.py'
        file = raw_input(h + '[' + k + '?' + h + ']' + p + ' Input File : ')
    except IndexError:
        print h + '[' + m + '!' + h + ']' + p + ' Program Error!!!'
        sys.exit()
    except KeyboardInterrupt:
        print h + '[' + k + '^' + h + ']' + p + ' ctrl+c \n'
        print h + '[' + k + '#' + h + ']' + p + ' Keluar!!!\n'
        time.sleep(3)
        sys.exit()
    except EOFError:
        print h + '[' + k + '^' + h + ']' + p + ' ctrl+d \n'
        print h + '[' + k + '#' + h + ']' + p + ' Keluar!!!\n'
        time.sleep(3)
        sys.exit()
    else:
        try:
            string = open(file, 'r').read()
        except IOError:
            print '\n' + h + '[' + m + '!' + h + ']' + p + 'file Tidak Ada'
            raw_input(h + '[' + k + '^' + h + ']' + p + 'Tekan Enter untuk Kembali Ke Menu ')
            os.system('clear')
            menu()
        else:
            try:
                x = re.search('((?<![\\\\])[\\\'"])((?:.(?!(?<![\\\\])\\1))*.?)\\1', string).group()
            except Exception as e:
                raise e

    fileout = open('un.py', 'w')
    fileout.write('from sys import stdout\nfrom uncompyle6.main import decompile\nimport marshal\n\n')
    fileout.write('x = marshal.loads(' + x + ')')
    fileout.write("\ntry:\n    decompile(2.7, x, stdout)\nexcept:\n    print 'print Gagal Decompiled'")
    fileout.close()
    print h + '[' + k + '#' + h + ']' + p + ' Sedang Proses Tunggu Sebentar... '
    sp.call('python2 ' + 'un.py > out/jadi.py', shell=True, stderr=sp.STDOUT)
    os.system('rm un.py')
    os.system('clear')
    os.system('cat out/jadi.py')
    print '\n\n' + h + '[' + k + '#' + h + ']' + p + ' Berhasil Di Decompiled'
    print h + '[' + k + '#' + h + ']' + p + ' file saved : out/jadi.py'
    ask = raw_input(h + '[' + k + '?' + h + ']' + p + ' Decompile Lagi? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print h + '[' + m + '!' + h + ']' + p + ' Pilih Yang Bener ' + m + '!!!'
        raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter untuk Kembali Ke Menu ')
        os.system('clear')
        menu()


if __name__ == '__main__':
    if os.path.exists('out'):
        menu()
    else:
        os.system('mkdir out')
        menu()
