Summary:	SMTP Benchmark Suite
Name:		smtp-benchmark
Version:	1.0.3
Release:	%mkrel 4
License:	BSD
Group:		Networking/Other
URL:		http://www.etc.msys.ch/software/smtp-benchmark/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		smtp-benchmark-linux_fix.diff

%description
smtp-benchmark consists of two programs, smtpsend and smtpsink.
Whereas smtpsend is used to send generated e-mail messages using
SMTP to a mail transfer agent, smtpsink is designed to dispose of
received messages as quick as possible.

smtpsend measures the time spent sending e-mails and the number
of e-mails actually sent and outputs statistics after the program
run.

smtpsend can fork one or more parallel senders each using one or
more sequential connections to a SMTP server to deliver one or
more messages per connection.

smtpsink comes in handy when the relaying performance of a MTA is
to be measured.

%prep

%setup -q -n %{name}
%patch0 -p0

%build

gcc %{optflags} -o smtpsend/smtpsend smtpsend/smtpsend.c
gcc %{optflags} -o smtpsink/smtpsink smtpsink/smtpsink.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -m0755 smtpsend/smtpsend %{buildroot}%{_sbindir}/
install -m0755 smtpsink/smtpsink %{buildroot}%{_sbindir}/
install -m0644 smtpsend/smtpsend.8 %{buildroot}%{_mandir}/man8/
install -m0644 smtpsink/smtpsink.8 %{buildroot}%{_mandir}/man8/
  
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README
%{_sbindir}/smtpsend
%{_sbindir}/smtpsink
%{_mandir}/man8/smtpsend.8*
%{_mandir}/man8/smtpsink.8*


